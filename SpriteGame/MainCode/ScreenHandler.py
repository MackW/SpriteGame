'''
Created on Jun 8, 2014

@author: mack
'''

import os,sys
import pygame
from pygame.locals import *
from time import time
    
def load_image(name, colorkey=None):
    fullname = os.path.join('', 'Images')
    fullname = os.path.join(fullname, name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', fullname
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image 

def get_colorkey_hitmask(image, rect):
    colorkey=image.get_colorkey()
    mask=[]
    for x in range(rect.width):
        mask.append([])
        for y in range(rect.height):
            mask[x].append(not image.get_at((x,y)) == colorkey)
    return mask

def check_collision(obj1,obj2):
    try:rect1, rect2, hm1, hm2 = obj1.rect, obj2.rect, obj1.hitmask, obj2.hitmask
    except AttributeError:return False
    rect=rect1.clip(rect2)
    if rect.width==0 or rect.height==0:
        return False 
    x1,y1,x2,y2 = rect.x-rect1.x,rect.y-rect1.y,rect.x-rect2.x,rect.y-rect2.y
    for x in xrange(rect.width):
        for y in xrange(rect.height):
            if hm1[x1+x][y1+y] and hm2[x2+x][y2+y]:return True
            else:continue
    return False

def load_tile_table(filename, width, height):
    filename = os.path.join('Images',filename)
    masterimage = pygame.image.load(filename).convert()
    image_width, image_height = masterimage.get_size()
    tile_table = []
    for tile_y in range(0, image_height/height):
        for tile_x in range(0, image_width/width):        
            rect = (tile_x*width, tile_y*height, width, height)
            image=masterimage.subsurface(rect)
            colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, RLEACCEL) 
            tile_table.append(image)
            image=pygame.transform.flip(image,True,False)
            colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, RLEACCEL)
            tile_table.append(image)
    return tile_table

def load_single_image_from_tile(filename, index,width,height):
    filename = os.path.join('Images',filename)
    masterimage = pygame.image.load(filename).convert()
    image_width, image_height = masterimage.get_size()
    amountPerRow=image_width/width
    row=index // amountPerRow
    column=index % amountPerRow
    rect = (column*width, row*height, 32, 32)
    image=masterimage.subsurface(rect)
    return image

def draw_screen(levels,iLevel,xPosition):
    surf=pygame.Surface((1056,768))
    for iY in xrange(0,24):
        for iX in xrange(0,33):
            tmpLvl=levels[iLevel]
            imgDisp = tmpLvl.getImage(iY,iX+(xPosition//32))
            rec=pygame.Rect(iX*32,iY*32,32,32)
            surf.blit(imgDisp,rec)
    return surf
            
def transition(screen,surface1,surface2,duration,FPS):
    step = 255.0/(duration*FPS)
    alpha1 = 0
    alpha2 =255
    clock=pygame.time.Clock()
    last_time = time()
    while time()<last_time+duration:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
        surface1.set_alpha(alpha1)
        surface2.set_alpha(alpha2)
        screen.blit(surface1,surface1.get_rect())
        screen.blit(surface2,surface2.get_rect())
        pygame.display.flip()
        alpha1=alpha1+step
        alpha2=alpha2-step
        clock.tick(FPS)
        
def DrawTextToScreen(screen,fontsize,msg,x,y,colour,overWrite,overWriteColour,useCenter,updatescreen):
    #routine to allow Text to be drawn to the screen
    font = pygame.font.Font(None, fontsize) 
    text = font.render(msg, 1, colour)   
    if useCenter==True:
        textpos = text.get_rect(centerx=x,centery=y)
    else:                            
        textpos = text.get_rect(x=x,y=y)
    if overWrite==True : screen.fill(overWriteColour, textpos)   
    screen.blit(text, textpos)
    if updatescreen==True:
        pygame.display.flip()  
          
def DrawTextToSurface(surface,fontsize,msg,x,y,colour,overWrite,overWriteColour,useCenter):
    #routine to allow Text to be drawn to the screen
    font = pygame.font.Font(None, fontsize) 
    text = font.render(msg, 1, colour)   
    if useCenter==True:
        textpos = text.get_rect(centerx=x,centery=y)
    else:                            
        textpos = text.get_rect(x=x,y=y)
    if overWrite==True : surface.fill(overWriteColour, textpos)   
    surface.blit(text, textpos)
