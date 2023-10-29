import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import cos, sin  # Import cos and sin functions

# Initialize Pygame
pygame.init()

# Set up the display
display = (800, 600)
screen = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

# Set up the OpenGL perspective
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(-2.0, -1.0, -5)

# Car properties
car_x, car_y = 0, 0
car_speed = 0.1

# Define the car's vertices


def draw_car():
    # Draw car body (a simple rectangle)
    glColor3f(1, 1, 1)
    glBegin(GL_POLYGON)
    glVertex2f(car_x, car_y)
    glVertex2f(car_x + 1, car_y)
    glVertex2f(car_x + 1, car_y + 0.65)
    glVertex2f(car_x, car_y + 0.65)
    glEnd()

    # Draw car hood (square)
    glColor3f(1, 1, 1)
    glBegin(GL_POLYGON)
    glVertex2f(car_x, car_y)
    glVertex2f(car_x - 0.25, car_y)
    glVertex2f(car_x - 0.25, car_y + 0.4)
    glVertex2f(car_x, car_y + 0.4)
    glEnd()

    # Draw car hood (black square)
    glColor3f(0, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(car_x + 0.85, car_y + 0.4)
    glVertex2f(car_x + 1, car_y + 0.4)
    glVertex2f(car_x + 1, car_y + 0.65)
    glVertex2f(car_x + 0.85, car_y + 0.65)
    glEnd()

    # Draw car hood (triangle)
    glColor3f(1, 1, 1)
    glBegin(GL_POLYGON)
    glVertex2f(car_x, car_y + 0.4)
    glVertex2f(car_x, car_y + 0.65)
    glVertex2f(car_x - 0.1, car_y + 0.4)
    glEnd()

    # Draw wheels (circles)
    glColor3f(0.2, 0.8, 0.8)
    for i in range(2):
        circle_x = car_x + 0.1 + i * 0.6
        circle_y = car_y - 0.035
        glBegin(GL_POLYGON)
        for j in range(360):
            angle = j * 3.14159265358979323846 / 180.0
            glVertex2f(circle_x + 0.16 * cos(angle),
                       circle_y + 0.16 * sin(angle))
        glEnd()


# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        car_x -= car_speed
    if keys[pygame.K_RIGHT]:
        car_x += car_speed
    if keys[pygame.K_UP]:
        car_y += car_speed
    if keys[pygame.K_DOWN]:
        car_y -= car_speed

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glPushMatrix()
    glTranslatef(car_x, car_y, 0)
    draw_car()
    glPopMatrix()

    pygame.display.flip()
    pygame.time.wait(10)
