'''
Created on Dec 28, 2012

@author: Ryan
TODO: 
Player Choice
Level Read
Level Editor
Finish Cat Art
'''

import pygame, sys, os
from pygame.locals import *
from GameEngine import *
from CatPlayer import *
from SceneSprite import *
from EnemySprite import *
from ItemSprite import *



bubbleCats = GameEngine((800,600), "BubbleCats", 40)

screenHeight = bubbleCats.screenRect.height
for i in range(220):
    sprite = SceneSprite("CarpetTile.bmp", (0, 0), None)
    sprite.move(i*sprite.rect.width-150, screenHeight-sprite.rect.height)
    bubbleCats.addPlatform(sprite)
    sprite = SceneSprite("RunningBoardTile.bmp", (0,0), None)
    sprite.move(i*sprite.rect.width-150, screenHeight-94)
    bubbleCats.addBackground(sprite)
    
for i in range(15):
    bubbleCats.addBackground(SceneSprite("OutletTile.bmp", (i*1000, screenHeight-170)))

bubbleCats.addBackground(SceneSprite("CouchTop.bmp", (14000, 281), pygame.Color(131,131,131)))
bubbleCats.addBackground(SceneSprite("BethGoalTop.bmp", (14220, 195), pygame.Color(131,131,131)))

bubbleCats.addPlatform(SceneSprite("CouchBase.bmp", (14000, 410), pygame.Color(131,131,131))) # Base
bubbleCats.addPlatform(SceneSprite("BethGoal.bmp", (14220, 370), pygame.Color(131,131,131)))  # Offset 220
bubbleCats.addItem(ItemSprite("Trigger.bmp", 100, (14245, 260), 5, 2, pygame.Color(131,131,131))) # Offset 245

# Intro 
bubbleCats.addPlatform(SceneSprite("TableTopL.bmp", (900, 300), pygame.Color(131,131,131)))
bubbleCats.addPlatform(SceneSprite("TableTopMid.bmp", (980, 300),pygame.Color(131,131,131)))
bubbleCats.addPlatform(SceneSprite("TableTopR.bmp", (1060, 300),pygame.Color(131,131,131)))

bubbleCats.addEnemy(EnemySprite("Scorpion.bmp", 100, (1000,screenHeight-150), 20, 10, None, pygame.Color(130,130,130)))
bubbleCats.addItem(ItemSprite("Heart.bmp", 26, (1300,450), 5, 0, pygame.Color(0,0,0)))
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (980, 200), 5, 1, pygame.Color(255,255,255)))

# First Bubble Run
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (1600, 450), 5, 1, pygame.Color(255,255,255)))
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (1700, 450), 5, 1, pygame.Color(255,255,255)))
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (1800, 450), 5, 1, pygame.Color(255,255,255)))
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (1900, 450), 5, 1, pygame.Color(255,255,255)))

# First Trap
bubbleCats.addPlatform(SceneSprite("TableTopL.bmp", (2100, 250), pygame.Color(131,131,131)))
bubbleCats.addPlatform(SceneSprite("TableTopR.bmp", (2180, 250),pygame.Color(131,131,131)))

bubbleCats.addPlatform(SceneSprite("TableTopL.bmp", (2500, 250), pygame.Color(131,131,131)))
bubbleCats.addPlatform(SceneSprite("TableTopR.bmp", (2580, 250),pygame.Color(131,131,131)))

bubbleCats.addEnemy(EnemySprite("Scorpion.bmp", 100, (2000,screenHeight-150), 30, 15, None, pygame.Color(130,130,130)))
bubbleCats.addEnemy(EnemySprite("Scorpion.bmp", 100, (2500,screenHeight-150), 30, 15, None, pygame.Color(130,130,130)))

bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (2120, 120), 5, 1, pygame.Color(255,255,255)))
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (2520, 120), 5, 1, pygame.Color(255,255,255)))
bubbleCats.addItem(ItemSprite("Heart.bmp", 26, (2370,100), 5, 0, pygame.Color(0,0,0)))

