import pygame

pygame.init()  # initialize pygame
screen = pygame.display.set_mode((800, 600))  # size of the window

pygame.display.set_caption("Space Invaders")  # Title and display
icon = pygame.image.load('alien.png')
pygame.display.set_icon(icon)

# Player
player_img = pygame.image.load('space-invaders.png')
playerX = 370  # ship position at postion x coodinate (800) length
playerY = 480  # ship postion at y coordinates the (600) widith
playerX_change = 0


def player(x, y):
    # screen.blit means to draw the image on the screen
    screen.blit(player_img, (x, y))

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
        if event. type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame. K_RIGHT:
                playerX_change = 0  # to make space ship be at a standstill

    playerX += playerX_change  # use this to increase the value of player X as the change moves
    # Create a boundary for the ship so it does move off the screen
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    player(playerX, playerY)
    pygame.display.update()  # updates the window requirement
