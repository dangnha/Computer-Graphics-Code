from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *

# Define the vertices and colors for the triangle
vertices = [
    (0.0, 1.0, 0.0),
    (-1.0, -1.0, 0.0),
    (1.0, -1.0, 0.0)
]

colors = [
    (1.0, 0.0, 0.0),
    (0.0, 1.0, 0.0),
    (0.0, 0.0, 1.0)
]


def draw_triangle():
    glBegin(GL_TRIANGLES)
    for i in range(3):
        glColor3fv(colors[i])
        glVertex3fv(vertices[i])
    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_triangle()
    glFlush()


def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (width / height), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -5)


def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(800, 600)
    glutCreateWindow("Gradient Triangle with PyOpenGL")
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMainLoop()


if __name__ == "__main__":
    main()
