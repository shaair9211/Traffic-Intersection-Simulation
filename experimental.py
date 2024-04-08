import pygame
import sys
import random
import time
import math

pygame.init()

screen_width, screen_height = 1200, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Traffic Intersection Simulation")

white, black, red, asphalt_grey, green, yellow = (255, 255, 255), (0, 0, 0), (255, 0, 0), (99, 102, 102), (1, 50, 32), (255, 255, 0)

clock = pygame.time.Clock()
running = True

class LeftTurn:
    def __init__(self):
        self.angle = 1.57
        self.radius_lt = 15.5
        self.speed = 3

    def left_turn_i(self, point_x, point_y, dot_x, dot_y):
        if dot_x < point_x and dot_y > point_y:
            dot_x += self.speed
            pygame.draw.circle(screen, red, (int(dot_x), int(dot_y)), 4)
        elif dot_x >= point_x and dot_y > point_y:
            dot_y = point_y + math.cos(self.angle) * self.radius_lt
            dot_x = point_x - math.sin(self.angle) * self.radius_lt
            self.angle -= 0.1
            pygame.draw.circle(screen, red, (int(dot_x), int(dot_y)), 4)
        elif dot_x > point_x and dot_y <= point_y:
            dot_y -= self.speed
            pygame.draw.circle(screen, red, (int(dot_x), int(dot_y)), 4)
        return dot_x, dot_y

left_turn = LeftTurn()
dot_ix, dot_iy = 0, 317.5
dot_list = []  # List to hold dot coordinates

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Generate new dot and add to dot_list
    if random.random() < 0.02:  # Adjust this probability as needed
        dot_list.append((501, 301, 0, 317.5))  # Add dot coordinates to the list

    # Update and draw dots in dot_list
    for dot in dot_list:
        dot_ix, dot_iy = left_turn.left_turn_i(*dot)
    
    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)
    
# Quit Pygame
pygame.quit()
