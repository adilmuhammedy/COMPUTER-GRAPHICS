# 20220001 ADIL MUHAMMED Y SHEARING

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-100, 100.0, -100, 100.0)


def plotaxes():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINES)
    glVertex2f(0, -500)
    glVertex2f(0, 500)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(500, 0)
    glVertex2f(-500, 0)
    glEnd()


def plotgrid():
    glColor3f(0.202, 0.202, 0.202)
    for i in range(-500, 500, 50):
        if i != 0:
            glBegin(GL_LINES)
            glVertex2f(i, 500)
            glVertex2f(i, -500)
            glEnd()
            glBegin(GL_LINES)
            glVertex2f(500, i)
            glVertex2f(-500, i)
            glEnd()


def plotTriangle(x1, x2, x3, y1, y2, y3):
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(x2, y2)
    glVertex2f(x3, y3)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(x3, y3)
    glVertex2f(x1, y1)
    glEnd()


def drawSheared(x1, x2, x3, y1, y2, y3, shf, ref, choice):
    points = [[x1, y1], [x2, y2], [x3, y3]]
    newpoints = []
    for point in points:
        if (choice == 1):
            newpoints.append([point[0] + shf * (point[1] - ref), point[1]])
        elif (choice == 2):
            newpoints.append([point[0], point[1] + shf * (point[0] - ref)])
    plotaxes()
    plotgrid()
    glColor3f(0, 0, 1)
    plotTriangle(x1, x2, x3, y1, y2, y3)
    glColor3f(1, 0, 1)
    plotTriangle(newpoints[0][0], newpoints[1][0], newpoints[2][0], newpoints[0][1], newpoints[1][1], newpoints[2][1])
    glFlush()

def main():
    print("\nEnter Triangle co-ordinates:")
    x1 = float(input("\n\tx1: "))
    y1 = float(input("\n\ty1: "))
    side = float(input("\n\tside: "))
    x2 = x1 + side
    y2 = y1
    x3 = x1 + side / 2
    y3 = y1 + 0.86602540378 * side

    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    print("1.In X direction w.r.t yref\n2.In Y direction w.r.t xref")
    choice = int(input("Enter choice: "))
    shf = float(input("Enter shear factor: "))
    ref = int(input("Enter reference point: "))
    glutCreateWindow("2D Transformations - Shearing")
    glutDisplayFunc(lambda: drawSheared(x1, x2, x3, y1, y2, y3, shf, ref, choice))
    init()
    glutMainLoop()


main()
