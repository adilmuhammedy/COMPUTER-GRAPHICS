from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
theta=0
wsize=800
x=0
y=0
side=100
def drawRectangle(x,y):
    glBegin(GL_QUADS)
    glVertex2f((x-100)*math.cos(theta)-(y+50)*math.sin(theta),(y+50)*math.cos(theta)+(x-100)*math.sin(theta))
    glVertex2f((x+100)*math.cos(theta)-(y+50)*math.sin(theta), (y+50)*math.cos(theta)+(x+100)*math.sin(theta))
    glVertex2f((x+ 100)*math.cos(theta)-(y-50)*math.sin(theta), (y - 50)*math.cos(theta)+(x+100)*math.sin(theta))
    glVertex2f((x- 100)*math.cos(theta)-(y-50)*math.sin(theta), (y-50)*math.cos(theta)+(x-100)*math.sin(theta))
    glEnd()
def draw():
    global x,y
    glColor3f(1,0,0)
    glClear(GL_COLOR_BUFFER_BIT)
    drawRectangle(x,y)
    glutSwapBuffers()


def animate(temp):
    global x,y,theta
    glutPostRedisplay()
    glutTimerFunc(int(10000 /60), animate, int(0))
    if(theta>=360):
        theta=0
    theta+=1


def main():
    glutInit(sys.argv)
    glutInitWindowSize(wsize,wsize)
    glutInitWindowPosition(0,0)
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("Poly")
    glutDisplayFunc(draw)
    glutTimerFunc(0, animate, 0)
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(-wsize, wsize, -wsize, wsize)
    glutMainLoop()

main()
