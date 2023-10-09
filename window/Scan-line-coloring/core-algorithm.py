import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Define vertices of a polygon
# Triangle
vertices = [(100, 100), (200, 200), (300, 100)]
# Rectangle
# vertices = [(100, 100), (100, 200), (300, 200), (300, 100)]


def draw_polygon(vertices):
    glBegin(GL_POLYGON)
    for vertex in vertices:
        glVertex2f(*vertex)
    glEnd()


def draw_scan_line(vertices):
    min_y = min(vertices, key=lambda v: v[1])[1]
    max_y = max(vertices, key=lambda v: v[1])[1]

    for y in range(min_y, max_y + 1):
        intersections = []
        for i in range(len(vertices)):
            x1, y1 = vertices[i]
            x2, y2 = vertices[(i + 1) % len(vertices)]

            if y1 < y2:
                if y1 <= y <= y2:
                    x_intersection = x1 + (x2 - x1) * (y - y1) / (y2 - y1)
                    intersections.append(x_intersection)
            elif y1 > y2:
                if y2 <= y <= y1:
                    x_intersection = x2 + (x1 - x2) * (y - y2) / (y1 - y2)
                    intersections.append(x_intersection)

        intersections.sort()
        for i in range(0, len(intersections), 2):
            x1 = int(intersections[i])
            x2 = int(intersections[i + 1])
            glBegin(GL_LINES)
            glVertex2f(x1, y)
            glVertex2f(x2, y)
            glEnd()
            pygame.display.flip()


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluOrtho2D(0, 800, 0, 600)

    glClearColor(0.0, 0.0, 0.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 1.0, 0.0)

    draw_scan_line(vertices)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


if __name__ == "__main__":
    main()
