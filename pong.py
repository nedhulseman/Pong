import pygame, sys, time
from pygame.locals import *
from random import randint

pygame.init()

WINDOWWIDTH = 600
WINDOWHEIGHT = 300
MOVESPEED = 15

threeRIGHT = '3right'
twoRIGHT = '2right'
oneRIGHT = '1right'
RIGHT = 'right'
NEG1RIGHT ='-1right'
NEG2RIGHT = '-2right'
NEG3RIGHT = '-3right'

threeLEFT = '3left'
twoLEFT = '2left'
oneLEFT = '1left'
LEFT = 'left'
NEG1LEFT ='-1left'
NEG2LEFT = '-2left'
NEG3LEFT = '-3left'

directions=[oneRIGHT, twoRIGHT, threeRIGHT, RIGHT, NEG1RIGHT, NEG2RIGHT, NEG3RIGHT,
            oneLEFT, twoLEFT, threeLEFT, LEFT, NEG1LEFT, NEG2LEFT, NEG3LEFT]

#creation of colors
BLACK=(0,0,0)
WHITE=(255, 255, 255)

player1Score = 0
player2Score = 0 
scores=[player1Score, player2Score]

canvas=pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Pong')

leftPaddle=pygame.draw.rect(canvas, WHITE, (40, 200, 11, 80))
rightPaddle=pygame.draw.rect(canvas, WHITE, (WINDOWWIDTH-30, 200, 10, 77))
paddles = [leftPaddle, rightPaddle]
ball = {'rect':pygame.Rect(WINDOWWIDTH/2, WINDOWHEIGHT/2, 10, 10), 
        'color':WHITE, 'dir': None}

iterator = 0



def startGame(ball, directions, windowwidth, windowheight):
    ball['rect'].left = windowwidth / 2 + ball['rect'].width / 2
    ball['rect'].top = windowheight / 2 + ball['rect'].height / 2
    ball['dir'] = directions[randint(0, 13)]
    time.sleep(.8)
 
def movingBall(ball, ballspeed=1):
    if ball['dir'] == '3right':
        ball['rect'].left += ballspeed * 4
        ball['rect'].top -= ballspeed * 6
    elif ball['dir'] == '2right':
        ball['rect'].left += ballspeed * 4
        ball['rect'].top -= ballspeed * 4
    elif ball['dir'] == '1right':
        ball['rect'].left += ballspeed * 5
        ball['rect'].top -= ballspeed * 2
    elif ball['dir'] == 'right':
        ball['rect'].left += ballspeed * 5
    elif ball['dir'] == '-1right':
        ball['rect'].left += ballspeed * 5
        ball['rect'].top += ballspeed * 2
    elif ball['dir'] == '-2right':
        ball['rect'].left += ballspeed * 4
        ball['rect'].top += ballspeed * 4
    elif ball['dir'] == '-3right':
        ball['rect'].left += ballspeed * 4
        ball['rect'].top += ballspeed * 6

    
    elif ball['dir'] == '3left':
        ball['rect'].left -= ballspeed * 4
        ball['rect'].top -= ballspeed * 6
    elif ball['dir'] == '2left':
        ball['rect'].left -= ballspeed * 4
        ball['rect'].top -= ballspeed * 4
    elif ball['dir'] == '1left':
        ball['rect'].left -= ballspeed * 5
        ball['rect'].top -= ballspeed * 2
    elif ball['dir'] == 'left':
        ball['rect'].left -= ballspeed * 5
    elif ball['dir'] == '-1left':
        ball['rect'].left -= ballspeed * 5
        ball['rect'].top += ballspeed * 2
    elif ball['dir'] == '-2left':
        ball['rect'].left -= ballspeed * 4
        ball['rect'].top += ballspeed * 4
    elif ball['dir'] == '-3left':
        ball['rect'].left -= ballspeed * 4
        ball['rect'].top += ballspeed * 6
        
def checkHitSide(ball, windowheight):
    if ball['rect'].top < 0:
        if ball['dir'] == '3right':
            ball['dir'] = '-3right'
        elif ball['dir'] == '2right':
            ball['dir'] = '-2right'
        elif ball['dir'] == '1right':
            ball['dir'] = '-1right'
       
        elif ball['dir'] == '3left':
            ball['dir'] = '-3left'
        elif ball['dir'] == '2left':
            ball['dir'] = '-2left'
        elif ball['dir'] == '1left':
            ball['dir'] = '-1left'
    elif ball['rect'].top + ball['rect'].height > windowheight:
        if ball['dir'] == '-3right':
            ball['dir'] = '3right'
        elif ball['dir'] == '-2right':
            ball['dir'] = '2right'
        elif ball['dir'] == '-1right':
            ball['dir'] = '1right'
       
        elif ball['dir'] == '-3left':
            ball['dir'] = '3left'
        elif ball['dir'] == '-2left':
            ball['dir'] = '2left'
        elif ball['dir'] == '-1left':
            ball['dir'] = '1left'

