# -*- coding: cp1252 -*-
import pygame
from pygame.locals import *
import time
import Tools
#pygame.time.Clock
class Time(object):

    def __init__ (self,time,xr,yr,x,y,z):
        self.time=time
        self.reloj=pygame.time.Clock()
        self.t= self.reloj.tick(50)
        self.counter = 0
        self.counting=True
        self.xr=xr
        self.yr=yr
        self.x=x
        self.y=y
        self.z=z
        self.listaImg=[]#lista que contiene a las imagenes cargadas
        self.listaNum=[]#lista que contiene a los numeros se�alar con imagenes
        self.Clock=Tools.FastMethods.load_image("Screens/imgs/Reloj.png")
        for t in range(0,self.time+1):
            self.listaNum.append(str(t))
        for n in range(0,10):
            num=Tools.FastMethods.load_image("Screens/imgs/t"+str(n)+".png")
            self.listaImg.append(num)
            
    def update(self,pantalla):
        time=self.reloj.get_time()
        self.counter= self.counter+time
        pantalla.blit(self.Clock,(self.xr,self.yr))
        
        if self.counter >= 1000 and not self.time == 0:
            if self.time>=10:
                a=self.listaNum[self.time][0]
                b=self.listaNum[self.time][1]
                pantalla.blit(self.listaImg[int(a)],(self.x,self.y))
                pantalla.blit(self.listaImg[int(b)],(self.z,self.y))
            else:
                a=self.listaNum[self.time]
                pantalla.blit(self.listaImg[0],(self.x,self.y))
                pantalla.blit(self.listaImg[int(a)],(self.z,self.y))
            if self.counting==True:

                self.time-=1
            self.counter=0
        else:
            if self.time >= 10:
                a=self.listaNum[self.time][0]
                b=self.listaNum[self.time][1]
                pantalla.blit(self.listaImg[int(a)],(self.x,self.y))
                pantalla.blit(self.listaImg[int(b)],(self.z,self.y))
            else:
                a=self.listaNum[self.time]
                pantalla.blit(self.listaImg[0],(self.x,self.y))
                pantalla.blit(self.listaImg[int(a)],(self.z,self.y))
                
            if self.time==0:
                pantalla.blit(self.listaImg[0],(self.x,self.y))
                pantalla.blit(self.listaImg[0],(self.z,self.y))

    def Tiempo(self):
        return self.time

    def Reset(self,temp=90):
        self.time=temp
        self.counting=True
        self.counter=0

        

    def detener(self):
        self.counting=False

