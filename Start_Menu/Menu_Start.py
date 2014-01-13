import pygame
from pygame.locals import *
import sys
import time
import random
screen_w = 1024
screen_h = 768

def main():
    pygame.mixer.init()
    pygame.mixer.music.load("BGM_0002.mp3")
    pygame.mixer.music.play(-1)
    
    pygame.init()
    estado_pj1 = 0
    estado_pj2 = 0
    ID_pj1 = False
    ID_pj2 = False
    screen = pygame.display.set_mode((screen_w,screen_h))
    v = 0
    pygame.display.set_caption("Course_Wars")
    Fondo={}
    Fondo[0]=("Fondo_Start1.jpg")
    Fondo[1]=("Fondo_Start2.jpg")     
        
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if pygame.key.get_pressed()[K_RETURN]:
                    estado_pj1 = 1
                    ID_pj1 = True
                if pygame.key.get_pressed()[K_TAB]:
                    estado_pj2 = 1
                    ID_pj2 = True
                if pygame.key.get_pressed()[K_ESCAPE]:
                    pygame.quit()
                    sys.exit()
                    
        if estado_pj1 == 1 or estado_pj2 == 1:
            return [ID_pj1,ID_pj2]
                   
        fondo=pygame.image.load(Fondo[v]).convert()
        screen.blit((fondo),(0,0))
        pygame.display.flip()        
        v+=1        
        if v == 2:
            v = 0
        
        time.sleep(1)
            
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()            
                
if __name__== "__main__":
    main()
             