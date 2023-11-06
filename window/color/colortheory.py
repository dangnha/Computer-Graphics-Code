from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Define the vertices and normals for the triangle
vertices = [
    (0.0, 1.0, 0.0),
    (-1.0, -1.0, 0.0),
    (1.0, -1.0, 0.0)
]

normals = [
    (0.0, 0.0, 1.0),
    (0.0, 0.0, 1.0),
    (0.0, 0.0, 1.0)
]

# Define material properties for the triangle
material_diffuse = [
    (1.0, 0.0, 0.0, 1.0),  # Red
    (0.0, 1.0, 0.0, 1.0),  # Green
    (0.0, 0.0, 1.0, 1.0)  # Blue
]

material_specular = (1.0, 1.0, 1.0, 1.0)  # White
material_shininess = 50.0

# Define light properties
light_position = (1.0, 1.0, 1.0, 0.0)
light_diffuse = (1.0, 1.0, 1.0, 1.0)  # White


def draw_triangle():
    glBegin(GL_TRIANGLES)
    for i in range(3):
        glMaterialfv(GL_FRONT, GL_DIFFUSE, material_diffuse[i])
        glMaterialfv(GL_FRONT, GL_SPECULAR, material_specular)
        glMaterialfv(GL_FRONT, GL_SHININESS, material_shininess)
        glNormal3fv(normals[i])
        glVertex3fv(vertices[i])
    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHTING)
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
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow("Gradient Triangle with Lighting and Materials")
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_COLOR_MATERIAL)
    glutMainLoop()


if __name__ == "__main__":
    main()
