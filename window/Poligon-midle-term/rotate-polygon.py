import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

# Define the vertices of the polygon
vertices = [
    (0.25, 0.25),
    (0.75, 0.25),
    (0.75, 0.75),
    (0.25, 0.75)
]

# Function to rotate the polygon at a given angle


def rotate_polygon(angle):
    radians = math.radians(angle)
    rotated_vertices = [
        (
            v[0] * math.cos(radians) - v[1] * math.sin(radians),
            v[0] * math.sin(radians) + v[1] * math.cos(radians)
        )
        for v in vertices
    ]
    return rotated_vertices


def draw_polygon(rotated_vertices):
    glBegin(GL_POLYGON)
    for vertex in rotated_vertices:
        glVertex2fv(vertex)
    glEnd()


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluOrtho2D(0, 1, 0, 1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Rotate the polygon at 45 degrees
        rotated_vertices = rotate_polygon(45)

        # Draw the rotated polygon
        draw_polygon(rotated_vertices)

        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == "__main__":
    main()
