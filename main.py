#! /usr/bin/python

from tkinter import Frame, Button, Entry, OptionMenu, StringVar, Label
from utils import frames, buttons, slugs, screen, message, rule, board_clear, open_puzzle, save_puzzle
from butt import Butt, Number, curr_B

def mark(event):
	if event.char in "123456789":
		Number.set_value(Number(frame_numbers, value=int(event.char)))

master_frame = Frame(screen)


#*	Frame generation for Sudoku box


for i in range(3):
	box = []
	for j in range(3):
		frame = Frame(master_frame)
		if (i%2 or j%2) and i%2!=j%2:
			frame.config(bg="lightgrey")
		else:
			frame.config(bg="grey")
		frame.grid(row=i, column=j)
		screen.update()
		box.append(frame)
	frames.append(box)


#*	Button generation for Sudoku box


for i in range(9):
	line = []
	for j in range(9):
		line.append(Butt(frames[i//3][j//3], position=(i, j),  height=1, width=1))
		line[j].grid(row=i, column=j, ipadx=1, ipady=1, padx=1, pady=1)
	buttons.append(line)


#*	Debug button


# button1 = Button(master_frame)
# button1.grid(row=3, columnspan=3)
# button1['text'] = "hello"
# button1['command'] = test


#*	Controls frame


controls = Frame(master_frame)
controls.grid(rowspan=4, columnspan=3)


#*	Message frame and widget


frame_message = Frame(controls)
frame_message.grid(row=0, columnspan=2)

message_label = Label(frame_message, textvariable=message)
message_label.grid()


#*	Dropdown frame and widgets


frame_dropdowns = Frame(controls)
frame_dropdowns.grid(row=1, column=0)

#	Rule dropdown

rule.set("Classic")
rules = [rule for rule in slugs.keys()]
dropdown_rule = OptionMenu(frame_dropdowns, rule, *rules, command=board_clear)
dropdown_rule.grid(row=0)

#	Puzzle select

selector = Button(frame_dropdowns, command=open_puzzle)
selector['text'] = "Open puzzle"
selector.grid(row=1)

#	Puzzle save

saver = Button(frame_dropdowns, command=save_puzzle)
saver['text'] = "Save puzzle"
saver.grid(row=2)


#*	Virtual keypad frame and widgets


frame_numbers = Frame(controls, bg="white")
frame_numbers.grid(row=1, column=1)

for i in range(3):
	for j in range(3):
		x = Number(frame_numbers, value = i*3+(j+1))
		x.grid(row=i, column=j)


#*	Keyboard binds


screen.bind("<Key>", mark)


#*	Final packing


if __name__=="__main__":

	master_frame.pack(expand=True)
	screen.mainloop()
