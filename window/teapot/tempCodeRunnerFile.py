from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_teapot():
    glColor3f(1.0, 1.0, 0.0)  # Yellow color
    glutSolidTeapot(1.0)  # Radius of the teapot


def draw_cube():
    glColor3f(0.0, 0.0, 1.0)  # Blue color
    glutSolidCube(0.5)  # Size of the cube


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Position the camera
    gluLookAt(3, 3, 3, 0, 0, 0, 0, 1, 0)

    # Draw the teapot and the cube
    draw_teapot()
    draw_cube()

    glutSwapBuffers()


def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (width / height), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)


def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow("Teapot and Cube")

    glEnable(GL_DEPTH_TEST)

    glutDisplayFunc(display)
    glutReshapeFunc(reshape)

    glutMainLoop()


if __name__ == "__main__":
    main()
