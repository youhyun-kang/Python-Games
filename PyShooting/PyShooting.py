import pygame
import sys
import os
folder = os.chdir(r'C:\Users\youhy\OneDrive\Desktop\Projects\Spaceship\PyShooting')
import random
from time import sleep


padWidth = 480
padHeight = 640

rockImage = ['rock01.png','rock02.png','rock03.png','rock04.png','rock05.png',\
			'rock06.png','rock07.png','rock08.png','rock09.png','rock10.png',\
			'rock11.png','rock12.png','rock13.png','rock14.png','rock15.png',\
			'rock16.png','rock17.png','rock18.png','rock19.png','rock20.png',\
			'rock21.png','rock22.png','rock23.png','rock24.png','rock25.png',\
			'rock26.png','rock27.png','rock28.png','rock29.png','rock30.png']

explosionSound = ['explosion01.wav', 'explosion02.wav', 'explosion03.wav', 'explosion04.wav']

def writeScore(count):
	global gamePad
	font = pygame.font.Font('NanumGothic.ttf', 20)
	text = font.render('Rocks destroyed: ' + str(count), True, (255,255,255))
	gamePad.blit(text, (10, 0))

def writePassed(count):
	global gamePad
	font = pygame.font.Font('NanumGothic.ttf', 20)
	text = font.render('Rocks Passed: ' + str(count), True, (255,0,0))
	gamePad.blit(text, (320, 0))

def writeMessage(text):
	global gamePad, gameOverSound
	textfont = pygame.font.Font('NanumGothic.ttf', 45)
	text = textfont.render(text, True, (255, 0, 0))
	textpos= text.get_rect()
	textpos.center= (padWidth/2, padHeight/2)
	gamePad.blit(text, textpos)
	pygame.display.update()
	pygame.mixer.music.stop()
	gameOver.Sound.play()
	sleep(2)
	pygame.mixer.music.play()
	runGame()

def writeMessage2(text):
	global gamePad, gameOverSound
	textfont = pygame.font.Font('NanumGothic.ttf', 60)
	text = textfont.render(text, True, (255, 0, 0))
	textpos= text.get_rect()
	textpos.center= (padWidth/2, padHeight/2)
	gamePad.blit(text, textpos)
	pygame.display.update()
	pygame.mixer.music.stop()
	gameOver.Sound.play()
	sleep(2)
	pygame.mixer.music.play()
	runGame()

def crash():
	global gamePad
	writeMessage('Spaceship Destroyed!')

def gameOver():
	global gamePad
	writeMessage2('GAME OVER')

def drawObject(obj, x, y):
	global gamePad
	gamePad.blit(obj, (x,y))

def initGame():
	global gamePad, clock, background, fighter, missile, explosion, missileSound, gameOverSound
	pygame.init()
	gamePad = pygame.display.set_mode((padWidth, padHeight))
	pygame.display.set_caption('Spaceship')
	background = pygame.image.load('background.png')
	fighter = pygame.image.load('fighter.png')
	missile = pygame.image.load('missile.png')
	explosion = pygame.image.load('explosion.png')
	pygame.mixer.music.load('music.wav')
	pygame.mixer.music.play(-1)
	missileSound = pygame.mixer.Sound('missile.wav')
	gameOverSound = pygame.mixer.Sound('gameover.wav')
	clock = pygame.time.Clock()

def runGame():
	global gamepad, clock, background, fighter, missile, explosion, missileSound

	fighterSize = fighter.get_rect().size
	fighterWidth = fighterSize[0]
	fighterHeight = fighterSize[1]

	x = padWidth * 0.45
	y = padHeight * 0.9
	fighterX = 0 

	missileXY = []

	rock = pygame.image.load(random.choice(rockImage))
	rockSize = rock.get_rect().size
	rockWidth = rockSize[0]
	rockHeight = rockSize[1]
	destroySound = pygame.mixer.Sound(random.choice(explosionSound))

	rockX = random.randrange(0, padWidth - rockWidth)
	rockY = 0
	rockSpeed = 2

	isShot = False
	shotCount = 0
	rockPassed = 0

	onGame = False
	while not onGame:
		for event in pygame.event.get():
			if event.type in [pygame.QUIT]: #Quit Program
				pygame.quit()
				sys.exit()
			
			if event.type in [pygame.KEYDOWN]:
				if event.key == pygame.K_LEFT:
					fighterX -= 5 

				elif event.key == pygame.K_RIGHT:
					fighterX += 5

				elif event.key == pygame.K_SPACE:
					missileSound.play()
					missileX = x + fighterWidth / 2
					missileY = y - fighterHeight
					missileXY.append([missileX, missileY])


			if event.type in [pygame.KEYUP]:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					fighterX = 0

		drawObject(background, 0, 0)

		x += fighterX
		if x < 0:
			x = 0
		elif x > padWidth - fighterWidth:
			x = padWidth - fighterWidth
		
		if y < rockY + rockHeight:
			if(rockX > x and rockX < x + fighterWidth) or \
				(rockX + rockWidth > x and rockX + rockWidth < x + fighterWidth):
				crash()

		drawObject(fighter, x, y)

		if len(missileXY) != 0:
			for i, bxy in enumerate(missileXY):
				bxy[1] -= 10
				missileXY[i][1] = bxy[1]

				if bxy[1] < rockY:
					if bxy[0] > rockX and bxy [0] < rockX + rockWidth:
						missileXY.remove(bxy)
						isShot = True
						shotCount += 1
					
				if bxy[1] <=0:
					try:
						missileXY.remove(bxy)
					except:
						pass
		
		if len(missileXY) != 0:
			for bx, by in missileXY:
				drawObject(missile, bx, by)

		writeScore(shotCount)
		
		rockY += rockSpeed

		#When rock falls on Earth
		if rockY > padHeight:
			rock = pygame.image.load(random.choice(rockImage))
			rockSize = rock.get_rect().size
			rockWidth = rockSize[0]
			rockHeight = rockSize[1]
			rockX = random.randrange(0, padWidth - rockWidth)
			rockY = 0
			rockPassed += 1

		if rockPassed == 3:
			gameOver()
		
		writePassed(rockPassed)
		
		if isShot:
			drawObject(explosion, rockX, rockY)
			destroySound.play()

			rock = pygame.image.load(random.choice(rockImage))
			rockSize = rock.get_rect().size
			rockWidth = rockSize[0]
			rockHeight = rockSize[1]
			rockX = random.randrange(0, padWidth - rockWidth)
			rockY = 0
			destroySound = pygame.mixer.Sound(random.choice(explosionSound))
			isShot = False
		
			rockSpeed += 0.2
			if rockSpeed >= 10:
				rockSpeed + 10

		drawObject(rock, rockX, rockY)
		
		pygame.display.update()	#Game Background Redrawn

		clock.tick(60)

	pygame.quit() 				#Quit pygame


initGame()
runGame()

