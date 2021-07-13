import pygame
import os



def main():
    width = 720
    height = 500
    pic_size = 50
    white = (255, 255, 255)
    pygame.init()
    pic = pygame.image.load(os.path.join("images/sheep.png"))
    sound = pygame.mixer.Sound(os.path.join("sounds/sheep.wav"))
    pic = pygame.transform.scale(pic,(pic_size,pic_size))
    y=height / 3
    screen = pygame.display.set_mode((width,height))
    
    # initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
    myfont = pygame.font.SysFont("monospace", 15)

    # render text
    label = myfont.render("Score:", 1, (0,0,0))
    score = 0

    run = True
    while(run):
        screen.fill(white)
        screen.blit(pic,(0,y))
        scoretext=myfont.render("Score:"+str(score), 1,(0,0,0))
        screen.blit(scoretext, (width / 2, 10))
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
                 score += 1
            pygame.display.update() 

main()