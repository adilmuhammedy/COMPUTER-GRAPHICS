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

def drawReflected(x1, x2, x3, y1, y2, y3, ch):
    points = [[x1, y1], [x2, y2], [x3, y3]]
    newpoints = []
    for point in points:
        if(ch == 1):
            newpoints.append([point[0], -point[1]])
        elif(ch == 2):
            newpoints.append([-point[0], point[1]])
        elif(ch == 3):
            newpoints.append([-point[0], -point[1]])
        elif(ch == 4):
            newpoints.append([point[1], point[0]])
        elif(ch == 5):
            newpoints.append([-point[1], -point[0]])
    print(newpoints)
    plotaxes()
    plotgrid()
    glColor3f(0, 0, 1)
    plotTraingle(x1, x2, x3, y1, y2, y3)
    glColor3f(1, 0, 1)
    plotTraingle(newpoints[0][0], newpoints[1][0], newpoints[2] [0], newpoints[0][1], newpoints[1][1], newpoints[2][1])
    glFlush()

def rotateHelper(x, y, theta):
    return [round((x*math.cos(theta)) - (y*math.sin(theta))), round((x*math.sin(theta)) + (y*math.cos(theta)))]

def drawReflectedAboutLine(x1, x2, x3, y1, y2, y3, a, b, c, original_color=(0, 1, 0), transformed_color=(1, 0, 0)):
    newpoints = [[x1, y1], [x2, y2], [x3, y3]]
    xoffset = -c/a if c != 0 else 0
    thetaoffset = math.atan(-a/b) if b != 0 else math.pi/2
    for i, point in enumerate(newpoints):
        newpoints[i] = [point[0] - xoffset, point[1]]
    for i, point in enumerate(newpoints):
        newpoints[i] = rotateHelper(point[0], point[1], -thetaoffset)
    for i, point in enumerate(newpoints):
        newpoints[i] = [point[0], -point[1]]
    for i, point in enumerate(newpoints):
        newpoints[i] = rotateHelper(point[0], point[1], thetaoffset)
    for i, point in enumerate(newpoints):
        newpoints[i] = [point[0] + xoffset, point[1]]
    plotaxes()
    plotgrid()
    glColor3f(original_color[0], original_color[1], original_color[2])
    plotTraingle(x1, x2, x3, y1, y2, y3)
    glColor3f(transformed_color[0], transformed_color[1], transformed_color[2])
    plotTraingle(newpoints[0][0], newpoints[1][0], newpoints[2] [0], newpoints[0][1], newpoints[1][1], newpoints[2][1])
    glFlush()


def reflect(x1, x2, x3, y1, y2, y3):
    print("Enter the type of reflection : ")
    ch = int(input("1.Reflection about x axis\n2.Reflection about y axis\n3.Reflection about origin\n4.Reflection about x=y line\n5.Reflection about x=-y line\n"))
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    glutCreateWindow("2D Transformations - reflection")
    glutDisplayFunc(lambda: drawReflected(x1, x2, x3, y1, y2, y3, ch))
    init()
    glutMainLoop()

def reflectAboutLine(x1, x2, x3, y1, y2, y3):
    print("Reflection about line ax + by + c = 0")
    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))
    c = int(input("Enter value of c: "))
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    glutCreateWindow("2D Transformations - reflect about line")
    glutDisplayFunc(lambda: drawReflectedAboutLine( x1, x2, x3, y1, y2, y3, a, b, c))
    init()
    glutMainLoop()

def main():
    print("\nEnter Triangle co-ordinates:")
    x1 = float(input("\n\tx1: "))
    y1 = float(input("\n\ty1: "))
    side = float(input("\n\tside: "))
    x2 = x1 + side
    y2 = y1
    x3 = x1+side/2
    y3 = y1+0.86602540378*side

    reflect(x1, x2, x3, y1, y2, y3)

main()
