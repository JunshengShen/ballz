import pygame
from pygame import *
import random
import math

class Level:
    def __init__(self,round):
        self.brickNumber = random.randint(1, 5)  # 砖块数量
        self.bricks = []

        positions = [0,1,2,3,4,5,6,7]
        for i in range(self.brickNumber):
            position = random.choice(positions)
            positions.remove(position)
            self.bricks.append(Brick(positionNumber = position,bitNumber = round ))

    def moveDown(self):
        for brick in self.bricks:
            brick.listNumber+=1
            screen.blit(brick.surf,(brick.positionNumber*75,brick.listNumber*75))
    def paintCurrentLevel(self):
        for brick in self.bricks:
            color = 0
            if (brick.bitNumber >= 12):
                color = 240
            else:
                color = brick.bitNumber*20
            brick.surf.fill((255, color, color))
            screen.blit(brick.surf, (brick.positionNumber * 75, brick.listNumber * 75))

class Brick(pygame.sprite.Sprite):
    def __init__(self , positionNumber, bitNumber = 1):
        super(Brick,self).__init__()
        self.positionNumber = positionNumber
        self.bitNumber = bitNumber
        self.surf = pygame.Surface((75,75))
        color = 0
        if(bitNumber >= 12):
            color = 240
        else:
            color = bitNumber*20
        self.surf.fill((255, color, color))
        self.rect = self.surf.get_rect()
        self.listNumber = 0
        screen.blit(self.surf, (self.positionNumber*75, 0))
        # self.surf = pygame.Surface((75,75))
        # self.surf.fill((255,255,255))
        # self.rect = self.surf.get_rect()

class Ball():
    def __init__(self):

        self.paint = True
        self.ballMove = False
        self.keepdown = True
        self.surf = pygame.image.load("ball.jpg")


        self.rect = self.surf.get_rect()
        self.rect = self.rect.move([300, 700])
        screen.blit(self.surf, [300,700])
        self.speed = [1, 1]

        pygame.display.flip()
        pygame.display.update()
    def direction(self,x,y):
        self.speed = [x,y]


    def move(self,levels):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0:
            self.speed[0] = abs(self.speed[0])
        if self.rect.right > 600:
            self.speed[0] = -abs(self.speed[0])
        if self.rect.top < 0 :
            self.speed[1] =  abs(self.speed[1])
        if self.rect.bottom > 800:
            self.ballMove=False
            self.paint = True
            self.rect = self.rect.move([0,800-self.rect.bottom])
            return

        screen.blit(self.surf, self.rect)
        self.collision(levels)
        for level in levels:
            for brick in level.bricks:
                if(brick.bitNumber==0):
                    level.bricks.remove(brick)
        #pygame.time.delay(10)
    def draw(self):
        screen.blit(self.surf, self.rect)

    def collision(self,levels):
        for level in levels:
            for brick in level.bricks:
                y=0
                x=0
                xOrigin = 0
                yOrigin = 0
                if(self.rect.top <= (brick.listNumber+1)*75 and self.rect.top > brick.listNumber*75
                    and ((self.rect.left <= (brick.positionNumber + 1) * 75 and self.rect.left > brick.positionNumber * 75)
                    or (self.rect.right >= brick.positionNumber * 75 and self.rect.right < (brick.positionNumber + 1) * 75))):#and(((brick.listNumber+1)*75-self.rect.top)<20):
                    yOrigin = self.speed[1]
                    self.speed[1] = abs(self.speed[1])
                    y=(brick.listNumber+1)*75-self.rect.top+1

                elif((self.rect.bottom >=brick.listNumber*75 and self.rect.bottom <(brick.listNumber+1)*75)
                    and((self.rect.left <= (brick.positionNumber + 1) * 75 and self.rect.left > brick.positionNumber * 75)
                    or (self.rect.right >= brick.positionNumber * 75 and self.rect.right < (brick.positionNumber + 1) * 75))#and((self.rect.bottom-brick.listNumber*75)<20)
                   ):
                    yOrigin = self.speed[1]
                    self.speed[1] = - abs(self.speed[1])
                    y = self.rect.bottom-brick.listNumber*75+1

                if (self.rect.left <= (brick.positionNumber + 1) * 75 and self.rect.left > brick.positionNumber * 75
                     and((self.rect.top <= (brick.listNumber+1)*75 and self.rect.top > brick.listNumber*75)
                         or(self.rect.bottom >=brick.listNumber*75 and self.rect.bottom <(brick.listNumber+1)*75))):#and(((brick.positionNumber+1)*75-self.rect.left)<20):
                    xOrigin = self.speed[0]
                    self.speed[0] = abs(self.speed[0])
                    x=(brick.positionNumber+1)*75-self.rect.left+1

                elif((self.rect.right >= brick.positionNumber * 75 and self.rect.right < (brick.positionNumber + 1) * 75)
                    and ((self.rect.top <= (brick.listNumber + 1) * 75 and self.rect.top > brick.listNumber * 75)
                         or (self.rect.bottom >= brick.listNumber * 75 and self.rect.bottom < (brick.listNumber + 1) * 75))#and((self.rect.right-brick.positionNumber*75)<20)
                    ):
                    xOrigin = self.speed[0]
                    self.speed[0] = - abs(self.speed[0])
                    x=self.rect.right-brick.positionNumber*75+1
                if(x!=0 and y!=0):
                    if x > y:
                         self.speed[0] = xOrigin
                    else:
                        self.speed[1] = yOrigin
                    brick.bitNumber -= 1
                    return
                if(x!=0 or y!= 0):
                    brick.bitNumber -= 1
                    return