def checkHitPaddle(ball, paddle):
    if 'right' in ball['dir']:
        if ball['rect'].left + ball['rect'].width >= paddle.left and ball['rect'].left + ball['rect'].width <= paddle.left + paddle.width:
           if ball['rect'].top + ball['rect'].height >= paddle.top and ball['rect'].top <= paddle.top + 11:
               ball['dir'] = '3left'
           elif ball['rect'].top + ball['rect'].height > paddle.top + 11 and ball['rect'].top <= paddle.top + 22:
                ball['dir'] = '2left'
           elif ball['rect'].top + ball['rect'].height > paddle.top + 22 and ball['rect'].top <= paddle.top + 33:
                ball['dir'] = '1left'
           elif ball['rect'].top + ball['rect'].height > paddle.top + 33 and ball['rect'].top <= paddle.top + 44:
                ball['dir'] = 'left'
           elif ball['rect'].top + ball['rect'].height > paddle.top + 44 and ball['rect'].top <= paddle.top + 55:
                ball['dir'] = '-1left'
           elif ball['rect'].top + ball['rect'].height > paddle.top + 55 and ball['rect'].top <= paddle.top + 66:
                ball['dir'] = '-2left'
           elif ball['rect'].top + ball['rect'].height > paddle.top + 66 and ball['rect'].top <= paddle.top + 77:
                ball['dir'] = '-3left'
    if 'left' in ball['dir']:
        if ball['rect'].left <= paddle.left + paddle.width and ball['rect'].left >= paddle.left:
            if ball['rect'].top + ball['rect'].height >= paddle.top and ball['rect'].top < paddle.top + 40:
                 ball['dir'] = '3right'
            elif ball['rect'].top + ball['rect'].height > paddle.top + 11 and ball['rect'].top <= paddle.top + 22:
                 ball['dir'] = '2right'
            elif ball['rect'].top + ball['rect'].height > paddle.top + 22 and ball['rect'].top <= paddle.top + 33:
                 ball['dir'] = '1right'
            elif ball['rect'].top + ball['rect'].height > paddle.top + 33 and ball['rect'].top <= paddle.top + 44:
                 ball['dir'] = 'right'
            elif ball['rect'].top + ball['rect'].height > paddle.top + 44 and ball['rect'].top <= paddle.top + 55:
                 ball['dir'] = '-1right'
            elif ball['rect'].top + ball['rect'].height > paddle.top + 55 and ball['rect'].top <= paddle.top + 66:
                 ball['dir'] = '-2right'
            elif ball['rect'].top + ball['rect'].height > paddle.top + 66 and ball['rect'].top <= paddle.top + 77:
                 ball['dir'] = '-3right'
                
def score(scores, windowwidth, windowheight, ball, directions):
    if ball['rect'].left < 0 or ball['rect'].left + ball['rect'].width > windowwidth:
        if ball['rect'].left < 0:
            scores[1] += 1
        else:
            scores[0] += 1
        startGame(ball, directions, windowwidth, windowheight)
        print(scores)

