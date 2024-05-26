import pygame
import sys
import math
import json
# Initialize Pygame
pygame.init()

movements = json.load(open("./movements.json"))
# Set up display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Juggling Animation")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Initial properties
juggler_x = 270
juggler_y = 300
hand_y = juggler_y + 100  # Position of the hands

ball_radius = 20
ball_speed = 0.05  # Speed of angle change
gravity = 0.3  # Gravity for parabolic motion
throw_speed = 9  # Initial vertical speed of the throw
throw_angle = 60  # Angle of the throw in degrees

# Ball properties

balls = [
    {"color": RED, "x": juggler_x, "y": hand_y, "vx": 0, "vy": 0, "throw_time": 0, "throw_angle": move["throw_angle"], "throw_speed": move["throw_speed"]} for move in movements
]

# Input fields
# input_box_radius = pygame.Rect(200, 50, 140, 32)
# input_box_speed = pygame.Rect(200, 100, 140, 32)
# input_box_throw = pygame.Rect(200, 150, 140, 32)
# input_box_angle = pygame.Rect(200, 200, 140, 32)
# input_boxes = [input_box_radius, input_box_speed, input_box_throw, input_box_angle]

input_labels = ["Radius:", "Speed:", "Throw Speed:", "Throw Angle:"]
inputs = ["20", "0.05", "10", "45"]
active_box = None

# Button
# button_rect = pygame.Rect(200, 250, 140, 32)
# button_text = "Update"

font = pygame.font.Font(None, 32)

# Main loop
clock = pygame.time.Clock()
time = 0  # Global time to manage throws
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     if button_rect.collidepoint(event.pos):
        #         # Update the parameters when button is pressed
        #         try:
        #             ball_radius = int(inputs[0])
        #             ball_speed = float(inputs[1])
        #             throw_speed = int(inputs[2])
        #             throw_angle = float(inputs[3])
        #         except ValueError:
        #             pass  # Ignore invalid input

        #     # for i, box in enumerate(input_boxes):
        #     #     if box.collidepoint(event.pos):
        #     #         active_box = i
        #     #         break
        #     else:
        #         active_box = None

        if event.type == pygame.KEYDOWN:
            if active_box is not None:
                if event.key == pygame.K_RETURN:
                    active_box = None
                elif event.key == pygame.K_BACKSPACE:
                    inputs[active_box] = inputs[active_box][:-1]
                else:
                    inputs[active_box] += event.unicode

    # Clear the screen
    screen.fill(WHITE)

    # Draw input boxes and labels
    # for i, box in enumerate(input_boxes):
    #     label_surface = font.render(input_labels[i], True, BLACK)
    #     screen.blit(label_surface, (box.x - 150, box.y + 5))
    #     txt_surface = font.render(inputs[i], True, BLACK)
    #     width = max(200, txt_surface.get_width() + 10)
    #     box.w = width
    #     screen.blit(txt_surface, (box.x + 5, box.y + 5))
    #     pygame.draw.rect(screen, BLACK, box, 2)

    # Draw button
    # pygame.draw.rect(screen, BLACK, button_rect, 2)
    # button_surf = font.render(button_text, True, BLACK)
    # screen.blit(button_surf, (button_rect.x + 5, button_rect.y + 5))

    # Update and draw the balls
    for ball in balls:
        # Check if it's time to throw the ball
        if time >= ball['throw_time']:
            # Update ball position
            ball['x'] += ball['vx']
            ball['y'] += ball['vy']
            ball['vy'] += gravity

            # Check if the ball is caught
            if ball['y'] >= hand_y:
                ball['y'] = hand_y
                ball['vx'] = 0
                ball['vy'] = 0
                ball['throw_time'] += 100  # Schedule next throw

            # If the ball is in the hands, prepare to throw
            if ball['vy'] == 0 and ball['y'] == hand_y:
                angle_radians = math.radians(ball["throw_angle"])
                ball['vx'] = ball["throw_speed"] * math.cos(angle_radians) * (-1 if ball['x'] > juggler_x else 1)
                ball['vy'] = -ball["throw_speed"] * math.sin(angle_radians)

        pygame.draw.circle(screen, ball['color'], (int(ball['x']), int(ball['y'])), ball_radius)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
    time += ball_speed * 60  # Update global time

pygame.quit()
sys.exit()
