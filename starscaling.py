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
tx=0
ty=0

def star(x,y):
    glBegin(GL_POLYGON)
    glVertex2f((x-100)*tx,(y+100)*ty)
    glVertex2f(x*tx, (y+300)*ty)
    glVertex2f((x+ 100)*tx, (y + 100)*ty)
    glVertex2f((x+ 300)*tx, y*ty)
    glVertex2f((x+ 100)*tx, (y- 100)*ty)
    glVertex2f(x*tx, (y- 300)*ty)
    glVertex2f((x- 100)*tx, (y- 100)*ty)
    glVertex2f((x- 300)*tx, y*ty)
    glEnd()

def draw():
    global x, y
    glColor3f(1, 0, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    star(x, y)
    glutSwapBuffers()

def animate(temp):
    global x,y,tx,ty
    glutPostRedisplay()
    glutTimerFunc(int(1000 /60), animate, int(0))
    dir=0
    if(tx>=2 or ty>=2):
        tx=ty=0
        dir=1
    else:
        tx+=0.01
        ty+=0.01
    if dir==1:
        tx-=1
        ty-=1


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
