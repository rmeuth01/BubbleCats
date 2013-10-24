'''
Created on Dec 28, 2012

@author: Ryan
'''

import pygame, sys, os
from pygame.locals import *
from ImageUtils import *

class GameEngine():
    '''
    classdocs
    '''
    def __init__(self, (w,h), title, refreshRate):
        '''
        Constructor
        '''
        pygame.mixer.pre_init(22050, -16, 2, 2048) # setup mixer to avoid sound lag
        pygame.init()
        self.window = pygame.display.set_mode((w,h))
        pygame.display.set_caption(title)
        self.screen = pygame.display.get_surface()
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 30)
        self.refreshRate = refreshRate
        self.allsprites = pygame.sprite.OrderedUpdates()
        self.backgroundSprites = pygame.sprite.RenderPlain()
        self.platformSprites = pygame.sprite.RenderPlain()
        self.playerGroup = pygame.sprite.RenderPlain()
        self.enemyGroup = pygame.sprite.RenderPlain()
        self.itemGroup = pygame.sprite.RenderPlain()
        self.screenRect = self.screen.get_rect()
        self.healthImage, self.healthRect = load_image("Heart.bmp", pygame.Color(0,0,0))
        self.winImage, self.WinRect = load_image("YouWin.bmp", pygame.Color(131,131,131))
        self.endScreenCount = 500
        
    def addPlayer(self, playerSprite):
        self.player = playerSprite
        self.playerGroup.add(self.player)
        
    def addBackground(self, backgroundSprite):
        self.backgroundSprites.add(backgroundSprite)
        self.allsprites.add(backgroundSprite)
    
    def addPlatform(self, platformSprite):
        self.platformSprites.add(platformSprite)
        self.allsprites.add(platformSprite)
    
    def addEnemy(self, enemySprite):
        self.enemyGroup.add(enemySprite)
        self.allsprites.add(enemySprite)
        
    def addItem(self, itemSprite):
        self.itemGroup.add(itemSprite)
        self.allsprites.add(itemSprite)
        
    def playerPlatformColl(self):
        collList = pygame.sprite.spritecollide(self.player, self.platformSprites, False)
        for sprite in collList:
            self.player.platformCollide(sprite.rect)
            
    def playerItemColl(self):
        collList = pygame.sprite.spritecollide(self.player, self.itemGroup, False)
        for sprite in collList:
            self.player.itemCollide(sprite)
            self.itemGroup.remove(sprite)
            self.allsprites.remove(sprite)
            
    def playerEnemyColl(self):
        collList = pygame.sprite.spritecollide(self.player, self.enemyGroup, False)
        for sprite in collList:
            self.player.enemyCollide(sprite)
    
    def enemyPlatformColl(self):
        collDict = pygame.sprite.groupcollide(self.enemyGroup, self.platformSprites, False, False)
        for sprite in collDict.keys():
            for collPlat in collDict[sprite]:
                sprite.platformCollide(collPlat.rect)
                
    def drawHUD(self):
        # Points
        text = self.font.render("Score:", 1, (0,0,0) )
        textpos = text.get_rect(topleft=(10,10))
        self.screen.blit(text, textpos)
        text = self.font.render(str(self.player.score), 1, (0,0,0))
        textpos = text.get_rect(topright=(200,10))
        self.screen.blit(text,textpos)
        
        # Lives
        for i in range(self.player.lives):
            self.screen.blit(self.healthImage, (self.screenRect.width-((i+1)*(self.healthRect.width+5))-5, 10))
            
    def hasLost(self):
        if self.player.lives > 0:
            return False
        return True

    def hasWon(self):
        return self.player.reachedGoal
    
    def loadBackgroundMusic(self, filename):
        fullname = os.path.join('..','data', filename)
        pygame.mixer.music.load(fullname)
        pygame.mixer.music.play(-1)
        
    def update(self):
        self.clock.tick(40)
        
        
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                sys.exit()
            self.player.control(event) 
         
        sceneOffset = self.player.update(self.screenRect.inflate(-(self.screenRect.width-250),0))
        if sceneOffset != 0:
            for sprite in self.platformSprites:
                sprite.move(sceneOffset, 0)
            for sprite in self.enemyGroup:
                sprite.move(sceneOffset, 0)
            for sprite in self.itemGroup:
                sprite.move(sceneOffset, 0)
            for sprite in self.backgroundSprites:
                sprite.move(sceneOffset, 0)
        
        if self.player.lives > 0:
            self.playerPlatformColl()
            self.playerItemColl()
            self.playerEnemyColl()
        else:
            if self.player.rect.top > self.screenRect.height:
                return False

        self.enemyPlatformColl()
        self.allsprites.update()
        self.screen.fill(pygame.Color(223,183,103))
        self.allsprites.draw(self.screen)
        self.playerGroup.draw(self.screen)
        self.drawHUD()
        
        if self.player.reachedGoal:
            self.screen.blit(self.winImage, (200,75))
            self.endScreenCount -= 1
            
        pygame.display.flip()
        
        if self.endScreenCount < 1:
            return False
        return True
    
    def quit(self):
        pygame.quit()
    