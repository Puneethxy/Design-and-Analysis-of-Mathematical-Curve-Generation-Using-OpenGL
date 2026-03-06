import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import time
import sys

def bezier_quad(t, P0, P1, P2):
    # Quadratic Bézier curve formula
    x = (1-t)**2 * P0[0] + 2*(1-t)*t * P1[0] + t**2 * P2[0]
    y = (1-t)**2 * P0[1] + 2*(1-t)*t * P1[1] + t**2 * P2[1]
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
    # Measure start time and memory
    start_time = time.time()
    curve_points = []
    for t in np.linspace(0, 1, num_points):
        p = bezier_quad(t, *ctrl_points)
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
    pygame.display.set_caption("Quadratic Bézier Curve Example (Randomized & Complexity)")
    glViewport(0, 0, 600, 600)
    gluOrtho2D(0, 1, 0, 1)
    run = True

    # Randomized control points for quadratic Bézier
    ctrl_points = np.random.rand(3, 2)
    ctrl_points = [tuple(pt) for pt in ctrl_points]

    # Compute curve points and show complexity before display loop
    curve_points = compute_curve(ctrl_points, num_points=100)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        glClearColor(1, 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT)

        draw_control_polygon(ctrl_points)

        glColor3f(0, 0, 1)  # Blue curve
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
#for t in np.linspace(0, 1, num_points):
#This loop runs 'num_points' times, and each iteration involves a constant amount of work (calculating the Bézier formula).
#Therefore, the time complexity is O(n), where n is the number of points computed on
#the curve (num_points).
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Space Complexity
#The space complexity is determined by the storage of the curve points.
#We store 'num_points' points, each requiring a fixed amount of space.
#Thus, the space complexity is also O(n), where n is the number of points computed on the curve (num_points). the curve (num_points).
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------