import pygame
import random

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

enemyImg = pygame.image.load('enemy.png')
enemyX = random.randint(0, 736)
enemyY = 40
enemyX_change = 0.2
enemyY_change = 64

def enemy(x, y):
	screen.blit(enemyImg, (x, y))

bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 0.4
bullet_state = "ready"

def fire_bullet(x, y):
	global bullet_state
	bullet_state =  "fire"
	screen.blit(bulletImg, (x + 16, y))


running = True
while running:
	screen.fill((32, 32, 32))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				playerX_change = -0.2
			if event.key == pygame.K_RIGHT:
				playerX_change = 0.2
			if event.key == pygame.K_SPACE and bullet_state == "ready":
				bulletX = playerX # we need to add this this step as without this step bullet will change the coordinates with player
				fire_bullet(bulletX, bulletY)
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				playerX_change = 0

	playerX += playerX_change

	if playerX >= 736:
		playerX = 736
	elif playerX <= 0:
		playerX = 0

	enemyX += enemyX_change

	if enemyX >= 736:
		enemyX_change = -0.2
		enemyY += enemyY_change
	elif enemyX <= 0:
		enemyX_change = 0.2
		enemyY += enemyY_change

	# adding it so that multiple bullets can be fired
	if bulletY <= 0:
		bulletY = 480
		bullet_state = "ready"
	
	# bullet movements
	if bullet_state is "fire":
		fire_bullet(bulletX, bulletY)
		bulletY -= bulletY_change

	player(playerX, playerY)
	enemy(enemyX, enemyY)
	pygame.display.update()