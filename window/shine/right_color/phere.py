from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

light_ambientY = [1.0, 1.0, 0.0, 1.0]
light_ambientR = [1.0, 0.0, 0.0, 1.0]
light_ambientB = [0.0, 0.5, 1.0, 1.0]

sphere_yellow_rotation_angle = 0
sphere_red_rotation_angle = 0
sphere_x = 1


def init():
    w, h = 800, 600
    mat_specular = [1.0, 1.0, 1.0, 1.0]
    mat_shininess = [50.0]
    light_position = [1.0, 1.0, 1.0, 0.0]

    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(w, h)
    glutCreateWindow("OpenGL Window")

    glShadeModel(GL_SMOOTH)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST)
    glClearColor(0.0, 0.0, 0.0, 0.0)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(65.0, w / h, 1.0, 20.0)

    glMatrixMode(GL_MODELVIEW)


def display():
    global sphere_yellow_rotation_angle, sphere_red_rotation_angle

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -5.0)

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

    # Red Sphere
    glMaterialfv(GL_FRONT, GL_AMBIENT, light_ambientR)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, light_ambientR)
    glPushMatrix()
    glRotatef(sphere_red_rotation_angle, 0, 0, 1)
    glTranslatef(-1.0, 0.0, 0.0)
    glutSolidSphere(0.5, 60, 60)
    glPopMatrix()

    # Blue Sphere
    glMaterialfv(GL_FRONT, GL_AMBIENT, light_ambientB)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, light_ambientB)
    glPushMatrix()
    glTranslatef(1.0, 0.0, 0.0)
    glutSolidSphere(1.0, 50, 50)
    glPopMatrix()

    # Yellow Sphere
    glMaterialfv(GL_FRONT, GL_AMBIENT, light_ambientY)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, light_ambientY)
    glPushMatrix()
    glRotatef(sphere_yellow_rotation_angle, 0, 0, 1)
    glTranslatef(1.0, 2.0, 0.0)
    glutSolidSphere(0.5, 60, 60)
    glPopMatrix()

    glDisable(GL_LIGHT0)
    glDisable(GL_LIGHTING)
    glutSwapBuffers()


def spin():
    global sphere_yellow_rotation_angle, sphere_red_rotation_angle
    sphere_yellow_rotation_angle += 1
    sphere_red_rotation_angle += 1
    glutPostRedisplay()


def stop():
    global sphere_yellow_rotation_angle, sphere_red_rotation_angle
    sphere_yellow_rotation_angle = 0
    sphere_red_rotation_angle = 0
    glutPostRedisplay()


def keyboard(key, x, y):
    if key == b'b':
        glutIdleFunc(spin)
    elif key == b's':
        glutIdleFunc(stop)


if __name__ == "__main__":
    glutInit()
    init()
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutMainLoop()
