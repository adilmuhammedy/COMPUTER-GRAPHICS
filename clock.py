from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
x=0
y=0
wsize=1000
theta1=0
theta2=0
def circle():
    global x,y
    r1=500
    glColor3f(1,0,0)
    glBegin(GL_TRIANGLE_FAN)
    for theta1 in range(0,360,1):
        glVertex2f(r1*math.cos(theta1),r1*math.sin(theta1))
    glEnd()
    glFlush()
    r2=480
    glColor3f(1,1,1)
    glBegin(GL_TRIANGLE_FAN)
    for theta1 in range(0,360,1):
        glVertex2f(r2*math.cos(theta1),r2*math.sin(theta1))
    glEnd()
    glFlush()
    glColor3f(1,0,0)
    glPointSize(5)
    glBegin(GL_POINTS)
    for i in range(0,360,30):
        glVertex2f(450*math.cos(math.radians(i)),450*math.sin(math.radians(i)))
    glEnd()
    glFlush()

def needle():
    global theta1,theta2
    glColor3f(1,0,0)
    glLineWidth(2)
    glBegin(GL_LINES)
    glVertex2f(0,0)
    glVertex2f(400*math.sin(theta1),400*math.cos(theta1))
    glEnd()
    glFlush()

    glBegin(GL_POLYGON)
    glVertex2f((x+20)* math.cos(theta1) + (y+400) * math.sin(theta1), -(x+20) * math.sin(theta1) + (y+400) * math.cos(theta1))
    glVertex2f((x-20 )* math.cos(theta1) + (y+400) * math.sin(theta1), -(x-20) * math.sin(theta1) + (y+400) * math.cos(theta1))
    glVertex2f(x * math.cos(theta1) + (y+420) * math.sin(theta1), -x * math.sin(theta1) + (y+420) * math.cos(theta1))
    glEnd()
    glFlush()



    glColor3f(1,0,0)
    glLineWidth(5)
    glBegin(GL_LINES)
    glVertex2f(0,0)
    glVertex2f(250*math.sin(theta2),250*math.cos(theta2))
    glEnd()
    glFlush()

    glBegin(GL_POLYGON)
    glVertex2f((x+20)* math.cos(theta2) + (y+200) * math.sin(theta2), -(x+20) * math.sin(theta2) + (y+200) * math.cos(theta2))
    glVertex2f((x-20 )* math.cos(theta2) + (y+200) * math.sin(theta2), -(x-20) * math.sin(theta2) + (y+200) * math.cos(theta2))
    glVertex2f(x * math.cos(theta2) + (y+260) * math.sin(theta2), -x * math.sin(theta2) + (y+260) * math.cos(theta2))
    glEnd()
    glFlush()
def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    circle()
    needle()
    glutSwapBuffers()

def animate(temp):
    global theta1,theta2
    glutPostRedisplay()
    glutTimerFunc(int(1000/60),animate,int(0))
    if(theta1<360 and theta2<360):
        theta1=theta1+0.1
        theta2=theta2+0.001
    else:
        theta1=0
        theta2=0




def main():
    glutInit()
    glutInitWindowSize(wsize,wsize)
    glutInitWindowPosition(0,0)
    glutCreateWindow('clock')
    glutDisplayFunc(draw)
    glutTimerFunc(0,animate,0)
    glClearColor(0,0,0,0)
    gluOrtho2D(-wsize,wsize,-wsize,wsize)
    glutMainLoop()

main()
