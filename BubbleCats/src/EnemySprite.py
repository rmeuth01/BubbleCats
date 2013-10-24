'''
Created on Dec 28, 2012

@author: Ryan
'''
import pygame, sys, os
from pygame.locals import *
from ImageUtils import *


class EnemySprite(pygame.sprite.Sprite):
    '''
    classdocs
    '''

    def __init__(self, imgName, w, (x,y), patrolSteps, speed, attackSound,colorKey=None):
        '''
        Constructor
        '''
        pygame.sprite.Sprite.__init__(self) #call Sprite intializer
        self.AnimSet, self.rect = load_sliced_sprites(w, imgName, colorKey)
        self.rect.topleft = (x,y)
        self.patrolSteps = patrolSteps
        self.speed = speed
        self.flip = False
        self.image = self.AnimSet[0]
        self.steps = 0
        self.animCount = 0
        self.velY = 0
        self.updates = 0
        self.type = 0
        self.attackState = 0
        self.attackSound = None
        if attackSound != None:
            self.attackSound = load_sound(attackSound)
        
    def update(self):
        # Update Gravity
        self.velY += 2
        self.updates += 1
        newpos = self.rect.move(0,self.velY)
        if self.speed > 0: # -1 for stationary enemies
            if self.updates % 5 == 0:
                self.animCount += 1
                if self.animCount > len(self.AnimSet)-1:
                    self.animCount = 0
                self.image = self.AnimSet[self.animCount]
                
                self.steps += 1
                if self.steps > self.patrolSteps:
                    self.flip = ~self.flip
                    self.steps = 0
                
                if self.flip:
                    newpos = newpos.move(-self.speed,0)
                    self.image = pygame.transform.flip(self.image, 1,0)
                else:
                    newpos = newpos.move(self.speed, 0)
        else:
            if self.attackState > 0:
                self.attackState -= 1
                self.image = self.AnimSet[1]
            else:
                self.image = self.AnimSet[0]
        self.rect = newpos
    
    def attack(self):
        if self.speed < 0: # Stationary
            self.attackState = 60
            if self.attackSound != None:
                self.attackSound.play()
            
        
    def platformCollide(self, collRect):
        collRect = collRect.inflate(10,-20)
        if self.rect.bottom > collRect.top and self.rect.centery < collRect.top and (self.rect.centerx > collRect.left and self.rect.centerx < collRect.right):
            self.rect.bottom = collRect.top
            self.velY = 0
            return
        
        if self.rect.top > collRect.bottom: # and self.rect.centery > collRect.top and (self.rect.right > collRect.left and self.rect.centerx < collRect.right):
            self.velY = 0
            return
        
        if self.rect.left < collRect.right and self.rect.left > collRect.left and self.rect.bottom > collRect.bottom:
            self.rect.left = collRect.right
            return
            
        if self.rect.right > collRect.left and self.rect.right < collRect.right and self.rect.bottom > collRect.bottom:
            self.rect.right = collRect.left
            return
    
    def setLocation(self, (x,y)):
        self.rect.topleft = (x,y)
        
    def move(self, x, y):
        self.rect = self.rect.move(x,y)