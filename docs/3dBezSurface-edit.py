import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

# -----------------------------
# Bernstein
# -----------------------------
def bernstein(i, t):
    if i == 0: return (1 - t)**3
    if i == 1: return 3*t*(1 - t)**2
    if i == 2: return 3*t**2*(1 - t)
    if i == 3: return t**3

# -----------------------------
# Surface Equation
# -----------------------------
def bezier_surface(u, v, ctrl):
    p = np.zeros(3)
    for i in range(4):
        for j in range(4):
            p += bernstein(i,u)*bernstein(j,v)*ctrl[i][j]
    return p

def compute_surface(ctrl, res=20):
    surface = []
    for u in np.linspace(0,1,res):
        row=[]
        for v in np.linspace(0,1,res):
            row.append(bezier_surface(u,v,ctrl))
        surface.append(row)
    return surface

# -----------------------------
# Draw
# -----------------------------
def draw_surface(surface):
    glColor3f(0,0,1)
    for row in surface:
        glBegin(GL_LINE_STRIP)
        for p in row:
            glVertex3fv(p)
        glEnd()

def draw_control_grid(ctrl, selected):
    glPointSize(8)
    glBegin(GL_POINTS)
    for i in range(4):
        for j in range(4):
            if selected == (i,j):
                glColor3f(0,1,0)
            else:
                glColor3f(1,0,0)
            glVertex3fv(ctrl[i][j])
    glEnd()

# -----------------------------
# Main
# -----------------------------
def main():
    pygame.init()
    display=(800,600)
    pygame.display.set_mode(display, pygame.OPENGL|pygame.DOUBLEBUF)
    glEnable(GL_DEPTH_TEST)

    gluPerspective(45,display[0]/display[1],0.1,50)
    glTranslatef(0,0,-10)

    ctrl = np.random.uniform(-2,2,(4,4,3))
    selected=None
    dragging=False
    clock=pygame.time.Clock()

    while True:
        mx,my=pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                return

            if event.type==pygame.MOUSEBUTTONDOWN:
                dragging=True
                # Find nearest control point
                flat=[(i,j) for i in range(4) for j in range(4)]
                distances=[]
                for i,j in flat:
                    p=ctrl[i][j]
                    screen=np.array([(mx-400)/100,(300-my)/100])
                    distances.append(np.linalg.norm(p[:2]-screen))
                selected=flat[np.argmin(distances)]

            if event.type==pygame.MOUSEBUTTONUP:
                dragging=False
                selected=None

        keys=pygame.key.get_pressed()

        if selected:
            i,j=selected
            if dragging:
                ctrl[i][j][0]=(mx-400)/100
                ctrl[i][j][1]=(300-my)/100
            if keys[pygame.K_q]:
                ctrl[i][j][2]+=0.05
            if keys[pygame.K_e]:
                ctrl[i][j][2]-=0.05

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        surface=compute_surface(ctrl,25)

        draw_surface(surface)
        draw_control_grid(ctrl,selected)

        pygame.display.flip()
        clock.tick(60)

if __name__=="__main__":
    main()
