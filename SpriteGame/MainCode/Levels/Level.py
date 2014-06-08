from Helpers import *

class Level(object):
    lvlMap = []
    images = []
    xSize =0
    xPosition=0
    #def __init__(self):
    def getImage(self,iX,iY):
        return self.images[self.lvlMap[iX][iY]]
    
    def addImage(self,imgName):
        self.images.append(load_image('Brick-red.png',-1))