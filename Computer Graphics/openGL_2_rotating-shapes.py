import sys
sys.path.append('/Users/johnmessina/Documents/GitHub/Math-CS-Practice-Problems/Math-CS-Practice-Problems/')
from Algorithms.RemovePrintPath import *
RemovePrintPath()

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Define vertices
    # Keep in mind, order matters
    # Defined as a tuple of lists
# Define edges
# Define colors
# Define quads
# Define cube function
# Define main function
# Run main

vertices = (
    [-1,0,1], # 0 (lower left corner)
    [-1,0,-1],# 1 (upper left corner)
    [1,0,-1], # 2 (upper right corner)
    [1,0,1],  # 3 (lower right corner)
    [0,1,0]   # 4 (apex)
)

edges = (
    [0,1], # 0 left edge
    [1,2], # 1 upper edge
    [2,3], # 2 right edge
    [3,0], # 3 lower edger
    [0,4], # 4 lower left to apex
    [1,4], # 5 upper left to apex
    [2,4], # 6 upper right to apex
    [3,4]  # 7 lower right to apex
)

colors = (
    [  1,   0,   0],
    [  0,   1,   0],
    [  0,   0,   1],
    [  1,   1,   0],
    [  1,   0,   1],
    [  0,   1,   1],
    [  1,   0,   0],
    [  0,   1,   0]
)

quads = (
    [0,1,2,3]
)

triangles = (
    [0,1,4],
    [1,2,4],
    [2,3,4],
    [3,4,0]
)


def Pyramid():
    glBegin(GL_QUADS)
    x = 0
    for vertex in quads:
        glColor3fv(colors[x])
        glVertex3fv(vertices[vertex])
        x+=1
    glEnd()

    glBegin(GL_TRIANGLES)
    for triangle in triangles:
        x = 0
        for vertex in triangle:
            glColor3fv(colors[x])
            glVertex3fv(vertices[vertex])
            x+=1
    glEnd()

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(40, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0,0,-5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        glRotatef(1, 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Pyramid()
        pygame.display.flip()
        pygame.time.wait(10)

main()