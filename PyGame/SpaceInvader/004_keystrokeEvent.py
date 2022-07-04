import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

playerImg = pygame.image.load('player.png')
playerX = 368
playerY = 530
playerX_change = 0
playerY_change = 0

def player(x, y):
	screen.blit(playerImg, (x, y))

running = True
while running:
	screen.fill((32, 32, 32))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		
		# keystroke events
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				playerX_change = -0.2
			if event.key == pygame.K_RIGHT:
				playerX_change = 0.2
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				playerX_change = 0

	playerX += playerX_change
	player(playerX, playerY)
	pygame.display.update()