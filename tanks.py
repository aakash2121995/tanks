import pygame,time
import random
pygame.init()

display_width = 800
display_height = 600

FPS = 30

DISPLAY = pygame.display.set_mode((display_width,display_height))

fire_sound = pygame.mixer.Sound("tank-fire.wav")
gameover_sound = pygame.mixer.Sound("gameover.wav")

l_explosion = pygame.mixer.Sound("le.wav")


pygame.display.set_caption("Tanks")

blue = (0,0,255)
purple = (200,30,200)
red = (200,0,0)
light_red = (255,0,0)
white =  (255,255,255)
black = (0,0,0)
green = (0,180,0)
light_green = (0,255,0)
yellow = (200,200,0)
light_yellow = (255,255,0)
ground_height = 35

tankWidth = 40
tankHeight = 20

turretWidth = 5
wheelWidth = 5
clock = pygame.time.Clock()

button_font = pygame.font.Font("jokerman.ttf", 25)
smallfont = pygame.font.Font("comic.ttf", 25)
medfont = pygame.font.Font("comic.ttf", 40)
largefont = pygame.font.Font("jokerman.ttf", 80)

def tank(x,y,turpos):
	x = int(x)
	y = int(y)
	startX = 15
	
	possibleTurrets = [(x-27,y-2),(x-26,y-5),(x-25,y-8),(x-23,y-11),(x-20,y-13),(x-18,y-16),(x-16,y-18),(x-13,y-20),(x-11,y-21),(x-9,y-22),(x-6,y-22)]
	
	
	pygame.draw.circle(DISPLAY, black,(x,y),tankHeight/2)
	pygame.draw.rect(DISPLAY, black ,( x - tankHeight,y,tankWidth,tankHeight))
	
	pygame.draw.line(DISPLAY,black,(x,y),possibleTurrets[turpos],turretWidth)
	
	for i in range(7):
		pygame.draw.circle(DISPLAY,black,(x-startX,y+20),wheelWidth)
		startX -= 5
		
	return possibleTurrets[turpos]

def enemy_tank(x,y,turpos):
	x = int(x)
	y = int(y)
	startX = 15
	
	possibleTurrets = [(x+27,y-2),(x+26,y-5),(x+25,y-8),(x+23,y-11),(x+20,y-13),(x+18,y-16),(x+16,y-18),(x+13,y-20),(x+11,y-21),(x+9,y-22),(x+6,y-22)]
	
	
	pygame.draw.circle(DISPLAY, black,(x,y),tankHeight/2)
	pygame.draw.rect(DISPLAY, black ,( x - tankHeight,y,tankWidth,tankHeight))
	
	pygame.draw.line(DISPLAY,black,(x,y),possibleTurrets[turpos],turretWidth)
	
	for i in range(7):
		pygame.draw.circle(DISPLAY,black,(x-startX,y+20),wheelWidth)
		startX -= 5
		
	return possibleTurrets[turpos]

		
def introgame():
	
	pygame.mixer.music.load("intro3.mp3")
	pygame.mixer.music.play(-1)
	
	
	intro = True
	DISPLAY.fill(white)
	while intro:
		for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						pygame.quit()
						quit()
					elif event.key == pygame.K_c:
						intro = False
				elif event.type == pygame.QUIT:
						pygame.quit()
						quit()
	
		message ("Welcome to Tanks!",green,-120,largefont)
		message ("The objective is to shoot and destroy",black,-30)
		message ("the enemy tank before they destroy you.",black)
		message ("The more enemies you destroy, harder it gets",black,40)

		button("Play",150,500,100,50,light_green,green,"Play")
		button("Controls",350,500,130,50,light_yellow,yellow,"Controls")
		button("Quit",550,500,100,50,light_red,red,"Quit")
		pygame.display.update()
	
def game_over():
	
	pygame.mixer.music.load("gameover.wav")
	pygame.mixer.music.play(0)
	gameover = True
	DISPLAY.fill(white)
	while gameover:
		for event in pygame.event.get():
				
				if event.type == pygame.QUIT:
						gameover = False
						pygame.quit()
						quit()
	
		message ("Game Over!",green,-120,largefont)
		message ("You Died.",black,-40,medfont)
		

		button("Play Again",125,500,150,50,light_green,green,"Play")
		button("Controls",375,500,130,50,light_yellow,yellow,"Controls")
		button("Quit",600,500,80,50,light_red,red,"Quit")
		pygame.display.update()	
	
