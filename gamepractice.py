import pygame
import random
import math
from pygame import mixer  # allows us to import music into pygame

pygame.init()  # initialize pygame
screen = pygame.display.set_mode((800, 600))  # size of the window(w x l)

# Backgrond image
background = pygame.image.load("background.png")
pygame.display.set_caption("Space Invaders")  # Title and display
icon = pygame.image.load('alien.png')
pygame.display.set_icon(icon)

# Background sound
mixer.music.load('background.wav')  # uploads music
mixer.music.play(-1)  # plays music add minus one to play on loop

# Player
player_img = pygame.image.load('space-invaders.png')
playerX = 370  # ship position left and right
playerY = 480  # ship postion  top to bottom
playerX_change = 0

# Enemy position
enemy_img = []  # create an empty list to put enemies into it
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):  # create a loop to append items to list so multple enemies can occur
    enemy_img .append(pygame.image.load('ufo.png'))
    # alien position at postion (wideness) generates at random
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))  # alien postion at random   (lenght) generates at random
    enemyX_change.append(5)
    enemyY_change.append(40)

# Bullet position

# Ready - You can't see the bullet on the screen
# Fire - The Bullet is currently moving
bullet_img = pygame.image.load('bullet.png')
bulletX = 0  # alien position at postion (wideness) generates at random
bulletY = 480  # bullet needs to be shot at the top the ship which is about 480
bulletX_change = 0
bulletY_change = 10
bullet_state = 'ready'

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)  # selection of the font and the size

# Created x and y coordinates of the font where we want it to appear
textX = 10
textY = 10


def show_score(x, y):
    # Render the font how we wanted it to display on the screen
    # and chose the score value and the color we wanted to appear
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    # drew the score on the screen
    screen.blit(score, (x, y))


def player(x, y):
    # screen.blit means to draw the image on the screen
    screen.blit(player_img, (x, y))


def enemy(x, y, i):
    # screen.blit means to draw the image on the screen
    screen.blit(enemy_img[i], (x, y))


def fire_bullet(x, y):
    global bullet_state  # make it global to access bullet state from inside the function
    bullet_state = "fire"
    # draw the image on the screen and the coordinates we want it to appear
    screen.blit(bullet_img, (x + 16, y + 10))  # plus 16 to appear above it in the middle of ship


# Created a distance formula for the hitting of the bullet with the ship
def is_collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# Game loop
game_loop = True
while game_loop:
    screen.fill((0, 0, 0))  # colors in RGB
    # Background image drawn on screan
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False

            # If key stoke has been pressed check whether its right or left
        if event.type == pygame.KEYDOWN:  # to check if a key has been pressed  down
            if event.key == pygame.K_LEFT:  # check the key that is pressed is a left arrow
                # When the player moves to the left it is dcremented and increase the point sytem as well to make it go faster
                playerX_change = -7
            if event.key == pygame.K_RIGHT:
                playerX_change = 7  # When the player moves to the right it increases
            if event.key == pygame.K_SPACE:  # When player hits the space button
                if bullet_state is "ready":  # When you first hit the spacebar it check if bullet is on the screen or not
                    bullet_sound = mixer.Sound("laser.wav")
                    bullet_sound.play()
                    # if not on the screen it would then get the x coodinate of the spaceship
                    bulletX = playerX  # Once the space has been pressed we save the current bullet x coodinate in the playerX position
                    fire_bullet(bulletX, bulletY)  # Fire bullet is triggerd

        if event. type == pygame.KEYUP:  # Key is released
            if event.key == pygame.K_LEFT or event.key == pygame. K_RIGHT:
                playerX_change = 0  # to make space ship be at motionless

# Player movement
    playerX += playerX_change  # use this to increase the value of player X as the change moves
    # Create a boundary for the ship so it does move off the screen
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

# Enemy movement
    for i in range(num_of_enemies):  # index so we can determine which enemy is which
        # use this to increase the value of player X as the change moves
        enemyX[i] += enemyX_change[i]
        # Create a boundary for the enemy so it does move off the screen
        if enemyX[i] <= 0:  # When the enemy hits the boundary  from the left side
            enemyX_change[i] = 5  # The enemy will move to the right  to the right direction
            enemyY += enemyY_change  # As enemy changes it moves the player down
        elif enemyX[i] >= 736:  # When enemy hits boundary on the right
            enemyX_change[i] = -5  # Will then move in diection of the negative side
            # Enemy will move down everytime the enemy hits the boundary
            enemyY[i] += enemyY_change[i]

            # Collision
        collision = is_collision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:  # if a collision has a occured
            explosion_sound = mixer.Sound("explosion.wav")
            explosion_sound.play()
            bulletY = 480  # Reset Y coordinate to 480 - starting location of spaceship
            bullet_state = "ready"  # Get The bullet state back in to ready to fire once again
            score_value += 1  # increase the value of the score by one everytime we hit our enemy
            # When you shoot the enemy he responds into a new place
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)
        enemy(enemyX[i], enemyY[i], i)

# Bullet movement
    if bulletY <= 0:  # When the bullet shot is less than zero
        bulletY = 480  # reset the bullet to 480
        bullet_state = "ready"  # The bullt state is at ready, so you are allowed to shoot again
    if bullet_state is "fire":  # if the state of the bullet is fire/space bar pressed
        fire_bullet(bulletX, bulletY)  # move the bullet in postion of the spaceship
        bulletY -= bulletY_change  # bullet is going upward * So Y coordinate must decrease

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()  # updates the window requirement
