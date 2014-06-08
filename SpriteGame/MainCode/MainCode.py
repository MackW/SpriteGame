'''
Created on Jun 8, 2014

@author: mack
'''
import random,math,sys,pygame
from pygame.locals import *
from ScreenHandler import *
from Level0 import *

class ScreenDrawer:
    levelsContainer=[]
    iCurrentLevel=0
    xPosition=0
    scrollSpeed=4  #pixels per movement
    FPS=50
    def Main(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1024, 768))
        pygame.key.set_repeat(1, 1)
        self.levelsContainer.append(AddLevel0())
        clock=pygame.time.Clock()
        surf=pygame.Surface((1024,768))
        DrawTextToSurface(surf,72,'Looks Like you need a kip dude',512,384,(255,255,255),False,0,True)
        self.screen.blit(surf,surf.get_rect())
        surfGame=draw_screen(self.levelsContainer,self.iCurrentLevel,self.xPosition)
        transition(self.screen,surfGame,surf,5,self.FPS)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        if self.xPosition>0:
                            self.xPosition=self.xPosition -self.scrollSpeed
                    if event.key == K_RIGHT:   
                        if self.xPosition<self.levelsContainer[self.iCurrentLevel].xSize:
                            self.xPosition=self.xPosition +self.scrollSpeed
            surf=draw_screen(self.levelsContainer,self.iCurrentLevel,self.xPosition)
            rct=surf.get_rect()
            rct.left=-(self.xPosition%32)
            self.screen.blit(surf,rct)
            pygame.display.flip()
            clock.tick(self.FPS)


if __name__ == '__main__':
    MainWindow = ScreenDrawer()
    MainWindow.Main()