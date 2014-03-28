import pygame
from pygame.locals import *
import sys
import time
import random
import Sound
screen_w = 1024
screen_h = 768

def main():
    pygame.mixer.init(frequency= 22050, size=-16, channels=2, buffer=64)
    pygame.mixer.music.load("bgm/Title.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.3)

    
    pygame.init()
    pygame.mouse.set_visible(False)
    estado_pj1 = 0
    estado_pj2 = 0
    ID_pj1 = False
    ID_pj2 = False
    contador = 0
    screen = pygame.display.set_mode((screen_w,screen_h),FULLSCREEN)
    #screen = pygame.display.set_mode((screen_w,screen_h))
    v = 0
    pygame.display.set_caption("Course_Wars")
    Fondo={}
    Fondo[0]=("screens/start_menu/Fondo_Start1.jpg")
    Fondo[1]=("screens/start_menu/Fondo_Start2.jpg")     
    Salida = False 
    while Salida==False:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    estado_pj1 = 1
                    ID_pj1 = True
                    #print "precionado enter"
                    Salida=True
                if event.key == K_SPACE:
                    estado_pj2 = 1
                    ID_pj2 = True
                    #print "precionado tab"
                    Salida=True
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                    

        contador +=1
        if contador == 10:
            v+=1
            if v == 2:
                v = 0
            contador = 0
                   
        fondo=pygame.image.load(Fondo[v]).convert()
        screen.blit((fondo),(0,0))
        pygame.display.flip()
        #print(v)
        #print(contador)
       
        #time.sleep(1)
            
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()           
    if estado_pj1 == 1 or estado_pj2 == 1:
        #print "saliendo"

        #pygame.quit()
        Sound.soundPlayer.simpleplay("sfx/explode2.wav")

        return [ID_pj1,ID_pj2]

if __name__== "__main__":
    main()
             