from tkinter import Tk, StringVar, filedialog as fd
from pickle import load, dump

frames = []
buttons = []
board = []
slugs = {
	"Classic" : "classic",
	"King's move" : "classic+king",
	"Knight's move" : "classic+knight",
	"Adjacent cell consecutive" : "classic+adjacent",
	"Knight and King's move" : "classic+king+knight",
	"Knight and Adjacent" : "classic+knight+adjacent",
	"King and Adjacent" : "classic+king+adjacent",
	"All" : "classic+king+knight+adjacent"
}

reverse_slugs = {
	"classic" : "Classic",
	"king" : "King's move",
	"knight" : "Knight's move",
	"adjacent" : "Adjacent square"
}

screen = Tk()
screen.geometry(f"400x525+{int(screen.winfo_screenwidth()/2-200)}+{int(screen.winfo_screenheight()/2-400)}")
screen.resizable(width=False, height=False)

message = StringVar()
rule = StringVar()

def knight_check(x, y, value:str):
	knight = []
	positions = [(-1, -2), (-2, -1), (-2, 1), (-1, 2),
				(1, -2), (2, -1), (2, 1), (1, 2)]
	check = lambda x, y: knight.append(buttons[x][y]['text'])

	for i in positions:
		try:
			if(x+i[0] >= 0 and y+i[1] >= 0):
				check(x+i[0], y+i[1])
		except:
			...

	return value in knight

def king_check(x, y, value:str):
	king = []
	positions = [(-1, -1), (-1, 0), (-1, 1),
				(0, -1), (0, 1),
				(1, -1), (1, 0), (1, 1)]

	check = lambda x, y: king.append(buttons[x][y]['text'])

	for i in positions:
		try:
			check(x+i[0], y+i[1])
		except:
			...

	return value in king

def adjacent_check(x, y, value:str):
	adjacent = []
	positions = [(-1, 0), (0, 1), (0, -1), (1, 0)]

	check = lambda x, y:adjacent.append(buttons[x][y]['text'])

	for i in positions:
		try:
			check(x+i[0], y+i[1])
		except:
			...

	return (str(int(value) + 1) in adjacent) or (str(int(value)-1) in adjacent)

def classic_check(x, y, value:str):
	numbersx, numbersy, box = [], [], []

	for j in range(9):
		numbersx.append(buttons[x][j]['text'])

	for i in range(9):
		numbersy.append(buttons[i][y]['text'])

	for i in frames[x//3][y//3].winfo_children():
		box.append(i['text'])

	return (value in numbersx) or (value in numbersy) or (value in box)

def board_clear(event=None):
	for i in buttons:
		for j in i:
			j.value.set("")
	
	message.set("Board has been cleared!\nRules have been updated!")

def open_puzzle(event=None):
	global board

	board_clear()

	types=(
		('Sudoku puzzle', '*.sdk'),
		('Other', '*.*')
	)

	puzzle_file = fd.askopenfilename(filetypes=types)

	try:
		with open(puzzle_file, 'rb') as f:
			data = load(f)
		board = data['board']
		rule.set(data['rule'])

		for i in buttons:
			for j in i:
				j.value.set(board[buttons.index(i)][i.index(j)])
		
		message.set("Puzzle loaded")
	except:
		# message.set(e)
		...

def save_puzzle(event=None):
	global board

	board = []

	types=(
		('Sudoku puzzle', '*.sdk'),
		('Other', '*.*')
	)

	for i in buttons:
		line = []
		for j in i:
			line.append(j.value.get())
		board.append(line)

	data = {}
	data['board'] = board
	data['rule'] = rule.get()

	puzzle_file = fd.asksaveasfilename(filetypes = types)

	try:
		with open(puzzle_file, 'wb') as f:
			dump(data, f)
		message.set(f"Puzzle saved successfully to {puzzle_file.split('/')[-1]}")
	except:
		# message.set(e)
		...