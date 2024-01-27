from pynput.mouse import Button, Controller
from pynput import keyboard
from time import sleep

width = 1920
height = 1080
duration = 0.001

mouse = Controller()

class StopException(Exception):
	pass

def terminate():
	raise StopException

def horizontal_line():
	mouse.position = (600, 350)
	mouse.press(Button.left)

	x_pos = 600
	for i in range(4):
		mouse.position = (x_pos := x_pos + 25, 350)
		sleep(duration)

	mouse.release(Button.left)

def vertical_line():
	mouse.position = (600, 350)
	mouse.press(Button.left)

	y_pos = 350
	for i in range(4):
		mouse.position = (600, y_pos := y_pos + 25)
		sleep(duration)

	mouse.release(Button.left)

def peak_line():
	mouse.position = (600, 350)
	mouse.press(Button.left)

	x_pos = 600
	y_pos = 350
	for i in range(4):
		mouse.position = (x_pos := x_pos + 25, y_pos := y_pos - 25)
		sleep(duration)

	for i in range(4):
		mouse.position = (x_pos := x_pos + 25, y_pos := y_pos + 25)
		sleep(duration)

	mouse.release(Button.left)

def valley_line():
	mouse.position = (600, 350)
	mouse.press(Button.left)

	x_pos = 600
	y_pos = 350
	for i in range(4):
		mouse.position = (x_pos := x_pos + 25, y_pos := y_pos + 25)
		sleep(duration)

	for i in range(4):
		mouse.position = (x_pos := x_pos + 25, y_pos := y_pos - 25)
		sleep(duration)

	mouse.release(Button.left)

def spiral_line():
	mouse.position = (600, 350)
	mouse.press(Button.left)

	x_pos = 600
	y_pos = 350

	positions = (
				(580, 340),
				(565, 330),
				(560, 310),
				(575, 295),
				(595, 300),
				(600, 315),
				(593, 325),
				(580, 320),
				(577, 309),
			 )

	for pos_tuple in positions:
		mouse.position = pos_tuple
		sleep(duration)

	mouse.release(Button.left)

def circle_line():
	mouse.position = (612.5, 398)
	mouse.press(Button.left)

	positions = (
		(625, 393),
		(637.5, 383),
		(650, 350),
		(637.5, 317),
		(625, 307),
		(612.5, 302),
		(600, 300),
		(587.5, 302),
		(575, 307),
		(562.5, 317),
		(550, 350),
		(562.5, 383),
		(575, 393),
		(587.5, 398),
		(600, 400),
	)

	for pos_tuple in positions:
		mouse.position = pos_tuple
		sleep(duration)

	mouse.release(Button.left)

def heart_line():
	mouse.position = (600, 350)
	mouse.press(Button.left)

	positions = ( 
		(600, 350), 
		(615, 340), 
		(645, 357), 
		(629, 388), 
		(600, 409), 
		(571, 388), 
		(555, 357), 
		(585, 340), 
		(600, 350), 
	)

	for pos_tuple in positions:
		mouse.position = pos_tuple
		sleep(duration)

	mouse.release(Button.left)

def lightning_line():
	mouse.position = (600, 350)
	mouse.press(Button.left)

	positions = (
		(600, 350),
		#(580, 370),
		#(560, 390),
		#(540, 410),
		(520, 430),
		(500, 450),
		(533, 450),
		(566, 450),
		(600, 450),
		(580, 470),
		#(560, 490),
		#(540, 510),
		#(520, 530),
		(500, 550)
	)

	for pos_tuple in positions:
		mouse.position = pos_tuple
		sleep(duration)

	mouse.release(Button.left)


# def on_press(key):
# 	if key == keyboard.Key.esc:
# 		return False
# 	if key == keyboard.KeyCode(char="a"):
# 		horizontal_line()
# 	if key == keyboard.KeyCode(char="s"):
# 		vertical_line()
# 	if key == keyboard.KeyCode(char="d"):
# 		peak_line()
# 	if key == keyboard.KeyCode(char="f"):
# 		valley_line()
# 	if key == keyboard.KeyCode(char="j"):
# 		spiral_line()
# 	if key == keyboard.KeyCode(char="k"):
# 		circle_line()
# 	if key == keyboard.KeyCode(char="q"):
# 		heart_line()

instructions = {
	keyboard.Key.esc: terminate,
	keyboard.KeyCode(char="q"): heart_line,
	keyboard.KeyCode(char="a"): horizontal_line,
	keyboard.KeyCode(char="s"): vertical_line,
	keyboard.KeyCode(char="d"): peak_line,
	keyboard.KeyCode(char="f"): valley_line,
	keyboard.KeyCode(char="j"): spiral_line,
	keyboard.KeyCode(char="k"): circle_line,
	keyboard.KeyCode(char="l"): lightning_line,
	}

def on_press(key):
	try:
		instructions[key]()
	except StopException:
		return False
	except KeyError:
		pass

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()