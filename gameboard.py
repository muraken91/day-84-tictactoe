import random

class GameBoard:
	def __init__(self):
		self.board = ["-", "-", "-",
					  "-", "-", "-",
			          "-", "-", "-"]
		self.p_icon = ""
		self.c_icon = ""

	def print_board(self):
		board = self.board
		print("\n")
		print(board[0] + " | " + board[1] + " | " + board[2])
		print("__________")
		print(board[3] + " | " + board[4] + " | " + board[5])
		print("__________")
		print(board[6] + " | " + board[7] + " | " + board[8])
		print("\n")

	def player_input(self):
		choose = True
		while choose:
			tile_choice = int(input("Pick an empty tile between 1-9: ")) - 1
			if 0 <= tile_choice < 9:
				if self.board[tile_choice] == "X" or self.board[tile_choice] == "O":
					print("Invalid Tile, Please pick an empty tile")
				else:
					self.board[tile_choice] = self.p_icon
					choose = False
			else:
				print("Invalid Tile, Please pick an empty tile")

	def player_icon(self):
		choose = True
		while choose:
			icon_choice = input("Pick your icon (X/O): ").upper()
			if icon_choice == "X" or "O":
				if icon_choice == "X":
					self.c_icon = "O"
				else:
					self.c_icon = "X"
				self.p_icon = icon_choice
				choose = False
			else:
				print("Invalid input, please pick between X/O.")

	def cpu_input(self):
		choose = True
		while choose:
			tile_choice = random.randint(0, 8)
			if self.board[tile_choice] == "-":
				print(f"CPU chooses tile: {tile_choice}")
				self.board[tile_choice] = self.c_icon
				choose = False
