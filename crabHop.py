import pygame
from sys import exit

pygame.init()
pygame.mixer.init()
screen=pygame.display.set_mode((400,500))
clock=pygame.time.Clock()

pygame.display.set_caption('CrabHop')

#3 surfaces
garden1Surface=pygame.image.load('images/green.jpg').convert_alpha()
garden1Rect=garden1Surface.get_rect(bottomleft=(0,450))
waterSurface=pygame.image.load('images/blue.jpg').convert_alpha()
waterRect=waterSurface.get_rect(bottomleft=(0,400))
garden2Surface=pygame.image.load('images/green.jpg').convert_alpha()
garden2Rect=garden1Surface.get_rect(bottomleft=(0,100))

#black rectangles
rectUPsurface=pygame.Surface((400,50))
rectDOWNsurface=pygame.Surface((400,50))

#leaves row 1
leafr1Surf_1=pygame.image.load('images/leaf.png').convert_alpha()
leafr1Rect_1=leafr1Surf_1.get_rect(bottomleft=(-90,400))
leafr1Surf2=pygame.image.load('images/leaf_withlotus.png').convert_alpha()
leafr1Rect2=leafr1Surf2.get_rect(bottomleft=(130,400))
leafr1Surf4=pygame.image.load('images/leaf.png').convert_alpha()
leafr1Rect4=leafr1Surf4.get_rect(bottomleft=(375,400))

#leaves row 2
leafr2Surf1=pygame.image.load('images/leaf_withlotus.png').convert_alpha()
leafr2Rect1=leafr2Surf1.get_rect(bottomleft=(30,325))
leafr2Surf2=pygame.image.load('images/leaf.png').convert_alpha()
leafr2Rect2=leafr2Surf2.get_rect(bottomleft=(180,325))
leafr2Surf4=pygame.image.load('images/leaf_withlotus.png').convert_alpha()
leafr2Rect4=leafr2Surf4.get_rect(bottomleft=(390,325))

#leaves row 3
leafr3Surf_1=pygame.image.load('images/leaf_withlotus.png').convert_alpha()
leafr3Rect_1=leafr3Surf_1.get_rect(bottomleft=(-90,250))
leafr3Surf2=pygame.image.load('images/leaf.png').convert_alpha()
leafr3Rect2=leafr3Surf2.get_rect(bottomleft=(130,250))
leafr3Surf3=pygame.image.load('images/leaf.png').convert_alpha()
leafr3Rect3=leafr3Surf3.get_rect(bottomleft=(240,250))

#leaves row 4
leafr4Surf1=pygame.image.load('images/leaf_withlotus.png').convert_alpha()
leafr4Rect1=leafr4Surf1.get_rect(bottomleft=(30,175))
leafr4Surf3=pygame.image.load('images/leaf_withlotus.png').convert_alpha()
leafr4Rect3=leafr4Surf3.get_rect(bottomleft=(270,175))
leafr4Surf4=pygame.image.load('images/leaf.png').convert_alpha()
leafr4Rect4=leafr4Surf4.get_rect(bottomleft=(390,175))

#crab
crab1Sur=pygame.image.load('images/crab.png').convert_alpha()
crab1Sur=pygame.transform.scale(crab1Sur,(55,45))
crab1Rect=crab1Sur.get_rect(center=(200,425))

gameActive=False
totalLives=3

#fonts
textFont1=pygame.font.Font('fonts/Pixeltype.ttf',40)
textFont3=pygame.font.Font('fonts/font3.ttf',30)

#crab lives
crablivesSurf1=pygame.image.load('images/crab.png').convert_alpha()
crablivesSurf1=pygame.transform.scale(crablivesSurf1,(45,35))
crablivesRect1=crablivesSurf1.get_rect(center=(170,475))

crablivesSurf2=pygame.image.load('images/crab.png').convert_alpha()
crablivesSurf2=pygame.transform.scale(crablivesSurf2,(45,35))
crablivesRect2=crablivesSurf2.get_rect(center=(220,475))

crablivesSurf3=pygame.image.load('images/crab.png').convert_alpha()
crablivesSurf3=pygame.transform.scale(crablivesSurf3,(45,35))
crablivesRect3=crablivesSurf3.get_rect(center=(270,475))

#score count
score=0
scored=False
last_collision_time = 0
collision_delay = 500 

