from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys


# Global variable for teapot rotation angle
global_rotation_angle = 0

# Global variable for teapot position
pos_rotate = 0


def init():
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, [1, 1, 1, 0])
    glShadeModel(GL_SMOOTH)
    glMaterialfv(GL_FRONT, GL_SPECULAR, [1, 1, 1, 1])
    glMaterialfv(GL_FRONT, GL_SHININESS, [30])
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)


def draw_small_global1():
    glPushMatrix()

    glTranslatef(0, -2, pos_rotate)
    glRotatef(global_rotation_angle, 1, 0, 0)
    glTranslatef(0, 2, -pos_rotate)

    glutSolidSphere(0.5, 50, 50)
    glPopMatrix()


def draw_small_global2():
    glPushMatrix()

    glTranslatef(-2, 0, pos_rotate)
    glRotatef(global_rotation_angle, 0, 1, 0)
    glTranslatef(2, 0, -pos_rotate)

    glutSolidSphere(0.5, 50, 50)
    glPopMatrix()


def draw_big_global():
    glPushMatrix()
    glutSolidSphere(1.0, 50, 50)
    glPopMatrix()


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(0, 0, 6, 0, 0, 0, 0, 1, 0)

    # Set material and lighting properties for the first small sphere (red)
    glPushMatrix()
    glTranslatef(0, 2, 0)

    glMaterialfv(GL_FRONT, GL_AMBIENT, [1.0, 0.0, 0.0, 1.0])
    glMaterialfv(GL_FRONT, GL_DIFFUSE, [1.0, 0.0, 0.0, 1.0])
    glMaterialfv(GL_FRONT, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])
    glMaterialf(GL_FRONT, GL_SHININESS, 50)

    glEnable(GL_LIGHT1)
    glLightfv(GL_LIGHT1, GL_POSITION, [0, 1, 0, 0])
    glLightfv(GL_LIGHT1, GL_DIFFUSE, [0.5, 0.0, 0.0, 1.0])
    glLightfv(GL_LIGHT1, GL_AMBIENT, [0.5, 0.0, 0.0, 1.0])

    draw_small_global1()

    glPopMatrix()

    # Set material and lighting properties for the large sphere (blue)
    glPushMatrix()
    glTranslatef(0, 0, 0)

    glMaterialfv(GL_FRONT, GL_AMBIENT, [0.0, 0.0, 0.5, 1.0])
    glMaterialfv(GL_FRONT, GL_DIFFUSE, [0.0, 0.0, 0.5, 1.0])
    glMaterialfv(GL_FRONT, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])
    glMaterialf(GL_FRONT, GL_SHININESS, 50)

    glEnable(GL_LIGHT1)
    glLightfv(GL_LIGHT1, GL_POSITION, [0, 1, 0, 0])
    glLightfv(GL_LIGHT1, GL_DIFFUSE, [0.0, 0.0, 1.0, 1.0])
    glLightfv(GL_LIGHT1, GL_AMBIENT, [0.0, 0.0, 1.0, 1.0])

    draw_big_global()
    glPopMatrix()

    # Set material and lighting properties for the second small sphere (yellow)
    glPushMatrix()
    glTranslatef(2, 0, 0)

    glMaterialfv(GL_FRONT, GL_AMBIENT, [0.5, 0.5, 0.0, 1.0])
    glMaterialfv(GL_FRONT, GL_DIFFUSE, [0.5, 0.5, 0.0, 1.0])
    glMaterialfv(GL_FRONT, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])
    glMaterialf(GL_FRONT, GL_SHININESS, 50)

    glEnable(GL_LIGHT1)
    glLightfv(GL_LIGHT1, GL_POSITION, [0, 1, 0, 0])
    glLightfv(GL_LIGHT1, GL_DIFFUSE, [0.5, 0.5, 0.0, 1.0])
    glLightfv(GL_LIGHT1, GL_AMBIENT, [0.5, 0.5, 0.0, 1.0])

    draw_small_global2()

    glPopMatrix()

    glutSwapBuffers()


def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glLoadIdentity()
    gluPerspective(65, (width / height), 0.1, 20.0)
    glMatrixMode(GL_MODELVIEW)


# glutIdleFunc(spin): function to redisplay many time
def spin():
    global global_rotation_angle, pos_rotate
    pos_rotate = 1
    global_rotation_angle += 0.08
    glutPostRedisplay()


def stop():
    global global_rotation_angle, pos_rotate
    pos_rotate = 0
    global_rotation_angle = 0
    glutPostRedisplay()


def keyboard(key, x, y):
    global global_rotation_angle

    if key == b'a':
        glutIdleFunc(spin)
    elif key == b's':
        glutIdleFunc(stop)

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