def you_win():
	
	pygame.mixer.music.load("youwin.mp3")
	pygame.mixer.music.play(0)
	
	win = True
	DISPLAY.fill(white)
	while win:
		for event in pygame.event.get():
				
				if event.type == pygame.QUIT:
						win = False
						pygame.quit()
						quit()
	
		message ("Congratulations !!!",green,-120,largefont)
		message ("You Won.",black,-30,medfont)
		

		button("Play Again",125,500,150,50,light_green,green,"Play")
		button("Controls",375,500,130,50,light_yellow,yellow,"Controls")
		button("Quit",600,500,80,50,light_red,red,"Quit")
		pygame.display.update()	
	


def message(msg,color,y_displace=0,Font_type=smallfont,x_displace=0):
	
	textSurf=  Font_type.render(msg,True,color)
	
	rect = textSurf.get_rect()
	rect.center = (display_width/2)+x_displace,(display_height/2)+ y_displace
	
	DISPLAY.blit(textSurf,rect)
	pygame.display.update()	
	
def healthbar(player_health,enemy_health):
	if player_health > 66:
		p_color = green
	elif 66>=player_health > 33:
		p_color = light_yellow
	else:
		p_color = red
	
	if enemy_health > 66:
		e_color = green
	elif 66>= enemy_health > 33:
		e_color = light_yellow
	else:
		e_color = red
		
	pygame.draw.rect(DISPLAY,p_color,(680,25,player_health,25))
	pygame.draw.rect(DISPLAY,e_color,(20,25,enemy_health,25))	
	

def pauseGame():
	pause = True
	
	message("Paused",black,-70,largefont)
	message("Press C to continue or Q to quit",black,15,medfont)
	while pause:
		for event in pygame.event.get():
						if event.type == pygame.KEYDOWN:
							if event.key == pygame.K_q:
								pygame.quit()
								quit()
							elif event.key == pygame.K_c:
								pause = False
						
						elif event.type == pygame.QUIT:
								pygame.quit()
								quit()

def button(msg,x,y,width,height,active_color,inactive_color,action = None):
	
	cur = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	color = inactive_color
	if x + width > cur[0] > x and y + height > cur[1] > y:
		if click[0] and action != None :
			if action == "Play":
				gameloop()
			elif action == "Controls":
				game_controls()
			elif action == "Quit":
				pygame.quit()
				quit()
			elif action == "Main Menu":
				introgame()
			
		
		color = active_color
	
	pygame.draw.rect(DISPLAY,color,(x,y,width,height))
	
	message(msg,black,-display_height/2 + y + height/2,button_font,-display_width/2 + x +width/2)


def explosion(x,y,size=50):
	explode = True
	pygame.mixer.Sound.play(l_explosion)
	while explode:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		
		startPoint = x,y
		
		colorChoices = [red,yellow,light_red,purple,light_yellow,blue,light_yellow,red,]
		
		magnitude = 1
		
		while magnitude <size:
			exploding_x = x + random.randrange(-1*magnitude,magnitude)
			exploding_y = y + random.randrange(-1*magnitude,magnitude)
			
			pygame.draw.circle(DISPLAY,colorChoices[random.randrange(0,7)],(exploding_x,exploding_y),random.randrange(1,5))
			
			magnitude +=1
			
			pygame.display.update()
			clock.tick(100)
		explode = False
	

		
def fireshell (xy,x,y,turpos,shellPower,xlocation,barrier_width,randomHeight,enemyX,enemyY):
	fire = True
	
	pygame.mixer.Sound.play(fire_sound)
	
	startingShell = list(xy)
	
	con = 0
	damage = 0
	
	while fire:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
				
	
		pygame.draw.circle(DISPLAY, red,(startingShell[0],startingShell[1]),5)
		
	
		startingShell[0] -= int(11-turpos)*2
		
			
		
		startingShell[1] += int(((((startingShell[0]-xy[0])*0.01)**2))/(shellPower/50.0) - (turpos + turpos/(12-turpos)))
		
		if startingShell[1] > display_height - ground_height:
			
			hit_x = int(startingShell[0]*(display_height-ground_height)/startingShell[1])
			hit_y = display_height - ground_height
			
			if enemyX+10 > hit_x>enemyX-10:
					print("Critical Hit !")
					damage = 25
			elif enemyX+18 > hit_x>enemyX-18:
					print("Hard Hit !")
					damage = 18
			elif enemyX+25 > hit_x>enemyX-25:
					print("Good Hit !")
					damage = 10
			elif enemyX+35 > hit_x>enemyX-35:
					print("Light Hit !")
					damage = 5
			explosion(hit_x,hit_y)
			fire = False
			
		
			
		elif startingShell[0] < 0:
			fire = False
			
		check1 = startingShell[0] <= xlocation + barrier_width
		check2 = startingShell[0] >= xlocation
		check3 = startingShell[1] <= display_height
		check4 = startingShell[1] >= display_height - randomHeight
		
		if check1 and check2 and check3 and check4:
			hit_x = int(startingShell[0])
			hit_y = int(startingShell[1])
			print "Impact",hit_x,hit_y
	
			explosion(hit_x,hit_y)
			fire = False
							
		pygame.display.update()
		clock.tick(30)
	return damage
		
