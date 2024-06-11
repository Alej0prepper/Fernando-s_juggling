import pygame
import sys
import math
import json
from siteswap_parser import Siteswap
from learning_logic import generate_siteswap_sequence  # Import the function from the helper file

# Initialize Pygame
pygame.init()

# Load movements from JSON file
with open("./movements.json") as f:
    movements = json.load(f)

# Set up display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Juggling Animation")

# Define colors
colors = [(255, 25, 10), (0, 0, 0), (100, 10, 0), (0, 255, 0), (0, 0, 255), (0, 100, 155), (100, 10, 255), (56, 70, 55), (150, 90, 255)]
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initial properties
juggler_x = 270
juggler_y = 300
hand_y = juggler_y + 100  # Position of the hands

left_hand_x = juggler_x
right_hand_x = juggler_x + 240

ball_radius = 20
ball_speed = 0.05  # Speed of angle change
gravity = 0.3  # Gravity for parabolic motion

# Font for rendering text
font = pygame.font.Font(None, 32)

# Text input box
input_box = pygame.Rect(100, 50, 140, 32)
learn_button = pygame.Rect(250, 50, 100, 32)
next_button = pygame.Rect(370, 50, 100, 32)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
active = False
text = ''

# Ball properties
balls = []

# List of siteswaps to display
siteswap_sequence = []
current_index = 0
at_end = False  # Flag to track if we are at the end of the sequence

def update_balls(siteswap_string):
    global balls, time
    ss = Siteswap(siteswap_string)
    info = ss.get_info()
    if not info["isValid"]:
        print(f"Invalid siteswap: {info['error']}")
        return

    num_balls = int(info["numBalls"])
    sequence = info["sequence"]

    balls = [
        {
            "color": colors[i % len(colors)],
            "x": left_hand_x if i % 2 == 0 else right_hand_x,
            "y": hand_y,
            "vx": 0, "vy": 0,
            "start_delay": i * 50,  # Add delay for each ball
            "in_left_hand": i % 2 == 0,  # Start in the left hand if index is even, otherwise in right hand
            "movements": [movements[s - 1] for s in sequence if s - 1 < len(movements)],  # Adjust for 0-index
            "current_movement": 0,  # Index of the current movement
            "throw_time": 0,  # Time when the ball should be thrown next
        } for i in range(len(sequence))
    ]
    time = 0  # Reset the global time

def movement_index(movement):
    for i, move in enumerate(movements):
        if move == movement:
            return i

def reset_app_state():
    global balls, siteswap_sequence, current_index, at_end, text
    balls = []
    siteswap_sequence = []
    current_index = 0
    at_end = False
    text = ''

# Main loop
clock = pygame.time.Clock()
time = 0  # Global time to manage throws
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):
                active = not active
            else:
                active = False

            if learn_button.collidepoint(event.pos):
                siteswap_sequence = generate_siteswap_sequence(text)
                current_index = 0
                at_end = False
                if siteswap_sequence:
                    update_balls(siteswap_sequence[current_index])
                text = ''

            if next_button.collidepoint(event.pos):
                if at_end:
                    reset_app_state()
                elif siteswap_sequence:
                    current_index = (current_index + 1) % len(siteswap_sequence)
                    if current_index == len(siteswap_sequence) - 1:
                        at_end = True
                    update_balls(siteswap_sequence[current_index])

            color = color_active if active else color_inactive

        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    siteswap_sequence = generate_siteswap_sequence(text)
                    current_index = 0
                    at_end = False
                    if siteswap_sequence:
                        update_balls(siteswap_sequence[current_index])
                    text = ''
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

    # Clear the screen
    screen.fill(WHITE)

    # Render the current text.
    txt_surface = font.render(text, True, color)
    # Resize the box if the text is too long.
    width = max(200, txt_surface.get_width() + 10)
    input_box.w = width
    # Blit the text.
    screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
    # Blit the input_box rect.
    pygame.draw.rect(screen, color, input_box, 2)

    # Draw the learn button
    pygame.draw.rect(screen, pygame.Color('lightskyblue3'), learn_button)
    learn_button_text = font.render("Learn", True, BLACK)
    screen.blit(learn_button_text, (learn_button.x + 20, learn_button.y + 5))

    # Draw the next/end button
    pygame.draw.rect(screen, pygame.Color('lightskyblue3'), next_button)
    next_button_text = font.render("End" if at_end else "Next", True, BLACK)
    screen.blit(next_button_text, (next_button.x + 20, next_button.y + 5))

    # Update and draw the balls
    for ball in balls:
        elapsed_time = time - ball['start_delay']
        if elapsed_time >= 0:
            current_movement = ball['movements'][ball['current_movement']]
            if elapsed_time >= ball['throw_time']:
                ball['x'] += ball['vx']
                ball['y'] += ball['vy']
                ball['vy'] += gravity

                if ball['y'] >= hand_y:
                    ball['y'] = hand_y
                    ball['vy'] = 0
                    ball['throw_time'] += 190

                    if movement_index(ball['movements'][ball['current_movement']]) % 2 == 0:
                        ball['in_left_hand'] = not ball['in_left_hand']

                    ball['current_movement'] = (ball['current_movement'] + 1) % len(ball['movements'])
                    next_movement = ball['movements'][ball['current_movement']]

                    angle_radians = math.radians(next_movement["throw_angle"])
                    if ball['in_left_hand']:
                        ball['vx'] = next_movement["throw_speed"] * math.cos(angle_radians)
                    else:
                        ball['vx'] = -next_movement["throw_speed"] * math.cos(angle_radians)

                if ball['vy'] == 0 and ball['y'] == hand_y:
                    angle_radians = math.radians(current_movement["throw_angle"])
                    if ball['in_left_hand']:
                        ball['vx'] = -current_movement["throw_speed"] * math.cos(angle_radians)
                    else:
                        ball['vx'] = current_movement["throw_speed"] * math.cos(angle_radians)
                    ball['vy'] = -current_movement["throw_speed"] * math.sin(angle_radians)

        pygame.draw.circle(screen, ball['color'], (int(ball['x']), int(ball['y'])), ball_radius)

    pygame.display.flip()

    clock.tick(50)
    time += ball_speed * 60

pygame.quit()
sys.exit()