#intro surfaces
crabIntro=pygame.image.load('images/crab.png').convert_alpha()
crabIntroRect=crabIntro.get_rect(center=(200,250))
leafIntro=pygame.image.load('images/leaf_intro.png').convert_alpha()
leafIntro=pygame.transform.scale(leafIntro,(160,160))
leafIntroRect=leafIntro.get_rect(center=(200,250))
gameMessage=textFont1.render('Press SPACE to start',False,'Black')
round=0
gameName=textFont1.render('CRAB HOP',False,'Black')
gameNameRect=gameName.get_rect(center=(200,150))

#fade out function
def fade_out(surface, crab_surface, crab_rect, draw_scene):
    for alpha in range(255, 0, -20): 
        draw_scene()  
        temp = crab_surface.copy()
        temp.set_alpha(alpha)
        surface.blit(temp, crab_rect)
        pygame.display.update()
        pygame.time.delay(30)

def draw_scene():
    screen.blit(garden1Surface, garden1Rect)
    screen.blit(waterSurface, waterRect)
    screen.blit(garden2Surface, garden2Rect)

    # draw all leaves here
    screen.blit(leafr1Surf_1, leafr1Rect_1)
    screen.blit(leafr1Surf2, leafr1Rect2)
    screen.blit(leafr1Surf4, leafr1Rect4)
    screen.blit(leafr2Surf1, leafr2Rect1)
    screen.blit(leafr2Surf2, leafr2Rect2)
    screen.blit(leafr2Surf4, leafr2Rect4)
    screen.blit(leafr3Surf_1, leafr3Rect_1)
    screen.blit(leafr3Surf2, leafr3Rect2)
    screen.blit(leafr3Surf3, leafr3Rect3)
    screen.blit(leafr4Surf1, leafr4Rect1)
    screen.blit(leafr4Surf3, leafr4Rect3)
    screen.blit(leafr4Surf4, leafr4Rect4)

