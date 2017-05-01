# import pygame
# pygame.init()
# song = pygame.mixer.Sound('abc.mp3')
# clock = pygame.time.Clock()
# song.play()
# while True:
#     clock.tick(60)
# pygame.quit()


import pygame, sys, datetime
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((500, 400))
screen.fill((49, 26, 65))
pygame.display.set_caption("TESTIFICATE")
if datetime.date.today().month == 12 and datetime.date.today().day == 25:
    pygame.mixer.music.load("abc.mp3")
    print("Merry Christmas!")
else:
    pygame.mixer.music.load("abc.mp3")
print("Loading Music...")
pygame.mixer.music.play(-1, 0.0)
print("Playing Background Music...")
while True:
	filename = "clock.png"
	img = pygame.image.load(filename)
	screen.blit(img,(100,60))
	pygame.display.flip()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()