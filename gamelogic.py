class GameLogic:
	def __init__(self, p_icon, c_icon):
		self.winner = False
		self.player = p_icon
		self.cpu = c_icon

	def check_winner(self, board):
		self.check_row(board)
		self.check_column(board)
		self.check_cross(board)

	def check_row(self, board):
		if board[0] == board[1] == board[2] and board[0] != "-":
			if board[0] == self.player:
				print(f"You won!")
				self.winner = True
			elif board[0] == self.cpu:
				print(f"CPU won, You lost.")
				self.winner = True
		elif board[3] == board[4] == board[5] and board[3] != "-":
			if board[3] == self.player:
				print(f"You won!")
				self.winner = True
			elif board[3] == self.cpu:
				print(f"CPU won, You lost.")
				self.winner = True
		elif board[6] == board[7] == board[8] and board[6] != "-":
			if board[6] == self.player:
				print(f"You won!")
				self.winner = True
			elif board[6] == self.cpu:
				print(f"CPU won, You lost.")
				self.winner = True

	def check_column(self, board):
		if board[0] == board[3] == board[6] and board[0] != "-":
			if board[0] == self.player:
				print(f"You won!")
				self.winner = True
			elif board[0] == self.cpu:
				print(f"CPU won, You lost.")
				self.winner = True
		elif board[1] == board[4] == board[7] and board[1] != "-":
			if board[1] == self.player:
				print(f"You won!")
				self.winner = True
			elif board[1] == self.cpu:
				print(f"CPU won, You lost.")
				self.winner = True
		elif board[2] == board[5] == board[8] and board[2] != "-":
			if board[2] == self.player:
				print(f"You won!")
				self.winner = True
			elif board[2] == self.cpu:
				print(f"CPU won, You lost.")
				self.winner = True

	def check_cross(self, board):
		if board[0] == board[4] == board[8] and board[0] != "-":
			if board[0] == self.player:
				print(f"You won!")
				self.winner = True
			elif board[0] == self.cpu:
				print(f"CPU won, You lost.")
				self.winner = True
		elif board[2] == board[4] == board[6] and board[2] != "-":
			if board[2] == self.player:
				print(f"You won!")
				self.winner = True
			elif board[2] == self.cpu:
				print(f"CPU won, You lost.")
				self.winner = True
