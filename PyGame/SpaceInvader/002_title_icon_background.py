import pygame

# Initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('Spaceship.png')
pygame.display.set_icon(icon)

# Game Loop
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
    # screen color
	screen.fill((32, 32, 32))
	pygame.display.update()