pygame.init()

screen = pygame.display.set_mode((600,800))

# player = Brick()
#
#
# screen.blit(player.surf,(400,300))
#


pygame.display.flip()

color = [100,255,200]
mouseIsDown = False
round = 1


levels = []

pygame.display.flip()
pygame.display.update()
running = True
balls = []
balls.append(Ball())
#ball = Ball()
pygame.display.flip()
pygame.display.update()

while round:
    # stopedBall = 0
    # for ball in balls:
    #
    #     if (ball.paint == True):
    #         stopedBall += 1
    # if stopedBall == len(balls):
    #     for ball in balls:
    #         if (ball.ballMove == True):
    #             ball.move(levels)
    #
    pygame.time.delay(5)
    screen.fill((0, 0, 0))
    for ball in balls:
        ball.draw()
        if(ball.ballMove==True):
            ball.move(levels)

    #ball.move()
    for level in levels:
        level.paintCurrentLevel()
    pygame.display.update()
    #pygame.time.delay(1)
    #ball.move()
    #每一回合开始时绘制方块  使用一个标志paint来标明是否需要绘制
    gameOver = False

    stopedBall = 0
    for ball in balls:

        if(ball.paint==True):
            stopedBall += 1
    if stopedBall == len(balls):
        #现有方块向下移
        for level in levels:
            if(len(level.bricks))==0:
                levels.remove(level)

        screen.fill((0, 0, 0))
        for level in levels:
            level.moveDown()
        #绘制新的一层

        levels.insert(0,Level(round))

        try:
            if (levels[-1].bricks[0].listNumber > 9):
                gameOver = True
        except:
            shit=1
        round += 1
        ball.draw()
        for ball in balls:
            ball.paint=False
        if(round!=1 ):
            balls.append(Ball())
    if gameOver == True:
        break
    pygame.display.update()



    for event in pygame.event.get():

        if event.type == MOUSEBUTTONDOWN and mouseIsDown==False:
            mouseIsDown = True
            poss = pygame.mouse.get_pos()

        if event.type == MOUSEBUTTONDOWN and mouseIsDown==True:
            post=pygame.mouse.get_pos()



        if event.type == MOUSEBUTTONUP:
            mouseIsDown=False
            pose = pygame.mouse.get_pos()
            move_x = pose[0] - poss[0]
            move_y = pose[1] - poss[1]
            if(move_y>=0):
                continue
            mo = pow((move_x*move_x+move_y*move_y),0.5)
            for ball in balls:
                ball.direction(move_x/mo*10,move_y/mo*10)

                ball.ballMove = True

        if event.type == QUIT:
            exit()
background = pygame.image.load('dead.jpg').convert()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0, 0))
    pygame.display.update()