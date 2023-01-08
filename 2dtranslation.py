from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
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

def plotTraingle(x1, x2, x3, y1, y2, y3):
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

def translation(x1, x2, x3, y1, y2, y3, tx, ty):
    points = [[x1, y1], [x2, y2], [x3, y3]]
    newpoints = []
    for a in points:
        newpoints.append([a[0]+tx, a[1]+ty])
    print(newpoints)
    plotaxes()
    glColor3f(0, 0, 1)
    plotTraingle(x1, x2, x3, y1, y2, y3)
    glColor3f(1, 0, 1)
    plotTraingle(newpoints[0][0], newpoints[1][0], newpoints[2] [0], newpoints[0][1], newpoints[1][1], newpoints[2][1])
    glFlush()

def main():
    print("\nEnter Triangle co-ordinates:")
    x1 = float(input("\n\tx1: "))
    y1 = float(input("\n\ty1: "))
    side = float(input("\n\tside: "))
    x2 = x1 + side
    y2 = y1
    x3 = x1+side/2
    y3 = y1+0.86602540378*side
    tx = int(input("\nX translation: "))
    ty = int(input("\nY translation: "))

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    glutCreateWindow("2D Transformations - translation")
    glutDisplayFunc(lambda: translation(x1, x2, x3, y1, y2, y3, tx, ty))
    init()
    glutMainLoop()

main()
