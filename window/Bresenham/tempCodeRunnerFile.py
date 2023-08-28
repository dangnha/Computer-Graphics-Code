if dx > dy:
        err = dx / 2.0
        while x != x2:
            glVertex2f(x, y)
            err -= dy
            if err < 0:
                y += sy
                err += dx
            x += sx
    else:
        err = dy / 2.0
        while y != y2:
            glVertex2f(x, y)
            err -= dx
            if err < 0:
                x += sx
                err += dy
            y += sy
