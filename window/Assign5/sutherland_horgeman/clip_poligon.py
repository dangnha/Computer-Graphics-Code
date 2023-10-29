import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Define the clipping window (left, right, bottom, top)
x_min, x_max, y_min, y_max = 100, 300, 100, 300

# Define a polygon as a list of vertices (clockwise order)
polygon = [(150, 150), (250, 100), (300, 200), (200, 300)]


def clip_polygon(polygon):
    clipped_polygon = polygon.copy()  # Start with the original polygon

    # Clip against the left edge
    clipped_polygon = clip_against_edge(clipped_polygon, x_min, True)

    # Clip against the right edge
    clipped_polygon = clip_against_edge(clipped_polygon, x_max, False)

    # Clip against the bottom edge
    clipped_polygon = clip_against_edge(
        clipped_polygon, y_min, True, is_horizontal=True)

    # Clip against the top edge
    clipped_polygon = clip_against_edge(
        clipped_polygon, y_max, False, is_horizontal=True)

    return clipped_polygon


def clip_against_edge(polygon, edge, is_inside, is_horizontal=False):
    result = []
    for i in range(len(polygon)):
        current_point = polygon[i]
        next_point = polygon[(i + 1) % len(polygon)]

        if is_horizontal:
            current_coord = current_point[1]
            next_coord = next_point[1]
        else:
            current_coord = current_point[0]
            next_coord = next_point[0]

        if is_inside:
            if current_coord >= edge:
                result.append(current_point)
            if (current_coord < edge) != (next_coord < edge):
                if is_horizontal:
                    x = current_point[0] + (next_point[0] - current_point[0]) * (
                        edge - current_coord) / (next_coord - current_coord)
                    result.append((x, edge))
                else:
                    y = current_point[1] + (next_point[1] - current_point[1]) * (
                        edge - current_coord) / (next_coord - current_coord)
                    result.append((edge, y))
        else:
            if current_coord <= edge:
                result.append(current_point)
            if (current_coord > edge) != (next_coord > edge):
                if is_horizontal:
                    x = current_point[0] + (next_point[0] - current_point[0]) * (
                        edge - current_coord) / (next_coord - current_coord)
                    result.append((x, edge))
                else:
                    y = current_point[1] + (next_point[1] - current_point[1]) * (
                        edge - current_coord) / (next_coord - current_coord)
                    result.append((edge, y))

    return result


def draw_polygon(polygon):
    glBegin(GL_POLYGON)
    glColor3f(1.0, 1.0, 1.0)
    for point in polygon:
        glVertex2f(point[0], point[1])
    glEnd()
    glFlush()


def main():
    pygame.init()
    display = (400, 400)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluOrtho2D(0, 400, 0, 400)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_polygon(polygon)
        clipped_polygon = clip_polygon(polygon)

        if clipped_polygon:
            draw_polygon(clipped_polygon)

        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == "__main__":
    main()
