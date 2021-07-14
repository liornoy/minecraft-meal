import pygame
import os
import random


def main():
    width = 720
    height = 500
    pic_size = 50
    white = (255, 255, 255)
    pygame.init()
    pic = pygame.image.load(os.path.join("images/sheep.png")) 
    bg_pic = pygame.image.load(os.path.join("images/back-ground.jpg"))
    sound = pygame.mixer.Sound(os.path.join("sounds/sheep.wav"))
    pic = pygame.transform.scale(pic,(pic_size,pic_size))
    y=height / 3
    screen = pygame.display.set_mode((width,height))
    
    # initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
    myfont = pygame.font.SysFont("monospace", 15)

    # render text
    label = myfont.render("Score:", 1, (0,0,0))
    score = 0

    appels = []

    run = True
    while(run):
        screen.fill(white)
        screen.blit(bg_pic,(0,0))
        screen.blit(pic,(0,y))
        pygame.draw.rect(screen, (255,255,255), pygame.Rect(width / 2, 10, 70, 20))
        scoretext=myfont.render("Score:"+str(score), 1,(0,0,0))
        screen.blit(scoretext, (width / 2, 10))
        score  = update_apples(screen,appels,score,y)
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                run = False
            elif event.type == pygame.MOUSEMOTION:
                y = pygame.mouse.get_pos()[1]
                if y > height - pic_size:
                    y = height- pic_size
            elif event.type == pygame.MOUSEBUTTONUP:
                 pygame.mixer.Sound.play(sound)
            pygame.display.update() 

class Apple:
    def __init__(self, starting_X, starting_Y):
        self.pic = pygame.image.load(os.path.join("images/apple.png"))
        self.pic = pygame.transform.scale(self.pic,(30,30))
        self.X = starting_X
        self.Y = starting_Y

def update_apples(screen,apples,score,y):
    rnd = random.randint(0,5000)
    if rnd == 50:
        Y = random.randint(50,450)
        X = 720
        apples += [Apple(X,Y)] 
    for apple in apples:
        screen.blit(apple.pic, (apple.X,apple.Y))
        apple.X -= 0.25
        if apple.X < 0:
            if  abs(apple.Y - y) < 100:
                score+=1
            apples.remove(apple)
    return score
main()