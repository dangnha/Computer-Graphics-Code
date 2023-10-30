import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Define Cohen-Sutherland region codes
INSIDE = 0  # 0000
LEFT = 1    # 0001
RIGHT = 2   # 0010
BOTTOM = 4  # 0100
TOP = 8     # 1000

# Window coordinates (left, right, bottom, top)
x_min, x_max, y_min, y_max = 50, 100, 50, 100


def compute_region_code(x, y):
    code = INSIDE
    if x < x_min:
        code |= LEFT
    elif x > x_max:
        code |= RIGHT
    if y < y_min:
        code |= BOTTOM
    elif y > y_max:
        code |= TOP
    return code


def cohen_sutherland_clip(x1, y1, x2, y2):
    code1 = compute_region_code(x1, y1)
    code2 = compute_region_code(x2, y2)

    while True:
        if code1 == 0 and code2 == 0:
            return x1, y1, x2, y2
        elif code1 & code2:
            return None  # Line completely outside
        else:
            x, y = 0, 0  # Initialize to inside point
            code_out = code1 if code1 else code2

            if code_out & TOP:
                x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1)
                y = y_max
            elif code_out & BOTTOM:
                x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1)
                y = y_min
            elif code_out & RIGHT:
                y = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1)
                x = x_max
            elif code_out & LEFT:
                y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1)
                x = x_min

            if code_out == code1:
                x1, y1 = x, y
                code1 = compute_region_code(x1, y1)
            else:
                x2, y2 = x, y
                code2 = compute_region_code(x2, y2)


def draw_line(x1, y1, x2, y2):
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()
    glFlush()


def main():
    pygame.init()
    display = (800, 800)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluOrtho2D(0, 400, 0, 400)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        x1, y1, x2, y2 = 100, 50, 350, 350  # Define the line
        draw_line(x1, y1, x2, y2)
        clipped_line = cohen_sutherland_clip(x1, y1, x2, y2)

        if clipped_line:
            x1, y1, x2, y2 = clipped_line
            draw_line(x1, y1, x2, y2)

        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == "__main__":
    main()
