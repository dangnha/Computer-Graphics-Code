import pygame as pg
from OpenGL.GL import *


class App:

    def __init__(self):
        pg.init()
        pg.display.set_mode((640, 480), pg.OPENGL | pg.DOUBLEBUF)
        self.clock = pg.time.Clock()
        # Initialize OpenGL
        glClearColor(1, 0.2, 0.2, 1)
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
            # Draw the polygon
            glColor3f(0.0, 1.0, 0.0)
            glBegin(GL_POLYGON)
            glVertex2f(-0.5, -0.5)
            glVertex2f(0.5, -0.5)
            glVertex2f(0.5, 0.5)
            glVertex2f(-0.5, 0.5)
            glEnd()
            # Flip frame
            pg.display.flip()

            # timing
            self.clock.tick(60)
        self.quit()

    def quit(self):
        pg.quit()


if __name__ == "__main__":
    myApp = App()