#loading sounds
bg_music=pygame.mixer.Sound('sound/bg.mp3')
splash_sound=pygame.mixer.Sound('sound/water.mp3')
jump_sound=pygame.mixer.Sound('sound/jump.wav')
jump_sound.set_volume(0.8)
bg_music.set_volume(0.6)
bg_music.play(-1)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        
        if gameActive:
            if event.type==pygame.KEYDOWN and event.key==pygame.K_UP:
                jump_sound.play()
                if crab1Rect.y>75:
                    crab1Rect.y-=70
                    scored=False
        
        if not gameActive and event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
            totalLives = 3
            score = 0
            crab1Rect.center = (200, 425)
            gameActive = True



    if gameActive and totalLives>=0:
        round+=1
        screen.blit(rectUPsurface,(0,0))
        screen.blit(rectUPsurface,(0,450))
        screen.blit(garden1Surface,garden1Rect)
        screen.blit(waterSurface,waterRect)
        screen.blit(garden2Surface,garden2Rect)

        # Boundary check (place this right after if gameActive and totalLives >= 0:)
        if crab1Rect.left <= 0 or crab1Rect.right >= 400:
                totalLives -= 1
                screen.blit(garden1Surface, garden1Rect)
                screen.blit(waterSurface, waterRect)
                screen.blit(garden2Surface, garden2Rect)

                screen.blit(leafr1Surf_1, leafr1Rect_1)
                screen.blit(leafr1Surf2, leafr1Rect2)
                screen.blit(leafr1Surf4, leafr1Rect4)
                screen.blit(leafr2Surf1, leafr2Rect1)
                screen.blit(leafr2Surf2, leafr2Rect2)
                screen.blit(leafr2Surf4, leafr2Rect4)
                screen.blit(leafr3Surf_1, leafr3Rect_1)
                screen.blit(leafr3Surf2, leafr3Rect2)
                screen.blit(leafr3Surf3, leafr3Rect3)
                screen.blit(leafr4Surf1, leafr4Rect1)
                screen.blit(leafr4Surf3, leafr4Rect3)
                screen.blit(leafr4Surf4, leafr4Rect4)

                screen.blit(crab1Sur, crab1Rect)
                livesFont = textFont1.render(f'Lives left: ', True, 'Yellow')
                screen.blit(livesFont, (10, 465))
                scoreText = textFont1.render(f'Score: {score}', False, 'Yellow')
                screen.blit(scoreText, (10, 11))

                pygame.display.update()

                pygame.time.wait(1000)
                crab1Rect.center = (200, 425)
                score = 0
                continue

        if totalLives==3:
                screen.blit(crablivesSurf1,crablivesRect1)
                screen.blit(crablivesSurf2,crablivesRect2)
                screen.blit(crablivesSurf3,crablivesRect3)
        elif totalLives==2:
                screen.blit(crablivesSurf1,crablivesRect1)
                screen.blit(crablivesSurf2,crablivesRect2)
                pygame.draw.rect(screen, 'black', (240, 458, 51, 100))
        elif totalLives==1:
               screen.blit(crablivesSurf1,crablivesRect1)
               pygame.draw.rect(screen, 'black', (190, 458, 102, 100))
        elif totalLives==0:
               pygame.draw.rect(screen, 'black', (140, 458, 153, 100))
        elif totalLives<0:
               gameActive=False  

        livesFont=textFont1.render('Lives left: ',True,'Yellow')
        screen.blit(livesFont,(10,465)) 

        #score text
        pygame.draw.rect(screen, 'black', (0, 0, 140, 50))
        scoreText=textFont1.render(f'Score: {score}',False,'Yellow')
        screen.blit(scoreText,(10,11))

        #leaves row 1
        leafr1Rect_1.x+=1
        if leafr1Rect_1.x>500: leafr1Rect_1.x=-90
        screen.blit(leafr1Surf_1,leafr1Rect_1)

        leafr1Rect2.x+=1
        if leafr1Rect2.x>500: leafr1Rect2.x=-90
        screen.blit(leafr1Surf2,leafr1Rect2)

        leafr1Rect4.x+=1
        if leafr1Rect4.x>500: leafr1Rect4.x=-90
        screen.blit(leafr1Surf4,leafr1Rect4)


        #leaves row 2
        leafr2Rect1.x-=1
        if leafr2Rect1.x<-80: leafr2Rect1.x=490
        screen.blit(leafr2Surf1,leafr2Rect1)

        leafr2Rect2.x-=1
        if leafr2Rect2.x<-80: leafr2Rect2.x=490
        screen.blit(leafr2Surf2,leafr2Rect2)

        leafr2Rect4.x-=1
        if leafr2Rect4.x<-80: leafr2Rect4.x=490
        screen.blit(leafr2Surf4,leafr2Rect4)


        #leaves row 3
        leafr3Rect_1.x+=1
        if leafr3Rect_1.x>500: leafr3Rect_1.x=-90
        screen.blit(leafr3Surf_1,leafr3Rect_1)

        leafr3Rect2.x+=1
        if leafr3Rect2.x>500: leafr3Rect2.x=-90
        screen.blit(leafr3Surf2,leafr3Rect2)

        leafr3Rect3.x+=1
        if leafr3Rect3.x>500: leafr3Rect3.x=-90
        screen.blit(leafr3Surf3,leafr3Rect3)


        #leaves row 4
        leafr4Rect1.x-=1
        if leafr4Rect1.x<-80: leafr4Rect1.x=490
        screen.blit(leafr4Surf1,leafr4Rect1)

        leafr4Rect3.x-=1
        if leafr4Rect3.x<-80: leafr4Rect3.x=490
        screen.blit(leafr4Surf3,leafr4Rect3)

        leafr4Rect4.x-=1
        if leafr4Rect4.x<-80: leafr4Rect4.x=490
        screen.blit(leafr4Surf4,leafr4Rect4)


        #crab collision
        screen.blit(crab1Sur,crab1Rect)
        #row 1
        if crab1Rect.colliderect(leafr1Rect_1):
                    crab1Rect.x+=1
                    if crab1Rect.x>500: crab1Rect.x=-90
                    if not scored:
                           current_time=pygame.time.get_ticks()
                           if current_time-last_collision_time>collision_delay:
                                score+=10
                                last_collision_time=current_time
                                scored=True

        elif crab1Rect.colliderect(leafr1Rect2):
                    crab1Rect.x+=1
                    if crab1Rect.x>500: crab1Rect.x=-90
                    if not scored:
                        current_time=pygame.time.get_ticks()
                        if current_time-last_collision_time>collision_delay:
                                score+=20
                                last_collision_time=current_time
                                scored=True
        elif crab1Rect.colliderect(leafr1Rect4):
                    crab1Rect.x+=1
                    if crab1Rect.x>500: crab1Rect.x=-90
                    if not scored:
                        current_time=pygame.time.get_ticks()
                        if current_time-last_collision_time>collision_delay:
                                score+=10
                                last_collision_time=current_time
                                scored=True
        #row2
        elif crab1Rect.colliderect(leafr2Rect1):
                crab1Rect.x-=1
                if crab1Rect.x<-80: crab1Rect.x=490
                if not scored:
                        current_time=pygame.time.get_ticks()
                        if current_time-last_collision_time>collision_delay:
                                score+=20
                                last_collision_time=current_time
                                scored=True
        elif crab1Rect.colliderect(leafr2Rect2):
                crab1Rect.x-=1
                if crab1Rect.x<-80: crab1Rect.x=490
                if not scored:
                        current_time=pygame.time.get_ticks()
                        if current_time-last_collision_time>collision_delay:
                                score+=10
                                last_collision_time=current_time
                                scored=True
        elif crab1Rect.colliderect(leafr2Rect4):
                crab1Rect.x-=1
                if crab1Rect.x<-80: crab1Rect.x=490
                if not scored:
                        current_time=pygame.time.get_ticks()
                        if current_time-last_collision_time>collision_delay:
                                score+=20
                                last_collision_time=current_time
                                scored=True
        #row 3 
        elif crab1Rect.colliderect(leafr3Rect_1):
                crab1Rect.x+=1
                if crab1Rect.x>500: crab1Rect.x=-90
                if not scored:
                        current_time=pygame.time.get_ticks()
                        if current_time-last_collision_time>collision_delay:
                                score+=20
                                last_collision_time=current_time
                                scored=True
        elif crab1Rect.colliderect(leafr3Rect2):
                crab1Rect.x+=1
                if crab1Rect.x>500: crab1Rect.x=-90
                if not scored:
                        current_time=pygame.time.get_ticks()
                        if current_time-last_collision_time>collision_delay:
                                score+=10
                                last_collision_time=current_time
                                scored=True
        elif crab1Rect.colliderect(leafr3Rect3):
                crab1Rect.x+=1
                if crab1Rect.x>500: crab1Rect.x=-90
                if not scored:
                        current_time=pygame.time.get_ticks()
                        if current_time-last_collision_time>collision_delay:
                                score+=10
                                last_collision_time=current_time
                                scored=True
        #row 4
        elif crab1Rect.colliderect(leafr4Rect1):
                crab1Rect.x-=1
                if crab1Rect.x<-80: crab1Rect.x=490
                if not scored:
                        current_time=pygame.time.get_ticks()
                        if current_time-last_collision_time>collision_delay:
                                score+=20
                                last_collision_time=current_time
                                scored=True
        elif crab1Rect.colliderect(leafr4Rect3):
                crab1Rect.x-=1
                if crab1Rect.x<-80: crab1Rect.x=490
                if not scored:
                        current_time=pygame.time.get_ticks()
                        if current_time-last_collision_time>collision_delay:
                                score+=20
                                last_collision_time=current_time
                                scored=True
        elif crab1Rect.colliderect(leafr4Rect4):
                crab1Rect.x-=1
                if crab1Rect.x<-80: crab1Rect.x=490
                if not scored:
                        current_time=pygame.time.get_ticks()
                        if current_time-last_collision_time>collision_delay:
                                score+=10
                                last_collision_time=current_time
                                scored=True
        
        #collision with water
        elif crab1Rect.colliderect(waterRect):
                totalLives -= 1
                jump_sound.set_volume(0)
                bg_music.set_volume(0.3)
                splash_sound.play()
                fade_out(screen, crab1Sur, crab1Rect, draw_scene)
                pygame.time.wait(500)
                crab1Rect.center = (200, 425)
                score = 0
                jump_sound.set_volume(0.8)
                bg_music.set_volume(0.6)

        elif crab1Rect.colliderect(garden2Rect):
               pygame.display.update() 
               pygame.time.wait(1000)
               gameActive=False
    else:
        # screen.fill((130, 195, 232))
        screen.fill((168, 233, 255))
        screen.blit(leafIntro,leafIntroRect)
        screen.blit(crabIntro,crabIntroRect)
        screen.blit(gameName,gameNameRect)

        if round==0:
                screen.blit(gameMessage,(80,350))
        else:
               scoreEnd=textFont1.render(f'Your score: {score}',False,'Black')
               screen.blit(scoreEnd,(110,330))
               scoreEnd2=textFont1.render('press SPACE to restart',False,'Black')
               screen.blit(scoreEnd2,(65,360))

    
    pygame.display.update()
    clock.tick(60)