'''
Created on Dec 28, 2012

@author: Ryan
'''
import pygame, sys, os
from pygame.locals import *
from ImageUtils import *


class SceneSprite(pygame.sprite.Sprite):
    '''
    classdocs
    '''

    def __init__(self, imgName, (x,y), colorKey=None):
        '''
        Constructor
        '''
        pygame.sprite.Sprite.__init__(self) #call Sprite intializer
        self.image, self.rect = load_image(imgName, colorKey)
        self.rect.topleft = (x,y)
    
    def setLocation(self, (x,y)):
        self.rect.topleft = (x,y)
        
    def move(self, x, y):
        self.rect = self.rect.move(x,y)