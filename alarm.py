import Tkinter;
import sys;
import time;
import datetime;
import playsound;
import mp3play;
import threading;
import os
import pygame, sys
from pygame.locals import *


pygame.init()
screen = pygame.display.set_mode((500, 400))
screen.fill((49, 26, 65))
pygame.display.set_caption("TESTIFICATE")

print("Press \n 1. Basic Alarm Tone\n 2. Nature's Alarm Tone");
choice = raw_input();
path = '';
if(choice == '1'):
	path = r'alarms\Alarm-Clock Sound!!!.mp3';
if(choice == '2'):
	path = r'alarms\Best Natural Ringtone alarm tone.mp3';
# clip = mp3play.load(path);


pygame.mixer.music.load(path)


class Alarm(threading.Thread):
	def __init__(self, hours, minutes, seconds):
		super(Alarm, self).__init__()
		self.hours = hours
		self.minutes = minutes
		self.seconds = seconds
		# self.clip = mp3play.load(path);
		self.keep_running = True;

	def run(self):
		try:
			while self.keep_running:
				now = time.localtime()
				if (now.tm_hour == self.hours and now.tm_min == self.minutes):
					print("ALARM NOW!")
					# os.popen("abc.mp3")
					#self.clip.play();
					print("Loading Music...")
					pygame.mixer.music.play(-1, 0.0)
					print("Playing Background Music...")
					return
				time.sleep(20);
		except:
			return
	def just_die(self):
		self.keep_running = False;


print("Alarm\n");
print("Enter start time : HH:MM:SS");

time1 = raw_input();
time_arr = time1.split(':')
hh = int(time_arr[0]);
min = int(time_arr[1]);
sec = int(time_arr[2]);

# print("Press \n 1. Basic Alarm Tone\n 2. Nature's Alarm Tone");
# choice = raw_input();
# path = '';
# if(choice == '1'):
# 	path = r'alarms\Alarm-Clock Sound!!!.mp3';
# if(choice == '2'):
# 	path = r'alarms\Best Natural Ringtone alarm tone.mp3';
# clip = mp3play.load(path);


alarm = Alarm(hh, min,sec)
alarm.start()

while True:
	filename = "clock.png"
	img = pygame.image.load(filename)
	screen.blit(img,(100,60))
	pygame.display.flip()
	text = str(raw_input())

	if text == "stop":
		alarm.just_die()
		break


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()
# try:
#     while True:
#          text = str(raw_input())
         
#          if text == "stop":
#             alarm.just_die()
#             break
# except:
#     print("Yikes lets get out of here")
#     alarm.just_die()