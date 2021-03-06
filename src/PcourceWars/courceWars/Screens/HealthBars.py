#!/usr/bin/python
# -*- coding: latin-1 -*-
"""m�dulo que representa a las barras de vida de cada uno de los personajes"""

import sys, pygame

width, height = 1024, 768
blue=(0,0,255)
red=(255,0,0)
yellow=(255,255,0)
grey=(150,150,150)
black=(0,0,0)

class HP_Bar(object):
    
    def __init__(self, Screen, NumJug):
        self.screen = Screen
        self.numJug = NumJug
    
    def draw(self, vida):
        if(vida<=25):
            color=red
        else:
            if(vida<=50):
                color=yellow
            else:
                color=blue
            
        if(self.numJug == 1):
            pygame.draw.rect(self.screen,black,(27,28,407,34),0)
            pygame.draw.rect(self.screen,black,(227,58,207,16),0)
            pygame.draw.rect(self.screen,grey,(30,30,400,30),0)
            pygame.draw.rect(self.screen,color,(430,30,-vida*4,30),0)
        else:
            pygame.draw.rect(self.screen,black,(width - 432,28,405,34),0)
            pygame.draw.rect(self.screen,black,(width - 432,58,205,16),0)
            pygame.draw.rect(self.screen,grey,(width - 430,30,400,30),0)
            pygame.draw.rect(self.screen,color,(width - 430,30,vida*4,30),0)
