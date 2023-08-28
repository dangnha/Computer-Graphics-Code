
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def mid_point(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    d = dy - dx/2
    y = y1

    for x in range(x1, x2 + 1):
        glVertex2f(x, y)
        if d > 0:
            y += 1
            d = d + dy - dx
        d += dy


def draw_line():
    glBegin(GL_POINTS)
    glColor3f(1.0, 0.0, 0.0)
    mid_point(100, 50, 150, 90)
    glEnd()


def main():
    pygame.init()
    display = (600, 400)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluOrtho2D(0, 800, 0, 600)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT)
        # Call draw line function
        draw_line()

        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == "__main__":
    main()
