import os
import pygame
from pygame.locals import RLEACCEL
    
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


def draw_screen(levels,iLevel,xPosition):
    surf=pygame.Surface(1056,768)
    surf.set_clip(None)
    for iX in xrange(0,34):
        for iY in xrange(0,25):
            imgDisp = levels[iLevel].getImage[iX+xPosition,iY]
            surf.blit(imgDisp,pygame.Rect(x=iX*32,y=iY*32,width=32,height=32))
    return surf
            
    
    
    
