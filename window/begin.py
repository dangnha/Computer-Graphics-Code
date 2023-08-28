import pygame as pg
from OpenGL.GL import *
from OpenGL.GLUT import *


import numpy as np


class App:

    def __init__(self):
        pg.init()
        pg.display.set_mode((840, 680), pg.OPENGL | pg.DOUBLEBUF)
        self.clock = pg.time.Clock()
        # Initialize OpenGL
        glClearColor(0.1, 0.2, 0.2, 1)
        self.mainloop()

    def mainloop(self):
        running = True
        while running:
            # Check event
            for event in pg.event.get():
                if (event.type == pg.QUIT):
                    running = False
            # Refresh screen
            glClear(GL_COLOR_BUFFER_BIT)
            # --------------------------------
            # Draw the polygon
            glColor3f(1.0, 0.0, 0.0)
            glBegin(GL_POLYGON)
            glVertex2f(-0.5, -0.5)
            glVertex2f(0.5, -0.5)
            glVertex2f(0.5, 0.5)
            glVertex2f(-0.5, 0.5)
            glEnd()
            # --------------------------------

            # Flip frame
            pg.display.flip()

            # timing
            self.clock.tick(60)
        self.quit()

    def quit(self):
        pg.quit()


class Triangle:

    def __init__(self):
        # x,y,z,r,g,b,a - That mean we input position, color, textures
        self.vertices = (
            -0.5, -0.5, 0.0, 1.0, 0.0, 0.0,  # mean position x,y,z and color red
            0.5, -0.5, 0.0, 0.0, 1.0, 0.0,
            0.0, 0.5, 0.0, 0.0, 0.0, 0.1
        )

        self.vertices = np.array(self.vertices, dtype=np.float32)
        self.vertex_count = 3
        self.vao = glGenVertexArrays(1)
        glBindVertexArray(self.vao)
        self.vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes,
                     self.vertices, GL_STATIC_DRAW)
        # 2:55


if __name__ == "__main__":
    myApp = App()
