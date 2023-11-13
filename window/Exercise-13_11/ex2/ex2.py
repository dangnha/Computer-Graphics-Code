from OpenGL.GL import *
from OpenGL.GLUT import *


def draw_rectangle(x, y, width, height, color):
    glColor3fv(color)
    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x + width, y)
    glVertex2f(x + width, y + height)
    glVertex2f(x, y + height)
    glEnd()


def draw_triangle(x1, y1, x2, y2, x3, y3, color):
    glColor3fv(color)
    glBegin(GL_TRIANGLES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glVertex2f(x3, y3)
    glEnd()


def draw_house():
    # Draw background (orange)
    draw_rectangle(0, 0, 800, 600, [1.0, 0.647, 0.0])  # RGB for orange

    # Draw house body (gray)
    draw_rectangle(200, 200, 400, 200, [0.5, 0.49, 0.5])  # RGB for gray

    # Draw roof (pink)
    draw_triangle(150, 200, 650, 200, 450, 50, [
                  1.0, 0.16, 1.0])  # RGB for pink, 700 is center

    # Draw door (brown)
    draw_rectangle(320, 250, 90, 150, [0.6, 0.4, 0.2])  # RGB for brown
    draw_rectangle(320, 230, 90, 10, [0.6, 0.4, 0.2])  # RGB for brown

    # Draw window (red)
    draw_rectangle(450, 270, 100, 100, [1.0, 0.0, 0.0])  # RGB for red
    draw_rectangle(450, 230, 100, 20, [1.0, 0.0, 0.0])  # RGB for red


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    draw_house()
    glutSwapBuffers()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
    glutCreateWindow(b"OpenGL House")
    glutReshapeWindow(800, 600)
    glOrtho(0, 800, 600, 0, -1, 1)
    glutDisplayFunc(display)
    glutMainLoop()


if __name__ == "__main__":
    main()
