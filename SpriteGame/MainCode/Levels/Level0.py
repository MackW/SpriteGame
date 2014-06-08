'''
Created on Jun 8, 2014

@author: mack
'''
from Level import *

def AddLevel(Levels):
    lclLevel = Level
    lclLevel.lvlMap=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    lclLevel.addImage(imgName)
    Levels.add(lclLevel)