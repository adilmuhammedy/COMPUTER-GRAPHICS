from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
wsize=1000
x=0
y=0
theta=0
theta1=90

def needle():
    glColor3f(0,0,1)
    glLineWidth(5)
    glBegin(GL_LINES)
    glVertex2f(0,0)
    glVertex2f(x*math.cos(theta)-(y+500)*math.sin(theta),x*math.sin(theta)+(y+500)*math.cos(theta))
    glEnd()
    glFlush()
    glBegin(GL_POLYGON)
    glVertex2f((x+200)* math.cos(theta) - (y+500) * math.sin(theta), (x+200) * math.sin(theta) + (y+500) * math.cos(theta))
    glVertex2f((x-200 )* math.cos(theta) - (y+500) * math.sin(theta), (x-200) * math.sin(theta) + (y+500) * math.cos(theta))
    glVertex2f(x * math.cos(theta) - (y+700) * math.sin(theta), x * math.sin(theta) + (y+700) * math.cos(theta))
    glEnd()
    glFlush()
    glLineWidth(5)
    glColor3f(1, 0, 0)
    glBegin(GL_LINES)
    glVertex2f(0,0)
    glVertex2f(x*math.cos(theta1)-(y+200)*math.sin(theta1),x*math.sin(theta1)+(y+200)*math.cos(theta1))
    glEnd()
    glFlush()
    glBegin(GL_POLYGON)
    glVertex2f((x+100)* math.cos(theta1) - (y+200) * math.sin(theta1), (x+100) * math.sin(theta1) + (y+200) * math.cos(theta1))
    glVertex2f((x-100 )* math.cos(theta1) - (y+200) * math.sin(theta1), (x-100) * math.sin(theta1) + (y+200) * math.cos(theta1))
    glVertex2f(x * math.cos(theta1) - (y+300) * math.sin(theta1), x * math.sin(theta1) + (y+300) * math.cos(theta1))
    glEnd()
    glFlush()

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    needle()
    glutSwapBuffers()

def animate(temp):
    global x,y,theta,theta1
    glutPostRedisplay()
    glutTimerFunc(int(1000/60),animate,int(0))
    if(theta<360 and theta1<360):
        theta=theta+0.01
        theta1=theta1+0.1
    else:
        theta=0
        theta1=90

def main():
    glutInit()
    glutInitWindowSize(wsize,wsize)
    glutInitWindowPosition(0,0)
    glutCreateWindow('neeedle')
    glutDisplayFunc(draw)
    glutTimerFunc(0,animate,0)
    glClearColor(1,1,1,1)
    gluOrtho2D(-wsize,wsize,-wsize,wsize)
    glutMainLoop()

main()
