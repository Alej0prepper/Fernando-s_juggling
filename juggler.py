import pygame
import sys
import math
import json

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

# Ball properties
balls = [
    {
        "color": colors[i],
        "x": left_hand_x if i % 2 == 0 else right_hand_x,
        "y": hand_y,
        "vx": 0, "vy": 0, "throw_time": 0,
        "throw_angle": movements[2]["throw_angle"],
        "throw_speed": movements[2]["throw_speed"],
        "start_delay": i * 80,  # Add delay for each ball
        "in_left_hand": i % 2 == 0  # Start in the left hand if index is even, otherwise in right hand
    } for i in range(3)
]

# Main loop
clock = pygame.time.Clock()
time = 0  # Global time to manage throws
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Update and draw the balls
    for ball in balls:
        # Check if it's time to throw the ball
        elapsed_time = time - ball['start_delay']
        if elapsed_time >= 0:
            if elapsed_time >= ball['throw_time']:
                # Update ball position
                ball['x'] += ball['vx']
                ball['y'] += ball['vy']
                ball['vy'] += gravity

                # Check if the ball is caught
                if ball['y'] >= hand_y:
                    ball['y'] = hand_y
                    ball['vy'] = 0
                    ball['throw_time'] += 200  # Schedule next throw

                    # Swap hands for the next throw
                    ball['in_left_hand'] = not ball['in_left_hand']

                    # Update vx based on the new hand position
                    angle_radians = math.radians(ball["throw_angle"])
                    if ball['in_left_hand']:
                        ball['vx'] = ball["throw_speed"] * math.cos(angle_radians)
                    else:
                        ball['vx'] = -ball["throw_speed"] * math.cos(angle_radians)

                # If the ball is in the hands, prepare to throw
                if ball['vy'] == 0 and ball['y'] == hand_y:
                    angle_radians = math.radians(ball["throw_angle"])
                    if ball['in_left_hand']:
                        ball['vx'] = -ball["throw_speed"] * math.cos(angle_radians)
                    else:
                        ball['vx'] = ball["throw_speed"] * math.cos(angle_radians)
                    ball['vy'] = -ball["throw_speed"] * math.sin(angle_radians)

        pygame.draw.circle(screen, ball['color'], (int(ball['x']), int(ball['y'])), ball_radius)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
    time += ball_speed * 60  # Update global time

pygame.quit()
sys.exit()
