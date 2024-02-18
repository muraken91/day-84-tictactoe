from gameboard import GameBoard
from gamelogic import GameLogic
from time import sleep


game_board = GameBoard()
game_board.player_icon()
game_logic = GameLogic(game_board.p_icon, game_board.c_icon)

game = True

while game:
	game_board.print_board()
	game_logic.check_winner(game_board.board)
	if game_logic.winner:
		game = False
	else:
		if "-" not in game_board.board:
			game = False
			print("It's a draw!")
		else:
			game_board.player_input()
			game_board.print_board()
			game_logic.check_winner(game_board.board)
			if game_logic.winner:
				game = False
			else:
				sleep(1)
				game_board.cpu_input()
