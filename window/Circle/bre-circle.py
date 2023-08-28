import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_circle(xc, yc, x, y):
    glBegin(GL_POINTS)
    glVertex2f(xc + x, yc + y)
    glVertex2f(xc - x, yc + y)
    glVertex2f(xc + x, yc - y)
    glVertex2f(xc - x, yc - y)
    glVertex2f(xc + y, yc + x)
    glVertex2f(xc - y, yc + x)
    glVertex2f(xc + y, yc - x)
    glVertex2f(xc - y, yc - x)
    glEnd()


def bresenham_circle(xc, yc, r):
    x = 0
    y = r
    d = 3 - 2 * r
    while x <= y:
        draw_circle(xc, yc, x, y)
        x += 1
        if d < 0:
            d += 4 * x + 6
        else:
            d += 4 * (x - y) + 10
            y -= 1
        draw_circle(xc, yc, x, y)


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluOrtho2D(0, 800, 0, 600)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT)

        glColor3f(0, 1, 1)

        # Call draw circle function
        bresenham_circle(400, 300, 100)

        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == "__main__":
    main()
