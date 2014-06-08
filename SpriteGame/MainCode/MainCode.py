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
    def Main(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1024, 768))
        pygame.key.set_repeat(1, 1)
        self.levelsContainer.append(AddLevel0())
        clock=pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()
            surf=draw_screen(self.levelsContainer,0,0)
            self.screen.blit(surf,surf.get_rect())
            pygame.display.flip()
            clock.tick(25)


if __name__ == '__main__':
    MainWindow = ScreenDrawer()
    MainWindow.Main()