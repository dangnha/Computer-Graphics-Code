from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import cos, sin


# List to store circle information (center and color)
circles = []


def draw_circle(center, radius, color):
    glColor3fv(color)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2fv(center)  # Center of the circle
    for i in range(361):  # 361 points to include the last point and close the fan
        angle = i * 2.0 * 3.141592 / 360
        x = center[0] + radius * cos(angle)
        y = center[1] + radius * sin(angle)
        glVertex2f(x, y)
    glEnd()


def on_mouse_click(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        # Add a new circle with the current center and color
        circles.append({"center": (x, y), "radius": 50,
                       "color": [1.0, 1.0, 1.0]})
    elif button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        # Change color of all circles on right-click
        for circle in circles:
            circle["color"][0] = (circle["color"][0] + 0.1) % 1.0
            circle["color"][1] = (circle["color"][1] + 0.2) % 1.0
            circle["color"][2] = (circle["color"][2] + 0.3) % 1.0


def on_key_press(key, x, y):
    if key == b'\x1b':  # Escape key
        glutLeaveMainLoop()


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Draw all circles in the list
    for circle in circles:
        draw_circle(circle["center"], circle["radius"], circle["color"])

    glutSwapBuffers()


# Initialize GLUT
glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
glutCreateWindow(b"OpenGL Circle Drawer")
glutReshapeWindow(800, 600)
glOrtho(0, 800, 600, 0, -1, 1)

# Register callback functions
glutMouseFunc(on_mouse_click)
glutKeyboardFunc(on_key_press)
glutDisplayFunc(display)

# Main loop
glutMainLoop()
