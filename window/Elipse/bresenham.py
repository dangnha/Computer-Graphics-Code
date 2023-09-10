import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Function to draw a quarter of an ellipse using Bresenham's algorithm


def draw_quarter_ellipse(a, b):
    glBegin(GL_POINTS)
    x, y = 0, b
    a_sqr, b_sqr = a * a, b * b
    two_a_sqr, two_b_sqr = 2 * a_sqr, 2 * b_sqr
    x_end = int(a_sqr / (a_sqr + b_sqr)**0.5)

    # Region 1
    P = b_sqr - a_sqr * b + 0.25 * a_sqr
    while x <= x_end:
        glVertex2f(x, y)  # Plot the pixel in the first quadrant

        x += 1

        # Mid-point inside or on the perimeter
        if P < 0:
            P += two_b_sqr * x + b_sqr
        else:
            y -= 1
            P += two_b_sqr * x - two_a_sqr * y + b_sqr

    # Region 2
    P = b_sqr * (x + 0.5)**2 + a_sqr * (y - 1)**2 - a_sqr * b_sqr
    while y >= 0:
        glVertex2f(x, y)  # Plot the pixel in the first quadrant

        y -= 1

        # Mid-point inside or on the perimeter
        if P > 0:
            P += -two_a_sqr * y + a_sqr
        else:
            x += 1
            P += two_b_sqr * x - two_a_sqr * y + a_sqr

    glEnd()


def draw_ellipse(a, b):
    glPushMatrix()
    draw_quarter_ellipse(a, b)
    glScalef(1, -1, 1)  # Flip the y-axis
    draw_quarter_ellipse(a, b)
    glScalef(-1, 1, 1)  # Flip the x-axis
    draw_quarter_ellipse(a, b)
    glScalef(1, -1, 1)  # Flip the y-axis back
    draw_quarter_ellipse(a, b)
    glPopMatrix()


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluOrtho2D(-400, 400, -300, 300)

    glClearColor(0, 0, 0, 1)
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(1, 1, 1)

    a, b = 200, 100  # Set the semi-major and semi-minor axes

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT)
        draw_ellipse(a, b)
        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == "__main__":
    main()
