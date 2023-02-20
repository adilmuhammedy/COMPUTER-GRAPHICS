from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
x=0
y=0
wsize=1000
ty=0
def bucket():
    global ty
    glColor3f(1,0,0)
    glLineWidth(5)
    glBegin(GL_LINES)
    glVertex2f(-100,0)
    glVertex2f(100, 0)
    glVertex2f(100, -5)
    glVertex2f(100, 400)
    glVertex2f(-100, -5)
    glVertex2f(-100, 400)
    glEnd()
    glFlush()
    x=0
    y=0
    glColor3f(1,1,0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x-100,y+0)
    glVertex2f(x+100, y+0)
    glVertex2f(x+100,y+ty)
    glVertex2f(x-100, y+ty)
    glEnd()
    glFlush()


def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    bucket()
    glutSwapBuffers()

def animate(temp):
    global ty
    glutPostRedisplay()
    glutTimerFunc(int(1000/60),animate,int(0))
    if (y+ty>350):
        ty=0
    else:
        ty+=1


def main():
    glutInit()
    glutInitWindowSize(wsize,wsize)
    glutInitWindowPosition(0,0)
    glutCreateWindow('crckle')
    glutDisplayFunc(draw)
    glutTimerFunc(0,animate,0)
    glClearColor(0,0,0,0)
    gluOrtho2D(-wsize,wsize,-wsize,wsize)
    glutMainLoop()

main()