def e_fireshell (xy,x,y,xlocation,barrier_width,randomHeight,playerX,playerY):
	
	damage = 0
	power_found = False
	turpos = 7
	power = 101
	while not power_found:
		power -= 1
		
		fire = True
		startingShell = list(xy)
		
		if power <=0:
			turpos +=1
			power = 101
		
		if turpos <0:
			turpos = 0
			break;
						
		while fire:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
				
			startingShell[0] += int(11-turpos)*2
				
			
			startingShell[1] += int(((((startingShell[0]-xy[0])*0.01)**2))/(power/50.0) - (turpos + turpos/(12-turpos)))
			
			if startingShell[1] > display_height - ground_height:
				
				hit_x = int(startingShell[0]*(display_height-ground_height)/startingShell[1])
				hit_y = display_height - ground_height

				if playerX+15 > hit_x>playerX-15:
					power_found = True
					print "Target Acuired"
				fire = False
				
	
			check1 = startingShell[0] <= xlocation + barrier_width
			check2 = startingShell[0] >= xlocation
			check3 = startingShell[1] <= display_height
			check4 = startingShell[1] >= display_height - randomHeight
			
			if check1 and check2 and check3 and check4:
				hit_x = int(startingShell[0])
				hit_y = int(startingShell[1])
				
				fire = False
			
			elif startingShell[0] < 0:
				fire = False
				
		
			
	pygame.mixer.Sound.play(fire_sound)	
	power = random.randrange(int(power*0.8),int (power*1.2))
	
	fire = True
	
	startingShell = list(xy)	
	while fire:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
				
		
		pygame.draw.circle(DISPLAY, red,(startingShell[0],startingShell[1]),5)
		

		startingShell[0] += int(11-turpos)*2
			
		
		startingShell[1] += int(((((startingShell[0]-xy[0])*0.01)**2))/(power/50.0) - (turpos + turpos/(12-turpos)))
		
		if startingShell[1] > display_height - ground_height:
			
			hit_x = int(startingShell[0]*(display_height-ground_height)/startingShell[1])
			hit_y = display_height - ground_height
			
			if playerX+10 > hit_x>playerX-10:
					print("Critical Hit !")
					damage = 25
			elif playerX+18 > hit_x>playerX-18:
					print("Hard Hit !")
					damage = 18
			elif playerX+25 > hit_x>playerX-25:
					print("Good Hit !")
					damage = 10
			elif playerX+35 > hit_x>playerX-35:
					print("Light Hit !")
					damage = 5
			
			explosion(hit_x,hit_y)
			fire = False
			
		
			
		elif startingShell[0] < 0:
			fire = False
			
		check1 = startingShell[0] <= xlocation + barrier_width
		check2 = startingShell[0] >= xlocation
		check3 = startingShell[1] <= display_height
		check4 = startingShell[1] >= display_height - randomHeight
		
		if check1 and check2 and check3 and check4:
			hit_x = int(startingShell[0])
			hit_y = int(startingShell[1])
			print "Impact",hit_x,hit_y
			explosion(hit_x,hit_y)
			fire = False
			
		
		
	
		
		pygame.display.update()
		clock.tick(30)
		
	return damage

	
def game_controls():
		
	gcont = True
	DISPLAY.fill(white)
	while gcont:
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
						pygame.quit()
						quit()
	
		message ("Controls",green,-120,largefont)
		message ("Fire: Spacebar",black,-30)
		message ("Move turret: Up and Down arrows",black,10)
		message ("Move Tank: Left and Right arrows",black,50)
		message ("Power: A and D keys",black,90)
		message ("Pause: P",black,130)

		button("Play",150,500,100,50,light_green,green,"Play")
		button("Main Menu",325,500,150,50,light_yellow,yellow,"Main Menu")
		button("Quit",550,500,100,50,light_red,red,"Quit")
		pygame.display.update()
		
		
def barrier(x,randomHeight,width):
	
	pygame.draw.rect(DISPLAY, black, (x,display_height - randomHeight,width,randomHeight)) 

