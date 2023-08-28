from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window = 0                                             # glut window number
width, height = 1000, 800                               # window size

# start drawing a rectangle


def draw_rect(x, y, width, height):
    glBegin(GL_LINE_LOOP)
    glVertex2f(x, y)                                   # bottom left point
    glVertex2f(x + width, y)                           # bottom right point
    glVertex2f(x + width, y + height)                  # top right point
    glVertex2f(x, y + height)                          # top left point
    glEnd()


def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def draw():                                            # ondraw is called all the time
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # clear the screen
    glLoadIdentity()                                   # reset position
    refresh2d(width, height)                           # set mode to 2d

    # ToDo draw rectangle
    # start drawing a rectangle
    glColor3f(1.0, 0.0, 0.0)                           # set color to blue
    draw_rect(100, 250, 800, 300)

    # important for double buffering
    glutSwapBuffers()


# initialization
glutInit()                                             # initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width, height)                      # set window size
glutInitWindowPosition(0, 0)                           # set window position
# create window with title
window = glutCreateWindow("rectangle")
# set draw function callback
glutDisplayFunc(draw)
glutIdleFunc(draw)                                     # draw all the time
glutMainLoop()
