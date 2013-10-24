'''
Created on Dec 28, 2012

@author: Ryan
'''
import pygame, sys, os, random
from pygame.locals import *
from ImageUtils import *

STOP = 0
LEFT = 1
RIGHT = 2
JUMP_HOLD = 3
JUMP = 4

class Cat(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #call Sprite intializer
        self.AnimSet, self.rect = load_sliced_sprites(155,'Duke.bmp', pygame.Color(0,255,0))
        self.image = self.AnimSet[0]
        self.rect.topleft = 500, 100
        self.failImage, self.failRect = load_image("FallingCat.bmp", pygame.Color(0,255,0))
        self.meowSounds = []
        self.bubbleSounds = []
        self.hurtSounds = []
        self.purrSound = None
        self.oneupSound = None
        self.velY = 0
        self.flip = False
        self.AnimCount = 0
        self.moveState = STOP
        self.lastMoveState = STOP
        self.jumpState = STOP
        self.jumping = False
        self.jumpStrength = 10
        self.lives = 5
        self.recovery = 0
        self.score = 0
        self.reachedGoal = False
        
        self.meowSounds.append(load_sound("meow1.wav"))
        self.meowSounds.append(load_sound("meow2.wav"))
        self.meowSounds.append(load_sound("meow3.wav"))
        self.meowSounds.append(load_sound("meow4.wav"))
        self.bubbleSounds.append(load_sound("Pop0.wav"))
        self.bubbleSounds.append(load_sound("Pop1.wav"))
        self.bubbleSounds.append(load_sound("Pop2.wav"))
        self.bubbleSounds.append(load_sound("Pop3.wav"))
        self.bubbleSounds.append(load_sound("Pop4.wav"))
        self.bubbleSounds.append(load_sound("Pop5.wav"))
        self.bubbleSounds.append(load_sound("Pop6.wav"))
        self.bubbleSounds.append(load_sound("Pop7.wav"))
        self.bubbleSounds.append(load_sound("Pop8.wav"))
        self.bubbleSounds.append(load_sound("Pop9.wav"))
        self.bubbleSounds.append(load_sound("Pop10.wav"))
        self.bubbleSounds.append(load_sound("Pop11.wav"))
        self.bubbleSounds.append(load_sound("Pop12.wav"))
        self.bubbleSounds.append(load_sound("Pop13.wav"))
        self.bubbleSounds.append(load_sound("Pop14.wav"))
        self.hurtSound = load_sound("AngryCat.wav")

        self.oneupSound = load_sound("OneUp.wav")
        self.purrSound = load_sound("purr5.wav")
        

    def update(self, viewRect):
        if self.reachedGoal:
            return 0
        # Update Gravity
        self.velY += 2
        
        # Update recovery
        if self.recovery > 0:
            self.recovery -= 1
            if self.recovery == 0:
                for img in self.AnimSet:
                    img.set_alpha(255)

    
        # Update Animations
        if self.moveState == RIGHT or self.moveState == LEFT:
            self.AnimCount += 1
            if self.AnimCount >= 8:
                self.AnimCount = 0
        
        moveX = 0
        if self.moveState == RIGHT and self.jumpState != JUMP_HOLD:
            if self.jumping:
                moveX = 20
            else:
                moveX = 10
            self.flip = False
            
        if self.moveState == LEFT and self.jumpState != JUMP_HOLD:
            if self.jumping:
                moveX = -20
            else:
                moveX = -10
            self.flip = True
        
        if self.jumpState == JUMP:
            moveX = 0
            self.velY = -self.jumpStrength
            self.jumping = True
            self.jumpState = STOP
            self.jumpStrength = 10
        
        newpos = self.rect.move((moveX, self.velY))
        
        # Viewport Collision
        backgroundOffset = 0
        if newpos.left < viewRect.left:
            backgroundOffset = viewRect.left - newpos.left
            newpos.left = viewRect.left
        
        if newpos.right > viewRect.right:
            backgroundOffset = viewRect.right - newpos.right
            newpos.right = viewRect.right

        self.rect = newpos
        
        if self.jumpState == JUMP_HOLD:
            self.image = self.AnimSet[8]
            self.jumpStrength += 1
            if self.jumpStrength > 40:
                self.jumpStrength = 40
        else:
            self.image = self.AnimSet[self.AnimCount]

        if self.velY < 0:
            self.image = self.AnimSet[9]
        if self.velY > 2:
            self.image = self.AnimSet[10]
            self.AnimCount = 7
        
        if self.flip:
            self.image = pygame.transform.flip(self.image, 1,0)
            
        if self.lives < 1:
            self.image = self.failImage

        return backgroundOffset
    
    def platformCollide(self, collRect):
        collRect = collRect.inflate(10,-20)
        if self.rect.bottom > collRect.top and self.rect.centery < collRect.top and (self.rect.centerx > collRect.left and self.rect.centerx < collRect.right):
            self.rect.bottom = collRect.top
            self.velY = 0
            self.jumping = False
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
            
    def itemCollide(self, item):
        if item.type == 0: # Heart
            self.lives+=1
            self.oneupSound.play()
        if item.type == 1: # Bubble
            self.score += 100
            random.choice(self.bubbleSounds).play()
        if item.type == 2: # Goal
            self.score += 1000
            self.purrSound.play(5)
            self.reachedGoal = True
            self.rect.left = item.rect.left-25
            self.rect.bottom = item.rect.bottom+20
            self.image = self.AnimSet[8]
            
    def enemyCollide(self, enemy):
        if self.recovery == 0:
            enemy.attack()
            if enemy.type == 0: # Scorpion
                self.lives-=1
            self.velY = -20
            
            if self.lives < 1:
                self.velY = -40
                
            self.recovery = 60
            for img in self.AnimSet:
                img.set_alpha(100)
            self.hurtSound.play()
            
            
    def control(self, keyEvent):
        actionKeys = [K_LEFT, K_RIGHT, K_SPACE]
        if self.reachedGoal:
            return
        
        if keyEvent.type == KEYDOWN and keyEvent.key in actionKeys:
            if self.moveState != STOP:
                self.lastMoveState = self.moveState
            if keyEvent.key == K_RIGHT:
                self.moveState = RIGHT
            elif keyEvent.key == K_LEFT:
                self.moveState = LEFT
            elif keyEvent.key == K_SPACE:
                if not self.jumping:
                    self.jumpState = JUMP_HOLD
            else:
                self.moveState = STOP

        if keyEvent.type == KEYUP and keyEvent.key in actionKeys:
            if keyEvent.key == K_SPACE:
                if not self.jumping:
                    self.jumpState = JUMP
            else:
                self.moveState = STOP