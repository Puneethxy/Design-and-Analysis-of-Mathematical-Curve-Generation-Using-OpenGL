import pygame
from OpenGL.GL import *
from OpenGL.GLU import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((500, 500), pygame.OPENGL | pygame.DOUBLEBUF)
    pygame.display.set_caption("OpenGL Line Example")
    glViewport(0, 0, 500, 500)
    gluOrtho2D(-1, 1, -1, 1)

    glClearColor(1.0, 1.0, 1.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(1, 0, 0)
    glBegin(GL_LINES)
    glVertex2f(-0.8, -0.8)
    glVertex2f(0.8, 0.8)
    glEnd()

    glFlush()
    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

if __name__ == "__main__":
    main()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
