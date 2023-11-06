from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Define vertices for the tetrahedron
vertices = [
    (0.0, 3.0, 0.0),       # Top vertex
    (-1.0, 1.0, -1.0),    # Bottom left vertex
    (1.0, 1.0, -1.0),     # Bottom right vertex
    (0.0, 1.0, 1.0)       # Bottom back vertex
]

# Define colors for each vertex (gradient colors)
colors = [
    (1.0, 0.0, 0.0),
    (0.0, 1.0, 0.0),
    (0.0, 0.0, 1.0),
    (1.0, 1.0, 0.0)
]

# Define the faces of the tetrahedron using vertex indices
faces = [
    (0, 1, 2),  # Base face
    (0, 1, 3),  # Front face
    (0, 2, 3),  # Right face
    (1, 2, 3)   # Left face
]

# Define grid parameters
grid_size = 10
grid_step = 1


camera_pos = (3.0, 4.0, 5.0)  # Camera position
camera_target = (1.0, 2.0, 0.0)  # Camera target (look-at point)
camera_up = (0.0, 1.0, 0.0)  # Up vector


def draw_tetrahedron():
    glBegin(GL_TRIANGLES)
    for face in faces:
        for vertex_index in face:
            glColor3fv(colors[vertex_index])
            glVertex3fv(vertices[vertex_index])
    glEnd()


def draw_grid():
    glColor3f(0.5, 0.5, 0.5)  # Gray color for the grid
    for i in range(-grid_size, grid_size + 1, grid_step):
        glBegin(GL_LINES)
        glVertex3f(i, 0, -grid_size)
        glVertex3f(i, 0, grid_size)
        glVertex3f(-grid_size, 0, i)
        glVertex3f(grid_size, 0, i)
        glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(camera_pos[0], camera_pos[1], camera_pos[2],
              camera_target[0], camera_target[1], camera_target[2],
              camera_up[0], camera_up[1], camera_up[2])
    glTranslatef(0.0, 0.0, -6.0)
    glRotatef(1, 1, 1, 1)
    draw_grid()
    draw_tetrahedron()
    glFlush()


def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(70, (width / height), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)


def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow("Tetrahedron with Mesh Background")
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glEnable(GL_DEPTH_TEST)
    glutMainLoop()


if __name__ == "__main__":
    main()