def printScore(scores):
    top = 10
    player = 1
    for score in scores:
        if player == 1:
            left = 210
        else:
            left = 350
        if score == 0:
            pygame.draw.rect(canvas, WHITE, (left, top, 40, 50))
            pygame.draw.rect(canvas, BLACK, (left + 10, top + 10, 20, 30))
        elif score == 1:
            pygame.draw.rect(canvas, WHITE, (left, top, 10, 50))
        elif score == 2:
            pygame.draw.rect(canvas, WHITE, (left, top, 30, 10))
            pygame.draw.rect(canvas, WHITE, (left + 20, top, 10, 20))
            pygame.draw.rect(canvas, WHITE, (left, top + 20, 30, 10))
            pygame.draw.rect(canvas, WHITE, (left, top + 20, 10, 20))
            pygame.draw.rect(canvas, WHITE, (left, top + 40, 30, 10))
        elif score == 3:
            pygame.draw.rect(canvas, WHITE, (left + 30, top, 10, 50))
            pygame.draw.rect(canvas, WHITE, (left, top, 30, 10))
            pygame.draw.rect(canvas, WHITE, (left, top + 20, 30, 10))
            pygame.draw.rect(canvas, WHITE, (left, top + 40, 30, 10))
        elif score == 4:
            pygame.draw.rect(canvas, WHITE, (left + 30, top, 10, 50))
            pygame.draw.rect(canvas, WHITE, (left, top, 10, 25))
            pygame.draw.rect(canvas, WHITE, (left, top + 15, 40, 10))            
        elif score == 5:
            pygame.draw.rect(canvas, WHITE, (left, top, 30, 10))
            pygame.draw.rect(canvas, WHITE, (left, top, 10, 20))
            pygame.draw.rect(canvas, WHITE, (left, top + 20, 30, 10))
            pygame.draw.rect(canvas, WHITE, (left + 20, top + 20, 10, 20))
            pygame.draw.rect(canvas, WHITE, (left, top + 40, 30, 10))  
        elif score == 6:
            pygame.draw.rect(canvas, WHITE, (left, top, 10, 50))
            pygame.draw.rect(canvas, WHITE, (left, top, 40, 10))
            pygame.draw.rect(canvas, WHITE, (left, top + 40, 40, 10))
            pygame.draw.rect(canvas, WHITE, (left + 30, top + 25, 10, 25))
            pygame.draw.rect(canvas, WHITE, (left, top + 20, 40, 10))
        elif score == 7:
            pygame.draw.rect(canvas, WHITE, (left, top, 40, 10))
            pygame.draw.rect(canvas, WHITE, (left + 30, top, 10, 50))
        elif score == 8:
            pygame.draw.rect(canvas, WHITE, (left, top, 40, 10))
            pygame.draw.rect(canvas, WHITE, (left, top + 20, 40, 10))
            pygame.draw.rect(canvas, WHITE, (left, top + 40, 40, 10))
            pygame.draw.rect(canvas, WHITE, (left, top, 10, 50))
            pygame.draw.rect(canvas, WHITE, (left + 30, top, 10, 50))
        elif score == 9:
            pygame.draw.rect(canvas, WHITE, (left, top, 40, 10))
            pygame.draw.rect(canvas, WHITE, (left, top + 20, 40, 10))
            pygame.draw.rect(canvas, WHITE, (left, top, 10, 25))
            pygame.draw.rect(canvas, WHITE, (left + 30, top, 10, 50))            
        player += 1
 

    

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    canvas.fill(BLACK)
   
    keyinput = pygame.key.get_pressed()
    if keyinput[pygame.K_DOWN]:
        rightPaddle.top += MOVESPEED
    elif keyinput[pygame.K_UP]:
        rightPaddle.top -= MOVESPEED
    if rightPaddle.top < 0:
        rightPaddle.top = 0
    if rightPaddle.top > WINDOWHEIGHT - rightPaddle.height:
        rightPaddle.top = WINDOWHEIGHT - rightPaddle.height
        
    if keyinput[pygame.K_a]:
        leftPaddle.top += MOVESPEED
    elif keyinput[pygame.K_q]:
        leftPaddle.top -= MOVESPEED
    if leftPaddle.top < 0:
        leftPaddle.top = 0
    if leftPaddle.top > WINDOWHEIGHT - leftPaddle.height:
        leftPaddle.top = WINDOWHEIGHT - leftPaddle.height
    
    
    if iterator == 0:
        startGame(ball, directions, WINDOWWIDTH, WINDOWHEIGHT)
    movingBall(ball, 2)   
    checkHitSide(ball, WINDOWHEIGHT)

    for pad in paddles:
        checkHitPaddle(ball, pad)
        
    score(scores, WINDOWWIDTH, WINDOWHEIGHT, ball, directions)
    printScore(scores)
    for i in scores:
        if i == 10:
            print("Winner!")
            pygame.quit()
            sys.exit()    
    
    pygame.draw.rect(canvas, WHITE, ball['rect'])
    pygame.draw.rect(canvas, WHITE, rightPaddle)   
    pygame.draw.rect(canvas, WHITE, leftPaddle)
    top = 15
    for i in range(15):
        pygame.draw.rect(canvas, WHITE, (297, top, 6, 30))
        top += 60

    pygame.display.update()
    iterator += 1
    time.sleep(.02)


