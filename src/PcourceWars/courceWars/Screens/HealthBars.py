import sys, pygame

width, height = 1024, 450
blue=(0,0,255)
red=(255,0,0)
yellow=(255,255,0)
grey=(92,92,92)

class HP_Bar(object):
    
    def __init__(self, Screen, NumJug):
        self.screen = Screen
        self.numJug = NumJug
    
    def draw(self, vida):
        if(vida<25):
            color=red
        else:
            if(vida<25):
                color=yellow
            else:
                color=blue
            
        if(self.numJug == 1):
            pygame.draw.rect(self.screen,grey,(30,30,400,30),0)
            pygame.draw.rect(self.screen,color,(30,30,vida*4,30),0)
        else:
            pygame.draw.rect(self.screen,grey,(width - 30,30,-400,30),0)
            pygame.draw.rect(self.screen,color,(width - 30,30,-vida*4,30),0)