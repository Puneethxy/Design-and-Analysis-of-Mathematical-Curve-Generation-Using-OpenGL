import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import time
import sys

# -----------------------------
# Bernstein Polynomial
# -----------------------------
def bernstein(i, t):
    if i == 0:
        return (1 - t) ** 3
    elif i == 1:
        return 3 * t * (1 - t) ** 2
    elif i == 2:
        return 3 * t ** 2 * (1 - t)
    elif i == 3:
        return t ** 3

# -----------------------------
# Bicubic Bézier Surface
# -----------------------------
def bezier_surface(u, v, control_points):
    point = np.zeros(3)

    for i in range(4):
        for j in range(4):
            point += bernstein(i, u) * bernstein(j, v) * control_points[i][j]

    return point

# -----------------------------
# Compute Surface Grid
# -----------------------------
def compute_surface(ctrl_pts, resolution=20):
    start_time = time.time()

    surface_points = []

    for u in np.linspace(0, 1, resolution):
        row = []
        for v in np.linspace(0, 1, resolution):
            p = bezier_surface(u, v, ctrl_pts)
            row.append(p)
        surface_points.append(row)

    end_time = time.time()

    exec_time = end_time - start_time
    space_usage = sys.getsizeof(surface_points)

    print(f"\nSurface computation ({resolution}x{resolution} grid):")
    print(f"  Time complexity (execution time): {exec_time:.6f} sec")
    print(f"  Space complexity (approx memory): {space_usage} bytes")

    return surface_points

# -----------------------------
# Draw Control Grid
# -----------------------------
def draw_control_grid(ctrl_pts):
    glColor3f(1, 0, 0)
    glPointSize(6)

    # Draw points
    glBegin(GL_POINTS)
    for i in range(4):
        for j in range(4):
            glVertex3fv(ctrl_pts[i][j])
    glEnd()

    # Draw grid lines
    glColor3f(0.6, 0.6, 0.6)
    for i in range(4):
        glBegin(GL_LINE_STRIP)
        for j in range(4):
            glVertex3fv(ctrl_pts[i][j])
        glEnd()

    for j in range(4):
        glBegin(GL_LINE_STRIP)
        for i in range(4):
            glVertex3fv(ctrl_pts[i][j])
        glEnd()

# -----------------------------
# Draw Surface Wireframe
# -----------------------------
def draw_surface(surface_pts):
    glColor3f(0, 0, 1)

    for row in surface_pts:
        glBegin(GL_LINE_STRIP)
        for p in row:
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

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -10)

    angle = 0
    run = True

    # Random 4x4 Control Grid
    ctrl_pts = np.random.uniform(-2, 2, (4, 4, 3))

    surface_pts = compute_surface(ctrl_pts, resolution=25)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glPushMatrix()
        glRotatef(angle, 1, 1, 0)
        angle += 0.3

        draw_control_grid(ctrl_pts)
        draw_surface(surface_pts)

        glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()

if __name__ == "__main__":
    main()
