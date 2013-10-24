'''
Created on Dec 28, 2012

@author: Ryan
'''
import pygame, sys, os
from pygame.locals import *

def load_sound(name):
    fullname = os.path.join('..','data', name)
    return pygame.mixer.Sound(fullname)

def load_image(name, colorkey=None):
    fullname = os.path.join('..','data', name)
    try:
        image = pygame.image.load(fullname).convert()
    except pygame.error, message:
        print "Cannot load image:", name
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

def load_sliced_sprites( w, filename, colorkey = None):
    '''
    Specs :
        Master can be any height.
        Sprites frames width must be the same width
        Master width must be len(frames)*frame.width
    '''
    images = []
    master_image = pygame.image.load(os.path.join('..', 'data', filename)).convert()
    master_image.set_colorkey(colorkey, RLEACCEL)
    master_width, h = master_image.get_size()
    for i in xrange(int(master_width/w)):
        images.append(master_image.subsurface((i*w,0,w,h)))
    return images, images[0].get_rect()