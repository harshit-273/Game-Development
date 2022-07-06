import pygame
import random
import math
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((800, 600)) 

# background sound
mixer.music.load('background.wav')
mixer.music.play(-1)

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

# multiple enemies

enemyImgs = []
enemyXs = []
enemyYs = []
enemyXs_changes = []
enemyYs_changes = []
no_of_enemies = 6

for i in range(no_of_enemies):
	enemyImgs.append(pygame.image.load('enemy.png'))
	enemyXs.append(random.randint(0, 736))
	enemyYs.append(40)
	enemyXs_changes.append(0.2)
	enemyYs_changes.append(64)


def enemy(x, y, i):
	screen.blit(enemyImgs[i], (x, y))

bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 0.4
bullet_state = "ready"

# score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

def show_score(x, y):
	score = font.render("Score: " + str(score_value), True, (255, 255, 255))
	screen.blit(score, (x, y))

def fire_bullet(x, y):
	global bullet_state
	bullet_state =  "fire"
	screen.blit(bulletImg, (x + 16, y))

def isCollision(enemyX, enemyY, bulletX, bulletY, bullet_state):
	distance = math.sqrt(math.pow((enemyX - bulletX), 2) + math.pow((enemyY - bulletY), 2))
	if distance < 27 and bullet_state == "fire":
		return True
	return False

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
				fire_sound = mixer.Sound('laser.wav')
				fire_sound.play()
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

	for i in range(no_of_enemies):
		enemyXs[i] += enemyXs_changes[i]
		if enemyXs[i] >= 736:
			enemyXs_changes[i] = -0.2
			enemyYs[i] += enemyYs_changes[i]
		elif enemyXs[i] <= 0:
			enemyXs_changes[i] = 0.2
			enemyYs[i] += enemyYs_changes[i]

		# collision
		collision  = isCollision(enemyXs[i], enemyYs[i], bulletX, bulletY, bullet_state)
		if collision:
			explosion_sound = mixer.Sound('explosion.wav')
			explosion_sound.play()
			bulletY = 480
			bullet_state = "ready"
			score_value += 1
			enemyXs[i] = random.randint(0, 736)
			enemyYs[i] = 40
		
		enemy(enemyXs[i], enemyYs[i], i)


	# adding it so that multiple bullets can be fired
	if bulletY <= 0:
		bulletY = 480
		bullet_state = "ready"
	
	# bullet movements
	if bullet_state is "fire":
		fire_bullet(bulletX, bulletY)
		bulletY -= bulletY_change

	player(playerX, playerY)
	show_score(textX, textY)
	pygame.display.update()