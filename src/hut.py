from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys 

def init():
    glClearColor(0.15, 0.12, 0.32, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1.0, 0.0, 1.0, -1.0, 1.0)


def draw_cube(x, y, s):
    glColor3f(0.3,0.1,0.8)
    
    glBegin(GL_POLYGON)
    glVertex3f(x, y, 0.0)
    glVertex3f(x+s, y, 0.0)
    glVertex3f(x+s, y+s, 0.0)
    glVertex3f(x, y+s, 0.0)
    glEnd()

    glColor3f(0.1,0.4,0.7)
    glBegin(GL_POLYGON) 
    glVertex3f(x+s, y, 0.0)
    glVertex3f(x+s+s, y+0.1, 0.0) 
    glVertex3f(x+s+s, y+s+0.1, 0.0)  
    glVertex3f(x+s, y+s, 0.0)
    glEnd()

    glColor3f(0.2, 0.6, 0.4)
    glBegin(GL_POLYGON)
    glVertex3f(x+s, y+s, 0.0)
    glVertex3f(x+s+s, y+s+0.1, 0.0)
    glVertex3f(x+s, 0.2+y, 0.0)
    glVertex3f(x, y+s, 0.0)
    glEnd()
    glFlush()


def draw():
    draw_cube(.2,.2,0.3)
    draw_cube(0.01, 0.6, 0.1)


def hut():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.4, 0.2)
    
    glBegin(GL_POLYGON)
    glVertex3f (0.1, 0.1, 0.0);
    glVertex3f (0.4, 0.1, 0.0);
    glVertex3f (0.4, 0.5, 0.0);
    glVertex3f (0.1, 0.5, 0.0);
    glEnd();
    glColor3f(1.0,0.0,0.0);

    glBegin(GL_POLYGON);
    glVertex3f (0.10, 0.5, 0.0);
    glVertex3f (0.4, 0.5, 0.0);
    glVertex3f (0.25, 0.75, 0.0);
    glEnd();
    glColor3f(0.0,1.0,0.0);

    glBegin(GL_POLYGON);
    glVertex3f (0.4, 0.1, 0.0);
    glVertex3f (0.8, 0.4, 0.0);
    glVertex3f (0.8, 0.75, 0.0);
    glVertex3f (0.4, 0.5, 0.0);
    glEnd();
    glColor3f(0.4,0.0,0.4);

    glBegin(GL_POLYGON);
    glVertex3f (0.4, 0.5, 0.0);
    glVertex3f (0.8, 0.75, 0.0);
    glVertex3f (0.62, 0.93, 0.0);
    glVertex3f (0.25, 0.75, 0.0);
    glEnd();
    glFlush();


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowPosition(50, 100)
    glutInitWindowSize(640, 480)
    glutCreateWindow("Polygon with viewport")
    init()
    glutDisplayFunc(draw)
    glutMainLoop()

main()