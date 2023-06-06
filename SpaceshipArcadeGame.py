import pygame
import random
import math

#Initializes all pygame modules
pygame.init()

#Sets screen size and game caption
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Spaceship Arcade Game')

#Loads background image
background = pygame.image.load('space-background.jpg')

#Loads spaceship image
Spaceship_Img = pygame.image.load('spaceship.png')
Spaceship_Img = pygame.transform.scale(Spaceship_Img, (80,80))

#Loads alien spacecraft image 1
Space_Alien = pygame.image.load('ufo.png')
Space_Alien = pygame.transform.scale(Space_Alien, (80,80))

#Loads alien spacecraft image 2
Space_Alien_2 = pygame.image.load('ufo.png')
Space_Alien_2 = pygame.transform.scale(Space_Alien_2, (80,80))

#Loads alien spacecraft image 3
Space_Alien_3 = pygame.image.load('ufo.png')
Space_Alien_3 = pygame.transform.scale(Space_Alien_3, (80,80))

#Loads bullet image
bullet = pygame.image.load('bullet.png')
bullet = pygame.transform.scale(bullet, (60,42))

#Sets initial spaceship coordinates and moving horizontal speed
spaceship_X = 360
spaceship_Y = 440
change_X = 0

#Sets initial alien spacecraft x-coordinates
alien_X = random.randint(0,520)
alien_X_2 = random.randint(0,520)
alien_X_3 = random.randint(0,520)

#Sets initial alien spacecraft y-coordinates
alien_Y = 0
alien_Y_2 = 0
alien_Y_3 = 0

#Sets initial alien spacecraft moving horizontal speed
alien_speed_X = 0.5
alien_speed_X_2 = 0.5
alien_speed_X_3 = 0.5


check = False

#Sets initial bullet coordinates
bullet_X = 370
bullet_Y = 400

#Sets initial score
score = 0

#Sets font to display score
font = pygame.font.SysFont('Arial', 32, 'bold')

#Function to display score at top-left
def score_txt():
    score_img = font.render(f'Score: {score}', True, 'white')
    screen.blit(score_img, (10,10))

#Sets font to display 'GAME OVER'
font_gameover = pygame.font.SysFont('Arial', 64, 'bold')

#Function to display 'GAME OVER'
def game_over_txt():
    game_over_img = font_gameover.render('GAME OVER', True, 'white')
    screen.blit(game_over_img, (10,10))

#Combined with 'while running:' initiates game
running = True

#Defines the conditions of when the bullet hits alien spacecraft 1
def collision():
    distance = math.sqrt(math.pow(bullet_X - alien_X, 2) + math.pow(bullet_Y - alien_Y, 2))
    if distance < 45:
        return True

#Defines the conditions of when the bullet hits alien spacecraft 2
def collision_2():
    distance = math.sqrt(math.pow(bullet_X - alien_X_2, 2) + math.pow(bullet_Y - alien_Y_2, 2))
    if distance < 45:
        return True

#Defines the conditions of when the bullet hits alien spacecraft 3
def collision_3():
    distance = math.sqrt(math.pow(bullet_X - alien_X_3, 2) + math.pow(bullet_Y - alien_Y_3, 2))
    if distance < 45:
        return True

