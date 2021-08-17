import pygame
import random

# This game consists of 3 enemies, 1 player and a prize.
# The player has to move from one side of the screen to the opposite side to
# reach the prize without colliding with any of the enemies,
# and before the enemies reach the edges of the screen's display, if they do,
# The player loses the game. If he reaches the prize before that he wins.

# The method pygame.init() is used to initialize all the imported modules, (Shinners, n.d).

pygame.init()

# These first to variables hold the values for the display screen's height and width
# They're placed in the argument of the pygame.display.set.mode function for the display set up,(Kenlon, 2017).

screen_width = 1520
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))

# These variables represent the player's, enemies and the prize (their images).
# The pygame.image.load() function loads image of the player, enemies or prize so they can be utilized in the game, (Kenlon, 2017).

player = pygame.image.load("player.jpg")
star = pygame.image.load("image.png")
ghost = pygame.image.load("monster.jpg")
skull = pygame.image.load("enemy.png")
prize = pygame.image.load("prize.jpg")

# These variables contain the width and height of the player's images, which are later used to keep images in the display screen
# The values of the width and height were obtain using the get_height() and get_width_function, (Built-in objecs, n.d).

player_height = player.get_height()
player_width = player.get_width()

star_height = star.get_height()
star_width = star.get_width()

ghost_height = ghost.get_height()
ghost_width = ghost.get_width()

skull_height = skull.get_height()
skull_width = skull.get_width()

prize_height = prize.get_height()
prize_width = prize.get_width()


# These two variables determine our player's starting position
# Variable 'step' is used to increase the player's postion depending on which direction they choose to go.

playerXPosition = 0
playerYPosition = 450

steps = 50  #the images move by pixels so 50 was suffient for faster/ more visible movement

# These next six variables determine the value's of the enemies' starting positons. Their x or y positions are completely random
# but subtracting the enemy image's height from the screen's height or image's width from screen's width
# ensures they always appear within the screen when the game starts.
# Each enemy moves in a different direction when the game begins and they also start a different positions when the game begins

starXPosition =  random.randint(0, screen_width - star_width)
starYPosition =  950

ghostXPosition =  random.randint(0, screen_width - ghost_width)
ghostYPosition =  0

skullXPosition =  screen_width - skull_width
skullYPosition =  random.randint(0, screen_height - skull_height)

# prize only changes position vertically but not horizintally since player has to reach it from the opposite end of the display.

prizeXPosition =  screen_width - prize_width
prizeYPosition =  random.randint(0, screen_height - prize_height)


# the game runs in a while main loop with a True boolean value, enuring loop always continues unless there's a prompt to stop like losing the game
# or winning the prize. In each iteration, the loop will check whether any events in the loop occured (i.e if keys have been pressed or if the user has pressed quit)
# and it will keep updating to reflect those events.

while 1:
    
    # this function determines the color of the background of our games display, the arguments produce a dark blue color, (Built-in objecs, n.d)
    screen.fill((0,0,80))

    # screen.blit funtion allows us to draw images to the screen, (Built-in objecs, n.d).
    
    screen.blit(player, (playerXPosition, playerYPosition))
    screen.blit(star, (starXPosition, starYPosition))
    screen.blit(ghost, (ghostXPosition, ghostYPosition))
    screen.blit(skull, (skullXPosition, skullYPosition))
    screen.blit(prize, (prizeXPosition, prizeYPosition))

    pygame.display.flip()  # this function updates the screen to replect changes/actions made, (Kenlon, 2017).

    # the following loop is the player's control keys. Loop uses if statements to keep checking which key is pressed or if the player has quit.
    # if they quit it will exit the game
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        # if the player presses a control key the variable 'step' will be subtracted or added to the value of the player's x or y position.
        # depending on the direction of the key pressed, (Kenlon, 2017)
        
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_LEFT:
                playerXPosition -= steps
            if event.key == pygame.K_RIGHT:
                playerXPosition += steps
            if event.key == pygame.K_UP:
                playerYPosition -= steps
            if event.key == pygame.K_DOWN:
                playerYPosition += steps

        # If the key is released the player will stop moving and no value will be added to the player's position variable, (Kenlon, 2017).
        
        if event.type == pygame.KEYUP:
            
            if event.key == pygame.K_LEFT:
                playerXPosition += 0
            if event.key == pygame.K_RIGHT:
                playerXPosition -= 0
            if event.key == pygame.K_UP:
                playerXPosition -= 0
            if event.key == pygame.K_DOWN:
                playerXPosition += 0
        
    # The Rect function is used to create boundaries around the images, that are defined by their positions
    # these boudaries allow us to use the colliderect() function which in a codition will deteremine what
    # happens when the images collide (i.e when their boudaries touch), (Built-in objecs, n.d).
    
    playerBox = pygame.Rect(player.get_rect())
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition
         
    starBox = pygame.Rect(star.get_rect())
    starBox.top = starYPosition
    starBox.left = starXPosition

    skullBox = pygame.Rect(skull.get_rect())
    skullBox.top = skullYPosition
    skullBox.left = skullXPosition

    ghostBox = pygame.Rect(ghost.get_rect())
    ghostBox.top = ghostYPosition
    ghostBox.left = ghostXPosition

    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition

    # These conditions set the outcome if the player collides with an enemy  or the enemy(image) reaches edge of display screen
    # the player loses and the game ends.
    
    if (playerBox.colliderect(starBox)) or starYPosition < 0 - star_height:
        print("You lose!")
        pygame.quit()
        exit(0)

    if (playerBox.colliderect(skullBox)) or skullXPosition < 0 - skull_width:
        print("You lose!")
        pygame.quit()
        exit(0)

    if (playerBox.colliderect(ghostBox)) or ghostXPosition < 0 + ghost_height:
        print("You lose!")
        pygame.quit()
        exit(0)

    # This conditions sets an outcome for when the player reaches the prize, in which case he will win and the game ends.
    
    if (playerBox.colliderect(prizeBox)):
        print("Congatulations, You win!")
        pygame.quit()
        exit(0)
        
    # These variables control the enemies movement. They are placed within the loop so that enemy images keep moving
    # by themselves. A value of 0.15 will be subtracted or added to enemy's x or y postion which each iteration of the loop.
    
    skullXPosition -= 0.15  
    ghostYPosition += 0.15
    starYPosition -= 0.15







# ***Reference list:

# Kenlon, S 2017, Using pygame to move your character around, viewed 20 July 2021 <https://opensource.com/article/17/12/game-python-moving-player>
# Built-in objects, n.d, viewed 19 July 2021, <https://pygame-zero.readthedocs.io/en/stable/builtins.html>.
# Shinners, P n.d, Line by line Chimp, viewed 19 July 2021, <https://www.pygame.org/docs/tut/ChimpLineByLine.html>.