# Scorpion Bubble Run
bubbleCats.addEnemy(EnemySprite("Scorpion.bmp", 100, (3300,screenHeight-150), 20, 10, None, pygame.Color(130,130,130)))
bubbleCats.addEnemy(EnemySprite("Scorpion.bmp", 100, (3900,screenHeight-150), 20, 10, None, pygame.Color(130,130,130)))
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (3200, 450), 5, 1, pygame.Color(255,255,255)))
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (3300, 450), 5, 1, pygame.Color(255,255,255)))
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (3400, 450), 5, 1, pygame.Color(255,255,255)))
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (3500, 450), 5, 1, pygame.Color(255,255,255)))
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (3600, 450), 5, 1, pygame.Color(255,255,255)))
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (3700, 450), 5, 1, pygame.Color(255,255,255)))
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (3800, 450), 5, 1, pygame.Color(255,255,255)))
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (3900, 450), 5, 1, pygame.Color(255,255,255)))
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (4000, 450), 5, 1, pygame.Color(255,255,255)))
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (4100, 450), 5, 1, pygame.Color(255,255,255)))
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (4200, 450), 5, 1, pygame.Color(255,255,255)))

# Sentry Intro
bubbleCats.addPlatform(SceneSprite("TableTopL.bmp", (4600, 300), pygame.Color(131,131,131)))
bubbleCats.addPlatform(SceneSprite("TableTopMid.bmp", (4680, 300),pygame.Color(131,131,131)))
bubbleCats.addPlatform(SceneSprite("TableTopMid.bmp", (4760, 300),pygame.Color(131,131,131)))
bubbleCats.addPlatform(SceneSprite("TableTopMid.bmp", (4840, 300),pygame.Color(131,131,131)))
bubbleCats.addPlatform(SceneSprite("TableTopR.bmp", (4920, 300),pygame.Color(131,131,131)))
bubbleCats.addEnemy(EnemySprite("SpraySentry.bmp", 300, (4610,150), 0, -1, "SpraySentry.wav", pygame.Color(131,131,131)))
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (4750, 200), 5, 1, pygame.Color(255,255,255)))
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (4850, 200), 5, 1, pygame.Color(255,255,255)))

# Bubble Pyramid
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (5300, 325), 5, 1, pygame.Color(255,255,255)))
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (5400, 325), 5, 1, pygame.Color(255,255,255)))
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (5500, 325), 5, 1, pygame.Color(255,255,255)))
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (5600, 325), 5, 1, pygame.Color(255,255,255)))
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (5700, 325), 5, 1, pygame.Color(255,255,255)))


bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (5350, 225), 5, 1, pygame.Color(255,255,255)))
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (5450, 225), 5, 1, pygame.Color(255,255,255)))
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (5550, 225), 5, 1, pygame.Color(255,255,255)))
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (5650, 225), 5, 1, pygame.Color(255,255,255)))

bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (5400, 125), 5, 1, pygame.Color(255,255,255)))
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (5500, 125), 5, 1, pygame.Color(255,255,255)))
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (5600, 125), 5, 1, pygame.Color(255,255,255)))

bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (5450, 25), 5, 1, pygame.Color(255,255,255)))
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (5550, 25), 5, 1, pygame.Color(255,255,255)))

bubbleCats.addItem(ItemSprite("Heart.bmp", 26, (5535,10), 5, 0, pygame.Color(0,0,0)))

# Sentry Trap

bubbleCats.addPlatform(SceneSprite("TableTopL.bmp", (6100, 250), pygame.Color(131,131,131)))
bubbleCats.addPlatform(SceneSprite("TableTopR.bmp", (6180, 250),pygame.Color(131,131,131)))
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (6130, 170), 5, 1, pygame.Color(255,255,255)))

bubbleCats.addPlatform(SceneSprite("TableTopL.bmp", (6620, 250), pygame.Color(131,131,131)))
bubbleCats.addPlatform(SceneSprite("TableTopR.bmp", (6700, 250),pygame.Color(131,131,131)))
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (6650, 170), 5, 1, pygame.Color(255,255,255)))