while running:
    #Adds background image
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False

        #Changes speed and direction based on key clicks
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                change_X += 0.5
            if event.key == pygame.K_LEFT:
                change_X -= 0.5
            #Adds bullet when space bar is clicked
            if event.key==pygame.K_SPACE:
                if check is False:
                    check = True
                    bullet_X = spaceship_X + 10
    #Changes speed of spaceship based on key clicks
    spaceship_X += change_X
    #Changes direction of spaceship movement when borders are hit
    if spaceship_X <= 0 or spaceship_X >= 720:
        change_X *= -1

    #Determines position, speed, and direction of alien spacecraft 1. Changes position of alien spacecraft 1
    #when collision occurs. Removes all three alien spacecrafts when alien spacecraft 1 collides with spaceship.
    alien_X += alien_speed_X
    if alien_X >= 720:
        alien_Y += 40
        alien_speed_X += 0.25
        alien_speed_X *= -1
    elif alien_X <= 0:
        alien_Y += 40
        alien_speed_X *= -1
        alien_speed_X += 0.25
    if bullet_Y <= 0:
        bullet_Y = 400
        check = False
    if check:
        screen.blit(bullet, (bullet_X, bullet_Y))
        bullet_Y -= 5
    collision_occurrence = collision()
    if collision_occurrence:
        bullet_X = -1000000
        bullet_Y = -1000000
        alien_X = random.randint(0, 520)
        score += 1
    if alien_Y >= 395 and alien_X >= spaceship_X:
        alien_X = -1000000
        alien_Y = -1000000
        alien_X_2 = -1000000
        alien_Y_2 = -1000000
        alien_X_3 = -1000000
        alien_Y_3 = -1000000
        change_X = 0
        game_over_txt()
        print('Game Over')

    #Determines position, speed, and direction of alien spacecraft 2. Changes position of alien spacecraft 2
    #when collision occurs. Removes all three alien spacecrafts when alien spacecraft 2 collides with spaceship.
    alien_X_2 += alien_speed_X_2
    if alien_X_2 >= 720:
        alien_Y_2 += 40
        alien_speed_X_2 += 0.25
        alien_speed_X_2 *= -1
    elif alien_X_2 <= 0:
        alien_Y_2 += 40
        alien_speed_X_2 *= -1
        alien_speed_X_2 += 0.25
    if bullet_Y <= 0:
        bullet_Y = 400
        check = False
    if check:
        screen.blit(bullet, (bullet_X, bullet_Y))
        bullet_Y -= 5
    collision_occurrence_2 = collision_2()
    if collision_occurrence_2:
        bullet_X = -1000000
        bullet_Y = -1000000
        alien_X_2 = random.randint(0, 520)
        score += 1
    if alien_Y_2 >= 395 and alien_X_2 >= spaceship_X:
        alien_X = -1000000
        alien_Y = -1000000
        alien_X_2 = -1000000
        alien_Y_2 = -1000000
        alien_X_3 = -1000000
        alien_Y_3 = -1000000
        change_X = 0
        game_over_txt()
        print('Game Over')

    #Determines position, speed, and direction of alien spacecraft 3. Changes position of alien spacecraft 3
    #when collision occurs. Removes all three alien spacecrafts when alien spacecraft 3 collides with spaceship.
    alien_X_3 += alien_speed_X_3
    if alien_X_3 >= 720:
        alien_Y_3 += 40
        alien_speed_X_3 += 0.25
        alien_speed_X_3 *= -1
    elif alien_X_3 <= 0:
        alien_Y_3 += 40
        alien_speed_X_3 *= -1
        alien_speed_X_3 += 0.25
    if bullet_Y <= 0:
        bullet_Y = 400
        check = False
    if check:
        screen.blit(bullet, (bullet_X, bullet_Y))
        bullet_Y -= 5
    collision_occurrence_3 = collision_3()
    if collision_occurrence_3:
        bullet_X = -1000000
        bullet_Y = -1000000
        alien_X_3 = random.randint(0, 520)
        score += 1
    if alien_Y_3 >= 395 and alien_X_3 >= spaceship_X:
        alien_X = -1000000
        alien_Y = -1000000
        alien_X_2 = -1000000
        alien_Y_2 = -1000000
        alien_X_3 = -1000000
        alien_Y_3 = -1000000
        change_X = 0
        game_over_txt()
        print('Game Over')
    #Adds spaceship, alien spacecraft 1, alien spacecraft 2, alien spacecraft 3, and score images.
    screen.blit(Spaceship_Img, (spaceship_X, spaceship_Y))
    screen.blit(Space_Alien, (alien_X, alien_Y))
    screen.blit(Space_Alien_2, (alien_X_2, alien_Y_2))
    screen.blit(Space_Alien_3, (alien_X_3, alien_Y_3))
    score_txt()
    pygame.display.update()