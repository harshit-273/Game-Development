import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

# title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
    # screen color
	screen.fill((32, 32, 32))
	pygame.display.update()