bubbleCats.addPlatform(SceneSprite("TableTopL.bmp", (6300, 375), pygame.Color(131,131,131)))
bubbleCats.addPlatform(SceneSprite("TableTopMid.bmp", (6380, 375),pygame.Color(131,131,131)))
bubbleCats.addPlatform(SceneSprite("TableTopMid.bmp", (6360, 375),pygame.Color(131,131,131)))
bubbleCats.addPlatform(SceneSprite("TableTopMid.bmp", (6440, 375),pygame.Color(131,131,131)))
bubbleCats.addPlatform(SceneSprite("TableTopR.bmp", (6520, 375),pygame.Color(131,131,131)))
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (6300, 100), 5, 1, pygame.Color(255,255,255)))
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (6400, 75), 5, 1, pygame.Color(255,255,255)))
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (6500, 100), 5, 1, pygame.Color(255,255,255)))

bubbleCats.addEnemy(EnemySprite("SpraySentry.bmp", 300, (6310,300), 0, -1, "SpraySentry.wav", pygame.Color(131,131,131)))
bubbleCats.addEnemy(EnemySprite("Scorpion.bmp", 100, (6310,screenHeight-150), 20, 10, None, pygame.Color(130,130,130)))

# Scorpion Slolam
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (7000, 450), 5, 1, pygame.Color(255,255,255)))
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (7100, 450), 5, 1, pygame.Color(255,255,255)))
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (7200, 450), 5, 1, pygame.Color(255,255,255)))
bubbleCats.addEnemy(EnemySprite("Scorpion.bmp", 100, (7300,screenHeight-150), 20, 10, None, pygame.Color(130,130,130)))
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (7600, 450), 5, 1, pygame.Color(255,255,255)))
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (7700, 450), 5, 1, pygame.Color(255,255,255)))
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (7800, 450), 5, 1, pygame.Color(255,255,255)))
bubbleCats.addEnemy(EnemySprite("Scorpion.bmp", 100, (7900,screenHeight-150), 20, 10, None, pygame.Color(130,130,130)))
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (8200, 450), 5, 1, pygame.Color(255,255,255)))
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (8300, 450), 5, 1, pygame.Color(255,255,255)))
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (8400, 450), 5, 1, pygame.Color(255,255,255)))
bubbleCats.addEnemy(EnemySprite("Scorpion.bmp", 100, (8500,screenHeight-150), 20, 10, None, pygame.Color(130,130,130)))
bubbleCats.addPlatform(SceneSprite("TableTopL.bmp", (8570, 250), pygame.Color(131,131,131)))
bubbleCats.addPlatform(SceneSprite("TableTopR.bmp", (8650, 250),pygame.Color(131,131,131)))
bubbleCats.addItem(ItemSprite("Heart.bmp", 26, (8637,230), 5, 0, pygame.Color(0,0,0)))
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (8800, 450), 5, 1, pygame.Color(255,255,255)))
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (8900, 450), 5, 1, pygame.Color(255,255,255)))
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (9000, 450), 5, 1, pygame.Color(255,255,255)))
bubbleCats.addEnemy(EnemySprite("Scorpion.bmp", 100, (9100,screenHeight-150), 20, 10, None, pygame.Color(130,130,130)))
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (9400, 450), 5, 1, pygame.Color(255,255,255)))
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (9500, 450), 5, 1, pygame.Color(255,255,255)))
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (9600, 450), 5, 1, pygame.Color(255,255,255)))

# Scorpions Everywhere
bubbleCats.addEnemy(EnemySprite("Scorpion.bmp", 100, (10000,screenHeight-150), 20, 10, None, pygame.Color(130,130,130)))
bubbleCats.addPlatform(SceneSprite("TableTopL.bmp", (10100, 250), pygame.Color(131,131,131)))
bubbleCats.addPlatform(SceneSprite("TableTopR.bmp", (10180, 250), pygame.Color(131,131,131)))
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (10130, 170), 5, 1, pygame.Color(255,255,255)))

bubbleCats.addEnemy(EnemySprite("Scorpion.bmp", 100, (10300,screenHeight-150), 20, 10, None, pygame.Color(130,130,130)))
bubbleCats.addPlatform(SceneSprite("TableTopL.bmp", (10500, 250), pygame.Color(131,131,131)))
bubbleCats.addPlatform(SceneSprite("TableTopR.bmp", (10580, 250), pygame.Color(131,131,131)))
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (10530, 170), 5, 1, pygame.Color(255,255,255)))

