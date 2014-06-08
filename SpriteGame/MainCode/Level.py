'''
Created on Jun 8, 2014

@author: mack
'''
class Level(object):
    lvlMap = []
    images = []
    xSize =0
    xPosition=0
    #def __init__(self):
    def getImage(self,iX,iY):
        return self.images[self.lvlMap[iX][iY]]
    
    def addImageByFileName(self,imgName):
        self.images.append(load_image('Brick-red.png',-1))

    def addImage(self,img):
        self.images.append(img)