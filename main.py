from cercle import *
import sys
from threading import Thread

GREEN = (0, 255, 0)
RED = (255 ,0 , 0)
COLOR = [RED, GREEN]
fini = False
temps = pygame.time.Clock()

window = Window(wwidth=1400, wheight=800, wtitle="cercle de multiplication")
modulo_n = 10
table_factor = 2
radius = 375
circle = Circle(window=window, radius=radius, modulo_n=modulo_n, table_factor=table_factor)
circle.update_circle()
thread = Thread(target=lambda:command_line_set_circle_parameters(circle))
thread.start()
number_vision = True
increase_modulo_n = False
increase_mul = False
info_mod_command1 = Printstring(x=30, y=50,main_font=circle.font, string="UP/DOWN : modulo+/-1", color=(0, 0, 0))
info_mod_command2 = Printstring(x=30, y=80,main_font=circle.font, string="SPACE : modulo+inf", color=RED)
info_mul_command1 = Printstring(x=30, y=120,main_font=circle.font, string="RIGHT/LEFT : mul+/-1", color=(0, 0, 0))
info_mul_command2 = Printstring(x=30, y=150,main_font=circle.font, string="RETURN : mul+inf", color=RED)
info_v_command = Printstring(x=30, y=190,main_font=circle.font, string="H : hide numbers", color=(0, 0, 0))
while not fini:
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			fini = True
		if event.type == KEYUP:
			if event.key == K_q:
				fini = True
			elif event.key == K_UP:
				circle.set_modulo_n(circle.modulo_n+1)
			elif event.key == K_DOWN:
				circle.set_modulo_n(circle.modulo_n-1)
			elif event.key == K_RIGHT:
				circle.set_table_factor(circle.table_factor+1)
			elif event.key == K_LEFT:
				circle.set_table_factor(circle.table_factor-1)
			elif event.key == K_h:
				number_vision = not number_vision
			elif event.key == K_SPACE:
				increase_modulo_n = not increase_modulo_n
				info_mod_command2.color = COLOR[increase_modulo_n]
				info_mod_command2.refresh()
			elif event.key == K_RETURN:
				increase_mul = not increase_mul
				info_mul_command2.color = COLOR[increase_mul]
				info_mul_command2.refresh()
	if increase_modulo_n:
		circle.set_modulo_n(circle.modulo_n+1)
	if increase_mul:
		circle.set_table_factor(circle.table_factor+1)


	

	temps.tick(60)

	window.fill((255,255,255))	
	circle.print(number_vision=number_vision)
	info_mod_command1.write()
	info_mod_command2.write()
	info_mul_command1.write()
	info_mul_command2.write()
	info_v_command.write()
	pygame.display.flip()

print("\nwait for stop the simulation...")
thread.join()

print("exit success")

