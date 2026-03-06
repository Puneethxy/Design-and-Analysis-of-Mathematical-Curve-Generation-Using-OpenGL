import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import time
import sys

# -----------------------------
# 3D Cubic Bézier Function
# -----------------------------
def bezier_cubic_3d(t, P0, P1, P2, P3):
    x = (1 - t)**3 * P0[0] + 3*(1 - t)**2 * t * P1[0] + 3*(1 - t) * t**2 * P2[0] + t**3 * P3[0]
    y = (1 - t)**3 * P0[1] + 3*(1 - t)**2 * t * P1[1] + 3*(1 - t) * t**2 * P2[1] + t**3 * P3[1]
    z = (1 - t)**3 * P0[2] + 3*(1 - t)**2 * t * P1[2] + 3*(1 - t) * t**2 * P2[2] + t**3 * P3[2]
    return [x, y, z]


# -----------------------------
# Draw Control Polygon (3D)
# -----------------------------
def draw_control_polygon(points):
    glColor3f(0.6, 0.6, 0.6)
    glBegin(GL_LINE_STRIP)
    for p in points:
        glVertex3f(p[0], p[1], p[2])
    glEnd()

    glColor3f(1, 0, 0)
    glPointSize(8)
    glBegin(GL_POINTS)
    for p in points:
        glVertex3f(p[0], p[1], p[2])
    glEnd()


# -----------------------------
# Compute Curve Points
# -----------------------------
def compute_curve(ctrl_points, num_points=100):
    start_time = time.time()

    curve_points = []
    for t in np.linspace(0, 1, num_points):
        p = bezier_cubic_3d(t, *ctrl_points)
        curve_points.append(p)

    end_time = time.time()

    exec_time = end_time - start_time
    space_usage = sys.getsizeof(curve_points) + sum(sys.getsizeof(pt) for pt in curve_points)

    print(f"\n3D Curve computation for {num_points} points:")
    print(f"  Time complexity (execution time): {exec_time:.6f} seconds")
    print(f"  Space complexity (memory usage): {space_usage} bytes")

    return curve_points


# -----------------------------
# Main Function
# -----------------------------
def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, pygame.OPENGL | pygame.DOUBLEBUF)
    pygame.display.set_caption("3D Cubic Bézier Curve")

    # Enable depth testing
    glEnable(GL_DEPTH_TEST)

    # Perspective Projection
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -8)

    run = True
    angle = 0

    # 4 Random 3D Control Points
    ctrl_points = np.random.uniform(-2, 2, (4, 3))
    ctrl_points = [tuple(pt) for pt in ctrl_points]

    curve_points = compute_curve(ctrl_points, num_points=200)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Rotate scene to visualize 3D
        glPushMatrix()
        glRotatef(angle, 1, 1, 0)
        angle += 0.5

        # Draw Control Polygon
        draw_control_polygon(ctrl_points)

        # Draw Bézier Curve
        glColor3f(0, 0, 1)
        glLineWidth(3)
        glBegin(GL_LINE_STRIP)
        for p in curve_points:
            glVertex3f(p[0], p[1], p[2])
        glEnd()

        glPopMatrix()
        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()


if __name__ == "__main__":
    main()