def gameloop():
	
	pygame.mixer.music.load("ocean-drift.wav")
	pygame.mixer.music.play(-1)
	
	
	global direction
	
	barrier_width = 50
	player_health = 100
	enemy_health = 100
	firePower = 50
	enemy_power = 60
	enemy_turpos = 8
	powerChange = 0
	turpos = 0
	mainTankX = display_width * 0.9
	mainTankY = display_height * 0.9
	
	enemyX = display_width * 0.1
	enemyY = display_height * 0.9
	
	gamexit = False
	gameover = False
	FPS = 15
	
	x = display_width/2 + random.randint(-0.1*display_width,0.1*display_width)
	randomHeight = random.randint(0.1*display_height,0.6*display_height)
	
	MoveTank = 0
	changeTurpos = 0
	
	
	while not gamexit:
		
		
		
		if gameover:
			
			message("Game over !",blue,-50,largefont)
			message("Press C to play again or Q to quit",black,50,medfont)
			
		while gameover:		
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						gameover = False
						gamexit = True
					elif event.key == pygame.K_c:
						gameloop()
				elif event.type == pygame.QUIT:
						gamexit = True 
						gameover = False		


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gamexit = True 
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					MoveTank = -5
					
				elif event.key == pygame.K_RIGHT:
					MoveTank = 5
				elif event.key == pygame.K_UP  :
					changeTurpos = 1
				elif event.key == pygame.K_DOWN:
					changeTurpos = -1
					
				elif event.key == pygame.K_p:
					pauseGame()
				elif event.key == pygame.K_SPACE:

					e_damage = fireshell(gun,mainTankX,mainTankY,turpos,firePower,x,barrier_width,randomHeight,enemyX,enemyY)
					
					possibleMovements = ['r','f']
					
					moveDirection = random.randrange(0,2)
					
					for y in range(random.randrange(1,10)):
						
						if display_width*0.3 > enemyX >= display_width*0.03:
							if possibleMovements[moveDirection] == 'f':
								enemyX += 5
							elif possibleMovements[moveDirection] == 'r':
								enemyX -= 5
							DISPLAY.fill(white)
							healthbar(player_health,enemy_health)
							gun = tank(mainTankX,mainTankY,turpos)
							enemy_gun = enemy_tank(enemyX,enemyY,enemy_turpos)
							
							barrier(x,randomHeight,barrier_width)
													
							DISPLAY.fill(green,rect = [0, display_height-ground_height,display_width,ground_height])
							
							message("Power: " + str(firePower) + '%',black,-display_height/2+ 40)
							
							pygame.display.update()
														
							clock.tick(FPS)	
							
						elif enemyX < display_width*0.03:
							enemyX += 5
							moveDirection = 1
							
							
							DISPLAY.fill(white)
							healthbar(player_health,enemy_health)
							gun = tank(mainTankX,mainTankY,turpos)
							enemy_gun = enemy_tank(enemyX,enemyY,enemy_turpos)
							
							barrier(x,randomHeight,barrier_width)
													
							DISPLAY.fill(green,rect = [0, display_height-ground_height,display_width,ground_height])
							
						
							message("Power: " + str(firePower) + '%',black,-display_height/2+ 40)
							
							pygame.display.update()
														
							clock.tick(FPS)	
					
					p_damage=e_fireshell(enemy_gun,enemyX,enemyY,x,barrier_width,randomHeight,mainTankX,mainTankY)
					player_health -= p_damage
					enemy_health -= e_damage
					
				elif event.key == pygame.K_a:
					powerChange = -1
				elif event.key == pygame.K_d:
					powerChange = 1

			
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					MoveTank = 0
				elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					changeTurpos = 0
				elif event.key == pygame.K_a or event.key == pygame.K_d:
					powerChange = 0
				
		if enemy_health < 1:
			you_win()	
		elif player_health < 1:
			game_over()

		mainTankX += MoveTank	
		turpos += changeTurpos	
		firePower += powerChange
		
		if turpos >9:
			turpos = 9
			changeTurpos = 0
		elif turpos <0 :
			turpos = 0
			changeTurpos = 0
			
			
		if firePower >100:
			firePower = 100
			powerChange = 0
			
		elif firePower <= 0 :
			firePower = 1
			powerChange = 0
			
			
		if mainTankX - tankWidth/2 < x + barrier_width:
			mainTankX += 5
			
			
		DISPLAY.fill(white)
		healthbar(player_health,enemy_health)
		gun = tank(mainTankX,mainTankY,turpos)
		enemy_gun = enemy_tank(enemyX,enemyY,enemy_turpos)
		
		barrier(x,randomHeight,barrier_width)
		DISPLAY.fill(green,rect = [0, display_height-ground_height,display_width,ground_height])
		
		message("Power: " + str(firePower) + '%',black,-display_height/2+ 40)
		
		pygame.display.update()
		
		clock.tick(FPS)	
		

	pygame.quit()
	quit()	
introgame()

