import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import time
import sys

def bezier_cubic(t, P0, P1, P2, P3):
    x = (1 - t)**3 * P0[0] + 3*(1 - t)**2 * t * P1[0] + 3*(1 - t) * t**2 * P2[0] + t**3 * P3[0]
    y = (1 - t)**3 * P0[1] + 3*(1 - t)**2 * t * P1[1] + 3*(1 - t) * t**2 * P2[1] + t**3 * P3[1]
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

def compute_curve(ctrl_points, num_points=100):
    start_time = time.time()
    curve_points = []
    for t in np.linspace(0, 1, num_points):
        p = bezier_cubic(t, *ctrl_points)
        curve_points.append(p)
    end_time = time.time()
    exec_time = end_time - start_time
    space_usage = sys.getsizeof(curve_points) + sum(sys.getsizeof(pt) for pt in curve_points)
    print(f"Curve computation for {num_points} points:")
    print(f"  Time complexity (execution time): {exec_time:.6f} seconds")
    print(f"  Space complexity (memory usage): {space_usage} bytes")
    return curve_points

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 600), pygame.OPENGL | pygame.DOUBLEBUF)
    pygame.display.set_caption("Cubic Bézier Curve Example (Randomized & Complexity)")
    glViewport(0, 0, 600, 600)
    gluOrtho2D(0, 1, 0, 1)
    run = True

    # Four randomized control points
    ctrl_points = np.random.rand(4, 2)
    ctrl_points = [tuple(pt) for pt in ctrl_points]

    # Compute curve points and print complexity
    curve_points = compute_curve(ctrl_points, num_points=100)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        glClearColor(1, 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT)

        draw_control_polygon(ctrl_points)

        glColor3f(0, 0, 1)
        glLineWidth(2)
        glBegin(GL_LINE_STRIP)
        for p in curve_points:
            glVertex2f(p[0], p[1])
        glEnd()

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Time Complexity
#The main computation is done in this loop:
#for t in np.linspace(0, 1, 100):
#    p = bezier_cubic(t, *ctrl_points)
#    glVertex2f(p[0], p[1])
#For every 100 sampled values of parameter t, you calculate the cubic Bézier formula.
#Each computation involves a fixed number of arithmetic operations (constant time O(1)since there are always 
#exactly 4 control points in cubic Bézier.
#Total time complexity: O(k), where k= 100 is the number of sample points.
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Space Complexity
#The space complexity is determined by the storage of control points and temporary variables.
#The space needed for the control points is constant: 4 points × 2 coordinates = fixed small size O(1).
#Temporary variables used in calculations also take constant space O(1).
#The 100 computed points along the curve are generated on the fly and passed directly to OpenGL for rendering without explicit storage, so no extra storage for points is required.
#Total space complexity: O(1)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