bubbleCats.addEnemy(EnemySprite("Scorpion.bmp", 100, (10600,screenHeight-150), 20, 10, None, pygame.Color(130,130,130)))
bubbleCats.addPlatform(SceneSprite("TableTopL.bmp", (10900, 250), pygame.Color(131,131,131)))
bubbleCats.addPlatform(SceneSprite("TableTopR.bmp", (10980, 250), pygame.Color(131,131,131)))
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (10930, 170), 5, 1, pygame.Color(255,255,255)))

bubbleCats.addEnemy(EnemySprite("Scorpion.bmp", 100, (10900,screenHeight-150), 20, 10, None, pygame.Color(130,130,130)))
bubbleCats.addPlatform(SceneSprite("TableTopL.bmp", (11300, 250), pygame.Color(131,131,131)))
bubbleCats.addPlatform(SceneSprite("TableTopR.bmp", (11380, 250), pygame.Color(131,131,131)))
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (11330, 170), 5, 1, pygame.Color(255,255,255)))

bubbleCats.addEnemy(EnemySprite("Scorpion.bmp", 100, (11200,screenHeight-150), 20, 10, None, pygame.Color(130,130,130)))
bubbleCats.addPlatform(SceneSprite("TableTopL.bmp", (11700, 250), pygame.Color(131,131,131)))
bubbleCats.addPlatform(SceneSprite("TableTopR.bmp", (11780, 250), pygame.Color(131,131,131)))
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (11730, 170), 5, 1, pygame.Color(255,255,255)))

bubbleCats.addEnemy(EnemySprite("Scorpion.bmp", 100, (11500,screenHeight-150), 20, 10, None, pygame.Color(130,130,130)))
bubbleCats.addPlatform(SceneSprite("TableTopL.bmp", (12100, 250), pygame.Color(131,131,131)))
bubbleCats.addPlatform(SceneSprite("TableTopR.bmp", (12180, 250), pygame.Color(131,131,131)))
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (12130, 170), 5, 1, pygame.Color(255,255,255)))

bubbleCats.addEnemy(EnemySprite("Scorpion.bmp", 100, (11800,screenHeight-150), 20, 10, None, pygame.Color(130,130,130)))
bubbleCats.addPlatform(SceneSprite("TableTopL.bmp", (12500, 250), pygame.Color(131,131,131)))
bubbleCats.addPlatform(SceneSprite("TableTopR.bmp", (12580, 250), pygame.Color(131,131,131)))
bubbleCats.addItem(ItemSprite("Heart.bmp", 26, (12567,230), 5, 0, pygame.Color(0,0,0)))

bubbleCats.addEnemy(EnemySprite("Scorpion.bmp", 100, (12100,screenHeight-150), 20, 10, None, pygame.Color(130,130,130)))
bubbleCats.addEnemy(EnemySprite("Scorpion.bmp", 100, (12400,screenHeight-150), 20, 10, None, pygame.Color(130,130,130)))

# BubbleFest
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (12800, 450), 5, 1, pygame.Color(255,255,255)))
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (12900, 350), 5, 1, pygame.Color(255,255,255)))
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (13000, 450), 5, 1, pygame.Color(255,255,255)))
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (13100, 300), 5, 1, pygame.Color(255,255,255)))
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (13200, 450), 5, 1, pygame.Color(255,255,255)))
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (13300, 250), 5, 1, pygame.Color(255,255,255)))
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (13400, 450), 5, 1, pygame.Color(255,255,255)))
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (13500, 200), 5, 1, pygame.Color(255,255,255)))
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (13600, 450), 5, 1, pygame.Color(255,255,255)))
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (13700, 250), 5, 1, pygame.Color(255,255,255)))
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (13800, 450), 5, 1, pygame.Color(255,255,255)))
bubbleCats.addItem(ItemSprite("Bubble.bmp", 100, (13900, 300), 5, 1, pygame.Color(255,255,255)))

bubbleCats.addPlayer(Cat())













bubbleCats.loadBackgroundMusic("Good Sleep.mp3")

while 1:
    if not bubbleCats.update():
        break
    
bubbleCats.quit()