import pygame

pygame.init()  # initialize pygame
screen = pygame.display.set_mode((800, 600))  # size of the window

pygame.display.set_caption("Blue Screen")  # Title and display
icon = pygame.image.load('alien.png')
pygame.display.set_icon(icon)

# Player
player_img = pygame.image.load('rocket.png')
playerX = 370  # ship position at postion x coodinate (800) length
playerY = 480  # ship postion at y coordinates the (600) widith


def player():
    # screen.blit means to draw the image on the screen
    screen.blit(player_img, (playerX, playerY))

    # it needs three parameters the image, and the coordinates of the player
game_loop = True
while game_loop:
    screen.fill((0, 0, 0))  # colors in RGB

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False
    player()
    pygame.display.update()  # updates the window requirement
