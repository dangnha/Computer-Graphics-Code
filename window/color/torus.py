from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_torus():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    gluLookAt(0.1, 0.1, 0.1, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    # Draw X, Y, and Z axes
    glBegin(GL_LINES)

    # X-axis (red)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(1.0, 0.0, 0.0)

    # Y-axis (green)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 1.0, 0.0)

    # Z-axis (blue)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 1.0)

    glEnd()

    # Draw the wireframe torus
    glColor3f(1.0, 1.0, 1.0)
    glutWireTorus(0.1, 0.6, 10, 30)

    glutSwapBuffers()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow("Wireframe Torus with Axes")
    glutDisplayFunc(draw_torus)
    glEnable(GL_DEPTH_TEST)

    glutMainLoop()


if __name__ == "__main__":
    main()
