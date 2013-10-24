'''
Created on Dec 28, 2012

@author: Ryan
'''
import pygame, sys, os
from pygame.locals import *
from ImageUtils import *


class ItemSprite(pygame.sprite.Sprite):
    '''
    classdocs
    '''

    def __init__(self, imgName, width, (x,y), updateSpeed, itemType, colorKey=None):
        '''
        Constructor
        '''
        pygame.sprite.Sprite.__init__(self) #call Sprite intializer
        self.AnimSet, self.rect = load_sliced_sprites(width, imgName, colorKey)
        self.image = self.AnimSet[0]
        self.rect.topleft = (x,y)
        self.type = itemType  # Default: Extra Life
        self.animCount = 0
        self.updates = 0
        self.updateSpeed = updateSpeed
    
    def setLocation(self, (x,y)):
        self.rect.topleft = (x,y)
        
    def move(self, x, y):
        self.rect = self.rect.move(x,y)
    
    def setType(self, itemType):
        self.type = itemType # 0 - Extra Life, 1 - Bubble
    
    def update(self):
        self.updates += 1
        if self.updates % self.updateSpeed == 0:
            self.animCount += 1
            if self.animCount > len(self.AnimSet)-1:
                self.animCount = 0
            self.image = self.AnimSet[self.animCount]