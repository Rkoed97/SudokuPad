from tkinter import Button, StringVar, font
from utils import frames, buttons, slugs, reverse_slugs, message, rule, knight_check, king_check, classic_check, adjacent_check

curr_B = None

class Butt(Button):

	def __init__(self, *args, position:tuple,  **kwargs):
		self.value = StringVar()
		self.value.set("")
		my_font = font.Font(size=15)
		Button.__init__(self, *args, command=self.set_current, textvariable=self.value, bg='lightgrey', fg='black', border = 0, **kwargs)
		self.position = position
		self['font'] = my_font

	def set_current(self):

		x = check(self.position[0], self.position[1], 1)

		for i in buttons:
			for j in i:
				j.config(bg="lightgrey")

		for i in x[1]:
			i.config(bg="#b7a4d2")

		self.config(bg='grey')
		global curr_B
		curr_B = self

class Number(Button):

	def __init__(self, *args, value:int, **kwargs):
		my_font = font.Font(size=15)
		Button.__init__(self, *args, command=self.set_value, **kwargs)
		self.value = str(value)
		self['text'] = value
		self['font'] = my_font

	def set_value(self):
		x, y = curr_B.position

		validity = check(x, y, self.value)[0]

		for r, v in validity.items():
			if(v):
				message.set(f"{self.value} here violates {reverse_slugs[r]} Sudoku rule")

		if not any([v for v in validity.values()]):
			curr_B.value.set(self.value)
			message.set("")

def check(*args):

	rules = slugs[rule.get()].split('+')
	active_buttons = []
	validity = {}

	for i in rules:
		if i == "classic":
			classic = classic_check(*args)
			validity['classic'] = classic[0]
			active_buttons = active_buttons+classic[1]
		elif i == "king":
			king = king_check(*args)
			validity['king'] = king[0]
			active_buttons = active_buttons+king[1]
		elif i == "knight":
			knight = knight_check(*args)
			validity['knight'] = knight[0]
			active_buttons = active_buttons+knight[1]
		elif i == "adjacent":
			adjacent = adjacent_check(*args)
			validity['adjacent'] = adjacent[0]
			active_buttons = active_buttons+adjacent[1]

	return (validity, list(set(active_buttons)))