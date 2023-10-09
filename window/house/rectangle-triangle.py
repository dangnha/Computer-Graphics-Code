import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def draw_triangle():
    glBegin(GL_TRIANGLES)
    glVertex3f(0.25, 0.75, 0)
    glVertex3f(0.75, 0.75, 0)
    glVertex3f(0.5, 1, 0)
    glEnd()


def draw_rectangle(vertices):
    glBegin(GL_QUADS)
    for vertex in vertices:
        glVertex3f(*vertex)
    glEnd()

# def draw_rectangle():
#     glBegin(GL_QUADS)
#     glVertex3f(0.25, 0.25, 0)
#     glVertex3f(0.75, 0.25, 0)
#     glVertex3f(0.75, 0.75, 0)
#     glVertex3f(0.25, 0.75, 0)
#     glEnd()


def main():
    pygame.init()
    display = (1200, 800)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    rectangles = [
        [(0.25, 0.25, 0), (0.75, 0.25, 0), (0.75, 0.75, 0), (0.25, 0.75, 0)],
        [(0.25, 0.75, 0), (0.75, 0.75, 0), (0.75, 1.25, 0), (0.25, 1.25, 0)],
        [(0.75, 0.25, 0), (1.25, 0.25, 0), (1.25, 0.75, 0), (0.75, 0.75, 0)],
        [(0.75, 0.75, 0), (1.25, 0.75, 0), (1.25, 1.25, 0), (0.75, 1.25, 0)],
    ]

    colors = [
        (1, 0, 0),
        (1, 1, 1),
        (1, 1, 0),
        (0, 0, 0),
    ]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glColor3f(1, 0, 0)
        draw_triangle()

        for i, rect in enumerate(rectangles):
            glColor3f(*colors[i])
            draw_rectangle(rect)

        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == "__main__":
    main()
