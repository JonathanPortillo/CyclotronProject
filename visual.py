import pygame
import time
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )


class Read:
        def __init__(self, filename):
            self.filename = filename 
            self.x_list = None
            self.y_list = None
            self.z_list = None
        def read(self):
            f = open(self.filename, 'r')
            data = f.read()
            split_data = data.split('\n')
            #x data
            split_data[0] = split_data[0][1:-1]
            #y data
            split_data[1] = split_data[1][1:-1]
            #z data
            split_data[2] = split_data[2][1:-1] 

            #x data in list char numbers
            split_data[0] = split_data[0].split(", ")
            #y data in list char numbers
            split_data[1] = split_data[1].split(", ")
            #z data in list char numbers
            split_data[2] = split_data[2].split(", ")

            #x data in floats
            split_data[0] = [float(x) for x in split_data[0]]
            #y data in floats
            split_data[1] = [float(y) for y in split_data[1]]
            #x data in floats
            split_data[2] = [float(z) for z in split_data[2]]

            self.x_list = split_data[0]
            self.y_list = split_data[1]
            self.z_list = split_data[2]
            f.close()
def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()


def Cyclic_Motion():
	glPointSize(1.0)
	glClearColor(0.0, 0.0, 0.0, 1.0)
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1.0, 1.0, 1.0)
	glBegin(GL_POINTS)
	glVertex2f(100, 150)
	glEnd()

def Particle_Projectile_Motion_Display(x_list, y_list):
    #glBegin(GL_LINE_LOOP)
    glBegin(GL_POINTS)
    for i in range(len(x_list)):
         glVertex2f(x_list[i], y_list[i])
    glEnd()

def main():

    pygame.init()
    
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    #read coorindate
    data = Read("pos.json")
    data.read()
    #gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    current_img_x = []
    current_img_y = []
    index = 0
    log_increase_coeff = 2
    while index < len(data.x_list):
        current_img_x = data.x_list[0:index]
        current_img_y = data.y_list[0:index]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        Particle_Projectile_Motion_Display(current_img_x, current_img_y)
        time.sleep(1/log_increase_coeff)
        log_increase_coeff +=1
        pygame.display.flip()
        index +=1


        #glRotatef(1, 3, 1, 1)
        # glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        # #Cube()
        # glBegin(GL_TRIANGLES);
        # glVertex2f( -0.7, -0.5 );
        # glVertex2f( 0.7, -0.5 );
        # glVertex2f( 0, 0.7 );
        # glEnd();

        #plots the points
        #Cyclic_Motion()
        #updates the screen
        # pygame.display.flip()
        # #waits for the screen response
        # pygame.time.wait(10)


main()