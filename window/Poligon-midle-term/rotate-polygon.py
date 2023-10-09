import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

vertices = [
    (0.25, 0.25),
    (0.75, 0.25),
    (0.75, 0.75),
    (0.25, 0.75)
]


def draw_polygon():
    glBegin(GL_POLYGON)
    for vertex in vertices:
        glVertex2fv(vertex)
    glEnd()


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluOrtho2D(0, 1, 0, 1)
    # Apply a 45-degree rotation
    glTranslatef(0.5, 0.5, 0.0)
    glRotatef(45, 0, 0, 1)
    glTranslatef(-0.5, -0.5, 0.0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_polygon()
        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == "__main__":
    main()
