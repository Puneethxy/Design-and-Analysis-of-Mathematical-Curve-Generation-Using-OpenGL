import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

# -----------------------------
# Bézier Curve
# -----------------------------
def bezier_cubic_3d(t, P0, P1, P2, P3):
    return (
        (1 - t)**3 * P0 +
        3*(1 - t)**2 * t * P1 +
        3*(1 - t) * t**2 * P2 +
        t**3 * P3
    )

def compute_curve(ctrl_points, num_points=100):
    return [bezier_cubic_3d(t, *ctrl_points)
            for t in np.linspace(0, 1, num_points)]

# -----------------------------
# Draw
# -----------------------------
def draw_curve(points):
    glColor3f(0, 0, 1)
    glBegin(GL_LINE_STRIP)
    for p in points:
        glVertex3fv(p)
    glEnd()

def draw_control_points(ctrl_points, selected):
    glPointSize(10)
    glBegin(GL_POINTS)
    for i, p in enumerate(ctrl_points):
        if i == selected:
            glColor3f(0, 1, 0)
        else:
            glColor3f(1, 0, 0)
        glVertex3fv(p)
    glEnd()

# -----------------------------
# Main
# -----------------------------
def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, pygame.OPENGL | pygame.DOUBLEBUF)
    glEnable(GL_DEPTH_TEST)

    gluPerspective(45, display[0]/display[1], 0.1, 50.0)
    glTranslatef(0, 0, -8)

    ctrl_points = np.random.uniform(-2, 2, (4, 3))
    selected = None
    dragging = False

    clock = pygame.time.Clock()

    while True:
        mouse_x, mouse_y = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.MOUSEBUTTONDOWN:
                dragging = True
                # Select nearest control point (simple distance check)
                selected = np.argmin([
                    np.linalg.norm(p[:2] - np.array([(mouse_x-400)/100, (300-mouse_y)/100]))
                    for p in ctrl_points
                ])

            if event.type == pygame.MOUSEBUTTONUP:
                dragging = False
                selected = None

        keys = pygame.key.get_pressed()
        if selected is not None:
            if dragging:
                ctrl_points[selected][0] = (mouse_x - 400)/100
                ctrl_points[selected][1] = (300 - mouse_y)/100
            if keys[pygame.K_q]:
                ctrl_points[selected][2] += 0.05
            if keys[pygame.K_e]:
                ctrl_points[selected][2] -= 0.05

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        curve = compute_curve(ctrl_points)

        draw_curve(curve)
        draw_control_points(ctrl_points, selected)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
