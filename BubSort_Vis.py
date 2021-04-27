import pygame, sys, random
from pygame.locals import *

def randListGen(l):
    ## Generates a list of random integers
    res = []
    for i in range(0, l):
        rndNum = random.randint(1, 100)
        res.append(rndNum)
    
    return res

## INIT
pygame.init()
clock = pygame.time.Clock()

WIN_SIZE = [700, 600]
screen = pygame.display.set_mode(WIN_SIZE, 0, 32)

## Data Set
data = randListGen(20)
diff_list = []
indx = 0

## Initiate bar list
bars = []
base = WIN_SIZE[1]
wdth_b = WIN_SIZE[0] / len(data)

## Making List of sized bar
for i in range(0, len(data)):
    diff_list.append(0)
    left = i * wdth_b
    hgt = data[i] * 2
    bar = pygame.Rect(left, (WIN_SIZE[1]- hgt), wdth_b, hgt)
    bars.append(bar)

## MAINLOOP
while True:
    #print (data)
    j = indx +1
    screen.fill( (0, 0, 0) )
    ## CONTROL
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    ## Algorithm
    while j < len(data):

        if data[indx] < data[j]:
            #pygame.draw.rect(screen, (0, 255, 0), bars[j])
            tmp = data[indx]
            data[indx] = data[j]
            data[j] = tmp
        

            ## RENDER
            for b in range(0, len(bars)):
                bars[b].height = data[b]
                bars[b].top = WIN_SIZE[1] - bars[b].height
                pygame.draw.rect(screen, (255, 255, 255), bars[b])
                
                pygame.draw.rect(screen, (0, 255, 0), bars[j])
            
        j += 1
            
    # RENDER
    for b in range(0, len(bars)):
        bars[b].height = data[b]
        bars[b].top = WIN_SIZE[1] - bars[b].height
        pygame.draw.rect(screen, (255, 255, 255), bars[b])

        if b == indx:
            pygame.draw.rect(screen, (255, 0, 0), bars[indx])
            #pass
       
    pygame.display.update()
    clock.tick(10)
    indx += 1