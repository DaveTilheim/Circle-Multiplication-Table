from izi_pygame import *
from math import *
import os
from random import randint
from time import sleep

SHIFTUP = 4.5
RED = (200, 0, 0)
BLACK = (0, 0, 0)
POINT_SIZE = 3
LIAISON_SIZE = 1
CIRCLE_REVOLUTION = 360

class Point:

	def __init__(self, x, y, value):
		self.x = x
		self.y = y
		self.value = value

class Circle:

	def __init__(self, window, radius, modulo_n, table_factor):
		self.win = window
		self.radius = radius
		self.x = window.wwidth//2
		self.y = window.wheight//2
		self.font = Fontstring(window=window.get_canva(), size=30)
		self.pr = Printstring(main_font=self.font, string="", color=(0, 0, 0))
		self.list_point = list()
		self.modulo_n = modulo_n
		self.table_factor = table_factor
		self.font_info = Fontstring(window=window.get_canva(), size=35)
		self.info_mul_mod = Printstring(x=30, y=15,main_font=self.font_info, string="", color=(0, 0, 180))
		self.info_mul_mod << f"{self.table_factor} modulo {self.modulo_n}"

	def update_circle(self):
		i = 0
		j = 0
		self.list_point = []
		while i < CIRCLE_REVOLUTION and j < self.modulo_n:
			x = self.x+self.radius*sin(radians(i))
			y = self.y-self.radius*cos(radians(i))
			self.list_point.append(Point(x, y, j))
			i += CIRCLE_REVOLUTION/self.modulo_n
			j += 1

	def print_liaison(self):
		for i in range(1, len(self.list_point), 1):
			p1 = self.list_point[i]
			p2 = self.list_point[i*self.table_factor%self.modulo_n]
			pygame.draw.line(self.win.get_canva(), (100, 0, 100), (p1.x, p1.y), (p2.x, p2.y), LIAISON_SIZE)

	def print_info(self):
		self.info_mul_mod.write()

	def print(self, number_vision=True):
		pygame.draw.circle(self.win.get_canva(), RED, (self.x, self.y), self.radius, 5)
		if number_vision:
			for p in self.list_point:
				pygame.draw.circle(self.win.get_canva(), (0, 0, 200), (int(p.x), int(p.y)), POINT_SIZE, 0)
				self.pr << str(int(p.value))
				if p.x < self.win.wwidth//2:
					self.pr.x = p.x-SHIFTUP*5
				elif p.x > self.win.wwidth//2:
					self.pr.x = p.x+SHIFTUP*2
				else:
					self.pr.x = p.x-SHIFTUP
				if p.y > self.win.wheight//2:
					self.pr.y = p.y+SHIFTUP
				elif p.y < self.win.wheight//2:
					self.pr.y = p.y-SHIFTUP*5
				else:
					self.pr.y = p.y+SHIFTUP
				self.pr.write()
		self.print_liaison()
		self.print_info()

	def set_modulo_n(self, value):
		self.modulo_n = value
		self.update_circle()
		self.info_mul_mod << f"{self.table_factor} modulo {self.modulo_n}"

	def set_table_factor(self, value):
		self.table_factor = value
		self.info_mul_mod << f"{self.table_factor} modulo {self.modulo_n}"



def command_line_set_circle_parameters(circle):
	os.system("clear")
	cmd = str("")
	while cmd != "end":
		print("\n[command] \nmod: change the modulo\nmul: change the mul table\nend: stop the programm\n")
		cmd = input("> ")
		if cmd == "end":continue
		cmd = cmd.split(" ")
		os.system("clear")
		if len(cmd) != 2:
			print("command must have 2 parameters (mod or mul)")
			continue
		if cmd[0] in ["mod", "mul"]:
			value = int()
			try:
				value = int(cmd[1])
			except:
				print("the second arg must be an integer")
				continue
				
			if cmd[0] == "mod":
				circle.set_modulo_n(value)
			else:
				circle.set_table_factor(value)
		else:
			print("the first arg must be \"mod\" or \"mul\"")
			continue
	print("wait for stop the thread...")



