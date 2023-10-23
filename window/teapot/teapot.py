from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

# Global variable for teapot height
teapot_height = 1.0

# Global variable for teapot rotation angle
teapot_rotation_angle = 0

# Global variable for teapot position
teapot_position_x = 0


def init():
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, [1, 1, 1, 0])
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)


def draw_teapot():
    glPushMatrix()
    glTranslatef(teapot_position_x, 0, 0)
    glRotatef(teapot_rotation_angle, 0, 0, 1)
    glutSolidTeapot(teapot_height)
    glPopMatrix()


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(3, 3, 3, 0, 0, 0, 0, 1, 0)
    draw_teapot()
    glutSwapBuffers()


def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (width / height), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)


def keyboard(key, x, y):
    global teapot_height, teapot_rotation_angle, teapot_position_x

    if key == b'T':
        teapot_height *= 2
    elif key == b't':
        teapot_height /= 2
    elif key == b'q':
        teapot_rotation_angle += 30
    elif key == b'Q':
        teapot_rotation_angle += 90
    elif key == b'l' or key == b'L':
        teapot_position_x -= 1
    elif key == b'r' or key == b'R':
        teapot_position_x += 1

    glutPostRedisplay()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow("Teapot")
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)  # Register the keyboard callback
    glutMainLoop()


if __name__ == "__main__":
    main()
