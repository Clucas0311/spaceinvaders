import pygame
import random

pygame.init()  # initialize pygame
screen = pygame.display.set_mode((800, 600))  # size of the window(w x l)

pygame.display.set_caption("Space Invaders")  # Title and display
icon = pygame.image.load('alien.png')
pygame.display.set_icon(icon)

# Player
player_img = pygame.image.load('space-invaders.png')
playerX = 370  # ship position left and right
playerY = 480  # ship postion  top to bottom
playerX_change = 0

# Enemy position
enemy_img = pygame.image.load('ufo.png')
enemyX = random.randint(0, 800)  # alien position at postion (wideness) generates at random
enemyY = random.randint(50, 150)  # alien postion at random   (lenght) generates at random
enemyX_change = 1
enemyY_change = 40


def player(x, y):
    # screen.blit means to draw the image on the screen
    screen.blit(player_img, (x, y))


def enemy(x, y):
    # screen.blit means to draw the image on the screen
    screen.blit(enemy_img, (x, y))


    # it needs three parameters the image, and the coordinates of the player
game_loop = True
while game_loop:
    screen.fill((0, 0, 0))  # colors in RGB

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False

            # If key stoke has been pressed check whether its right or left
        if event.type == pygame.KEYDOWN:  # to check if a key has been pressed  down
            if event.key == pygame.K_LEFT:  # check the key that is pressed is a left arrow
                # When the player moves to the left it is dcremented and increase the point sytem as well to make it go faster
                playerX_change = -1
            if event.key == pygame.K_RIGHT:
                playerX_change = 1  # When the player moves to the right it increases
        if event. type == pygame.KEYUP:  # Key is released
            if event.key == pygame.K_LEFT or event.key == pygame. K_RIGHT:
                playerX_change = 0  # to make space ship be at motionless

    playerX += playerX_change  # use this to increase the value of player X as the change moves
    # Create a boundary for the ship so it does move off the screen
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    enemyX += enemyX_change  # use this to increase the value of player X as the change moves
    # Create a boundary for the enemy so it does move off the screen
    if enemyX <= 0:  # When the enemy hits the boundary  from the left side
        enemyX_change = 0.3  # The enemy will move to the right  to the right direction
    elif enemyX >= 736:  # When enemy hits boundary on the right
        enemyX_change = -0.3  # Will then move in diection of the negative side
        enemyY += enemyY_change  # Enemy will move down everytime the enemy hits the boundary

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()  # updates the window requirement
