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
last_car_gen = time.time()
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
    
    def left_turn_j(self, point_x, point_y, dot_x, dot_y):
        if dot_y < point_y and dot_x < point_x:
            dot_y += self.speed
            pygame.draw.circle(screen, red, (int(dot_x), int(dot_y)), 4)
        elif dot_y >= point_y and dot_x < point_x:
            dot_y = point_y + math.cos(self.angle) * self.radius_lt
            dot_x = point_x - math.sin(self.angle) * self.radius_lt
            self.angle -= 0.1
            pygame.draw.circle(screen, red, (int(dot_x), int(dot_y)), 4)
        elif dot_y > point_y and dot_x >= point_x:
            dot_x += self.speed
            pygame.draw.circle(screen, red, (int(dot_x), int(dot_y)), 4)
        return dot_x, dot_y

    def left_turn_k(self, point_x, point_y, dot_x, dot_y):
        if dot_x > point_x and dot_y < point_y:
            dot_x -= self.speed
            pygame.draw.circle(screen, red, (int(dot_x), int(dot_y)), 4)
        elif dot_x <= point_x and dot_y < point_y:
            dot_y = point_y - (math.cos(self.angle) * self.radius_lt)
            dot_x = point_x + (math.sin(self.angle) * self.radius_lt)
            self.angle -= 0.1
            pygame.draw.circle(screen, red, (int(dot_x), int(dot_y)), 4)
        elif dot_x < point_x and dot_y >= point_y:
            dot_y += self.speed
            pygame.draw.circle(screen, red, (int(dot_x), int(dot_y)), 4)
        return dot_x, dot_y

    def left_turn_l(self, point_x, point_y, dot_x, dot_y):
        if dot_y > point_y and dot_x > point_x:
            dot_y -= self.speed
            pygame.draw.circle(screen, red, (int(dot_x), int(dot_y)), 4)
        elif dot_y <= point_y and dot_x > point_x:
            dot_y = point_y - math.cos(self.angle) * self.radius_lt
            dot_x = point_x + math.sin(self.angle) * self.radius_lt
            self.angle -= 0.1
            pygame.draw.circle(screen, red, (int(dot_x), int(dot_y)), 4)
        elif dot_y < point_y and dot_x <= point_x:
            dot_x -= self.speed
            pygame.draw.circle(screen, red, (int(dot_x), int(dot_y)), 4)
        return dot_x, dot_y
left_turns = LeftTurn()


dot_ix, dot_iy = 0, 317.5
dot_jx, dot_jy = 682.5, 0
dot_kx, dot_ky = 1200, 482.5
dot_lx, dot_ly = 517.5, 800

dot_list = []






