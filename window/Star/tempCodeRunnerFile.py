import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Define vertices for the 5-pointed star
vertices = [
    (0, 0.5),
    (0.15, 0.15),
    (0.5, 0.15),
    (0.2, -0.15),
    (0.35, -0.5),
    (0, -0.25),
    (-0.35, -0.5),
    (-0.2, -0.15),
    (-0.5, 0.15),
    (-0.15, 0.15),
]

# Define edges connecting the vertices
edges = [
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (6, 7),
    (7, 8),
    (8, 9),
    (9, 0),
]

# Define colors
colors = [
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (1, 1, 0),
    (0, 1, 1),
]

# Rotation parameters
angle = 0  # Initial angle
rotate_vertex_index = 0  # Index of the vertex to rotate around
rotating = False


def draw_star():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex2fv(vertices[vertex])
    glEnd()


def main():
    global angle, rotating

    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluOrtho2D(-1, 1, -1, 1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                rotating = True
            if event.type == MOUSEBUTTONUP:
                rotating = False

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glPushMatrix()
        if rotating:
            glTranslatef(vertices[rotate_vertex_index][0],
                         vertices[rotate_vertex_index][1], 0)
            glRotatef(angle, 0, 0, 1)  # Rotate around the chosen vertex
            glTranslatef(-vertices[rotate_vertex_index]
                         [0], -vertices[rotate_vertex_index][1], 0)
            angle += 1  # Increment the rotation angle
        draw_star()
        glPopMatrix()
        pygame.display.flip()


if __name__ == "__main__":
    main()
