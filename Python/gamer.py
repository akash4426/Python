import pygame 
from pygame.locals import *
import random

pygame.init()

clock = pygame.time.Clock()
fps = 60
h=720
w=1080

screen = pygame.display.set_mode((1080,720))
pygame.display.set_caption('Plane Crash Simulator')


#variables
plat_scroll = 0
flight = False
game_over = False
tower_freq = 1750
last_render = pygame.time.get_ticks() - tower_freq


#assets
bg = pygame.image.load('citybackdrop-upscale (1).jpg')
platform_img = pygame.image.load('1920x1080-black-solid-color-background.jpg')


class Plane(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('plane-removebg-preview.png')
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]
		self.vel = 0
		self.clicked = False

	def update(self):

		if flight == True:
			#gravity
			self.vel += 0.5
			if self.vel > 7:
				self.vel = 7
			if self.rect.bottom < 670:
				self.rect.y += int(self.vel)

		if game_over == False:
			#boost
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				self.vel = -10
			if pygame.mouse.get_pressed()[0] == 0:
				self.clicked = False



class Building(pygame.sprite.Sprite):
	def __init__(self, x, y, position):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('images-gigapixel-art-scale-6_00x.png')
		self.rect = self.image.get_rect()
		self.rect.topleft=[x,y]

	def update(self):
		self.rect.x -= 5




plane_group = pygame.sprite.Group()
tower_group = pygame.sprite.Group()

boeing = Plane(75, int(720 / 3))

plane_group.add(boeing)



run = True
while run:

	clock.tick(fps)

	#draw background
	screen.blit(bg, (0,0))

	plane_group.draw(screen)
	plane_group.update()
	tower_group.draw(screen)

	#draw the ground
	screen.blit(platform_img, (plat_scroll, 620))

	if pygame.sprite.groupcollide(plane_group, tower_group, False, False) or boeing.rect.bottom < 0:
		game_over = True

	if boeing.rect.bottom > 670:
		game_over = True
		flight = False


	if game_over == False and flight == True:

		time_now = pygame.time.get_ticks()
		if time_now - last_render > tower_freq:
			random_height = random.randint(-100,25)
			btm_tower = Building(1080,670 // 2.8 + random_height,1)
			tower_group.add(btm_tower)
			last_render = time_now


		plat_scroll -= 5
		if abs(plat_scroll) > 40:
			plat_scroll = 0
		tower_group.update()

	

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.MOUSEBUTTONDOWN and flight == False and game_over == False:
			flight = True

	pygame.display.update()

pygame.quit()