running = True
frame_count = 0
running = True
clock = pygame.time.Clock()

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Clear the screen
    screen.fill(asphalt_grey)
        #defining corner rectangles
    rect_width, rect_height, rect_margin = 500,300, 0
            # Draw rectangles on each corner of the window
        # Top-left corner
    pygame.draw.rect(screen, green, (rect_margin, rect_margin, rect_width + 1, rect_height + 1))
        # Top-right corner
    pygame.draw.rect(screen, green, (screen_width - rect_margin - rect_width + 1, rect_margin, rect_width, rect_height + 1))
        # Bottom-left corner
    pygame.draw.rect(screen, green, (rect_margin + 1, screen_height - rect_margin - rect_height + 1, rect_width, rect_height))
        # Bottom-right corner
    pygame.draw.rect(screen, green, (screen_width - rect_margin - rect_width + 1, screen_height - rect_margin - rect_height + 1, rect_width, rect_height))
        #dotted line properties
    dashed_line_width = 2
    dashed_line_length_h = 500
    dashed_line_length_v = 300
    dash_gap = 40
    dash_length = 20
        #lane specification
    lane_width = 33        
        # Bottom portion of vertical plain lines
    p = screen_height - dashed_line_length_v
    horiz_center = screen_width // 2
    pygame.draw.line(screen, white, ((horiz_center), p), ((screen_width // 2), (p + dashed_line_length_v)), dashed_line_width)
    pygame.draw.line(screen, black, ((horiz_center - (3*lane_width)), p), ((horiz_center - (3*lane_width)), (p + dashed_line_length_v)),    dashed_line_width)    
    pygame.draw.line(screen, black, ((horiz_center + ((3*lane_width) )), p), ((horiz_center + (3*lane_width)), (p + dashed_line_length_v)),    dashed_line_width)    
    pygame.draw.line(screen, white, ((horiz_center - ((3*lane_width + 2) )), (p - 199)), ((horiz_center - (3*lane_width + 2)), (p - 100)),    dashed_line_width + 3)    
    pygame.draw.line(screen, white, ((horiz_center + ((3*lane_width + 2) )), (p - 100)), ((horiz_center + (3*lane_width + 2)), (p - 1)),    dashed_line_width + 3)    
        # Bottom portion of vertical dashed lines
    for y in range(p, screen_height, dash_gap):
        pygame.draw.line(screen, white, ((horiz_center  - (lane_width)), y), ((horiz_center - (lane_width)), y + dash_length),   dashed_line_width)
        pygame.draw.line(screen, white, ((horiz_center  - (2*lane_width)), y), ((horiz_center - (2*lane_width)), y + dash_length),   dashed_line_width)
        pygame.draw.line(screen, yellow, ((horiz_center  - (3*lane_width)), y -1), ((horiz_center - (3*lane_width)), y + dash_length),  dashed_line_width)
        pygame.draw.line(screen, white, ((horiz_center  + (lane_width)), y), ((horiz_center + (lane_width)), y + dash_length),   dashed_line_width)
        pygame.draw.line(screen, white, ((horiz_center  + (2*lane_width)), y), ((horiz_center + (2*lane_width)), y + dash_length),   dashed_line_width)
        pygame.draw.line(screen, yellow, ((horiz_center  + ((3*lane_width) )), y -1), ((horiz_center + (3*lane_width)), y + dash_length),  dashed_line_width)
        # Top portion of vertical plain lines
    r = dashed_line_length_v
    horiz_center = screen_width // 2
    pygame.draw.line(screen, white, ((horiz_center), 0), ((screen_width // 2), (0 + dashed_line_length_v)), dashed_line_width)
    pygame.draw.line(screen, black, ((horiz_center - (3*lane_width)), 0), ((horiz_center - (3*lane_width)), (0 + dashed_line_length_v)),    dashed_line_width)    
    pygame.draw.line(screen, black, ((horiz_center + ((3*lane_width) )), 0), ((horiz_center + (3*lane_width)), (0 + dashed_line_length_v)),    dashed_line_width)    
        # Top portion of vertical dashed lines
    for y in range(0, r, dash_gap):
        pygame.draw.line(screen, white, ((horiz_center  - (lane_width)), y), ((horiz_center - (lane_width)), y + dash_length),   dashed_line_width)
        pygame.draw.line(screen, white, ((horiz_center  - (2*lane_width)), y), ((horiz_center - (2*lane_width)), y + dash_length),   dashed_line_width)
        pygame.draw.line(screen, yellow, ((horiz_center  - (3*lane_width)), y), ((horiz_center - (3*lane_width)), y + dash_length +2),  dashed_line_width)
        pygame.draw.line(screen, white, ((horiz_center  + (lane_width)), y), ((horiz_center + (lane_width)), y + dash_length),   dashed_line_width)
        pygame.draw.line(screen, white, ((horiz_center  + (2*lane_width)), y), ((horiz_center + (2*lane_width)), y + dash_length),   dashed_line_width)
        pygame.draw.line(screen, yellow, ((horiz_center  + ((3*lane_width) )), y), ((horiz_center + (3*lane_width)), y + dash_length +2),  dashed_line_width)
        # Right portion of horizontal plain lines
    q = screen_width - dashed_line_length_h
    vert_center = screen_height // 2
    pygame.draw.line(screen, white, (q, (vert_center)), ((q + dashed_line_length_h), (vert_center)),    dashed_line_width)
    pygame.draw.line(screen, black, (q, (vert_center - (3*lane_width))), ((q + dashed_line_length_h), (vert_center - (3*lane_width))),  dashed_line_width)
    pygame.draw.line(screen, black, (q, (vert_center + (3*lane_width))), ((q + dashed_line_length_h), (vert_center + (3*lane_width))),  dashed_line_width)
    pygame.draw.line(screen, white, ((q - 100), (vert_center - (3*lane_width + 1))), ((q - 2), (vert_center - (3*lane_width + 1))),  dashed_line_width +3)
    pygame.draw.line(screen, white, ((q - 198), (vert_center + (3*lane_width + 2))), ((q - 100), (vert_center + (3*lane_width + 2))),  dashed_line_width +3)
        # Right portion of horizontal dashed lines
    for x in range(q, screen_width, dash_gap):
        pygame.draw.line(screen, white, (x, (vert_center - (lane_width))), (x + dash_length, (vert_center - (lane_width))),    dashed_line_width)
        pygame.draw.line(screen, white, (x, (vert_center - (2*lane_width))), (x + dash_length, (vert_center - (2*lane_width))),    dashed_line_width)
        pygame.draw.line(screen, yellow, (x, (vert_center - (3*lane_width))), (x + dash_length, (vert_center - (3*lane_width))),   dashed_line_width)
        pygame.draw.line(screen, white, (x, (vert_center + (lane_width))), (x + dash_length, (vert_center + (lane_width))),    dashed_line_width)
        pygame.draw.line(screen, white, (x, (vert_center + (2*lane_width))), (x + dash_length, (vert_center + (2*lane_width))),    dashed_line_width)
        pygame.draw.line(screen, yellow, (x, (vert_center + (3*lane_width))), (x + dash_length, (vert_center + (3*lane_width))),   dashed_line_width)
        # Left portion of horizontal plain lines
    s = dashed_line_length_h
    vert_center = screen_height // 2
    pygame.draw.line(screen, white, (0, (vert_center)), ((0 + dashed_line_length_h), (vert_center)),    dashed_line_width)
    pygame.draw.line(screen, black, (0, (vert_center + (3*lane_width))), ((0 + dashed_line_length_h), (vert_center + (3*lane_width))),  dashed_line_width)
    pygame.draw.line(screen, black, (0, (vert_center - (3*lane_width))), ((0 + dashed_line_length_h), (vert_center - (3*lane_width))),  dashed_line_width)
        # Left portion of horizontal dashed lines
    for x in range(0, s, dash_gap):
        pygame.draw.line(screen, white, (x, (vert_center - (lane_width))), (x + dash_length, (vert_center - (lane_width))),    dashed_line_width)
        pygame.draw.line(screen, white, (x, (vert_center - (2*lane_width))), (x + dash_length, (vert_center - (2*lane_width))),    dashed_line_width)
        pygame.draw.line(screen, yellow, (x, (vert_center - (3*lane_width))), (x + dash_length, (vert_center - (3*lane_width))),   dashed_line_width)
        pygame.draw.line(screen, white, (x, (vert_center + (lane_width))), (x + dash_length, (vert_center + (lane_width))),    dashed_line_width)
        pygame.draw.line(screen, white, (x, (vert_center + (2*lane_width))), (x + dash_length, (vert_center + (2*lane_width))),    dashed_line_width)
        pygame.draw.line(screen, yellow, (x, (vert_center + (3*lane_width))), (x + dash_length, (vert_center + (3*lane_width))),   dashed_line_width)



    # dot_ix, dot_iy = left_turns.left_turn_i(501, 301, dot_ix, dot_iy)
    dot_jx, dot_jy = left_turns.left_turn_j(699, 301, dot_jx, dot_jy)
    dot_kx, dot_ky = left_turns.left_turn_k(699, 499, dot_kx, dot_ky)
    dot_lx, dot_ly = left_turns.left_turn_l(501, 500, dot_lx, dot_ly)


        # Generate new dot and add to dot_list
    if random.random() < 0.02:  # Adjust this probability as needed
        dot_list.append((501, 301, dot_ix, dot_iy))  # Add dot coordinates to the list

    # Update and draw dots in dot_list
    for dot in dot_list:
        dot_ix, dot_iy = left_turns.left_turn_i(*dot)

   
 





















    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)
    
    # Increment frame count
    frame_count += 1

# Quit Pygame
pygame.quit()