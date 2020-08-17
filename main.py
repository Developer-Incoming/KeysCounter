import keyboard

event_counter = []


def on_press(event):
	event_counter.append(event)
	with open('input_counter.txt', 'w') as file:
		file.write('{} \n'.format(int(len(event_counter)/2)))


keyboard.hook(on_press)
keyboard.wait()


