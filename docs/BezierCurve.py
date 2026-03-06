import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

def bezier_curve(t, points):
    # Binomial coefficients for cubic (n=3)
    P0, P1, P2, P3 = points
    x = (1-t)**3 * P0[0] + 3*(1-t)**2 * t * P1[0] + 3*(1-t)*t**2 * P2[0] + t**3 * P3[0]
    y = (1-t)**3 * P0[1] + 3*(1-t)**2 * t * P1[1] + 3*(1-t)*t**2 * P2[1] + t**3 * P3[1]
    return [x, y]

def draw_control_polygon(points):
    glColor3f(0.5, 0.5, 0.5)
    glBegin(GL_LINE_STRIP)
    for p in points:
        glVertex2f(p[0], p[1])
    glEnd()

    glColor3f(1, 0, 0)
    glPointSize(8)
    glBegin(GL_POINTS)
    for p in points:
        glVertex2f(p[0], p[1])
    glEnd()

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 600), pygame.OPENGL | pygame.DOUBLEBUF)
    pygame.display.set_caption("Cubic Bézier Curve Example")
    glViewport(0, 0, 600, 600)
    gluOrtho2D(0, 1, 0, 1)  # Coordinate range (0,0) to (1,1)
    run = True

    # Control points: change these to reshape the curve
    ctrl_points = [
        (0.1, 0.1),  # Start
        (0.3, 0.8),  # Control
        (0.7, 0.2),  # Control
        (0.9, 0.9),  # End
    ]

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        glClearColor(1, 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT)

        # Draw control polygon and points
        draw_control_polygon(ctrl_points)

        # Draw Bézier curve
        glColor3f(0, 0, 1)  # Blue curve
        glLineWidth(2)
        glBegin(GL_LINE_STRIP)
        for t in np.linspace(0, 1, 100):
            p = bezier_curve(t, ctrl_points)
            glVertex2f(p[0], p[1])
        glEnd()

        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()
