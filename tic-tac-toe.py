from random import randint as rd

BOARD = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
TEAMS = ["X", "O"]

def show_board():
    print(f"  {BOARD[0][0]}  | {BOARD[0][1]}  | {BOARD[0][2]}")
    print("______________")
    print(f"  {BOARD[1][0]}  | {BOARD[1][1]}  | {BOARD[1][2]}")
    print("______________")
    print(f"  {BOARD[2][0]}  | {BOARD[2][1]}  | {BOARD[2][2]}")


def greet_user():
	print("Welcome!")
	response = input("Would you like to play tic-tac-toe?(Y/N): ").strip().lower()
	if response == 'y':
		usr_name = input("What is your name good sir: ").strip()
		main_loop(usr_name)
	elif response == 'n':
		print('BYE, see you soon!')
	else:
		print('sorry!')


def main_loop(user_name):
	usr_team = input("On which team would you like to be?(X/O): ").strip()

	if usr_team.lower() == 'x':
		usr_team = TEAMS[0]
		bot_team = TEAMS[1]
	elif usr_team.lower() == 'o':
		usr_team = TEAMS[1]
		bot_team = TEAMS[0]
	draw_check = 0
	while True:
		place = input(f"Place the {usr_team}'s value: ").strip().lower()
		if place == 'a':
			if BOARD[0][0] != bot_team:
				if BOARD[0][0] != usr_team:
					BOARD[0][0] = usr_team
					bot_response(usr_team, bot_team)
				else:
					print("You've already filled it!")
			else:
				print('Already occupied by bot!')

		elif place == 'b':
			if BOARD[0][1] != bot_team:
				if BOARD[0][1] != usr_team:
					BOARD[0][1] = usr_team
					bot_response(usr_team, bot_team)

				else:
					print("You've already filled it!")
			else:
				print('Already occupied by bot!')

		elif place == 'c':
			if BOARD[0][2] != bot_team:
				if BOARD[0][2] != usr_team:
					BOARD[0][2] = usr_team
					bot_response(usr_team, bot_team)

				else:
					print("You've already filled it!")
			else:
				print('Already occupied by bot!')

		elif place == 'd':
			if BOARD[1][0] != bot_team:
				if BOARD[1][0] != usr_team:
					BOARD[1][0] = usr_team
					bot_response(usr_team, bot_team)
				else:
					print("You've already filled it!")
			else:
				print('Already occupied by bot!')

		elif place == 'e':
			if BOARD[1][1] != bot_team:
				if BOARD[1][1] != usr_team:
					BOARD[1][1] = usr_team
					bot_response(usr_team, bot_team)
				else:
					print("You've already filled it!")
			else:
				print('Already occupied by bot!')

		elif place == 'f':
			if BOARD[1][2] != bot_team:
				if BOARD[1][2] != usr_team:
					BOARD[1][2] = usr_team
					bot_response(usr_team, bot_team)
				else:
					print("You've already filled it!")
			else:
				print('Already occupied by bot!')

		elif place == 'g':
			if BOARD[2][0] != bot_team:
				if BOARD[2][0] != usr_team:
					BOARD[2][0] = usr_team
					bot_response(usr_team, bot_team)
				else:
					print("You've already filled it!")
			else:
				print('Already occupied by bot!')

		elif place == 'h':
			if BOARD[2][1] != bot_team:
				if BOARD[2][1] != usr_team:
					BOARD[2][1] = usr_team
					bot_response(usr_team, bot_team)
				else:
					print("You've already filled it!")
			else:
				print('Already occupied by bot!')

		elif place == 'i':
			if BOARD[2][2] != bot_team:
				if BOARD[2][2] != usr_team:
					BOARD[2][2] = usr_team
				else:
					print("You've already filled it!")
			else:
				print('Already occupied by bot!')


		else:
			print("Place between 'a-i' only!")

		draw_check += 1
		show_board()
		if decide_result(usr_team, bot_team, draw_check):
			print(decide_result(usr_team, bot_team, draw_check))
			break

def bot_response(usr_team, bot_team):
	while True:
		x,y = rd(0,2), rd(0,2)
		if BOARD[x][y] != usr_team:
			if BOARD[x][y] != bot_team:
				BOARD[x][y] = bot_team
				break


def decide_result(usr_team, bot_team, draw_check):
	if usr_team == BOARD[0][0] and usr_team == BOARD[1][0] and usr_team == BOARD[2][0]:
		return (f'{usr_team} won the game!')

	elif usr_team == BOARD[0][0] and usr_team == BOARD[0][1] and usr_team == BOARD[0][2]:
		return (f'{usr_team} won the game!')

	elif usr_team == BOARD[1][0] and usr_team == BOARD[1][1] and usr_team == BOARD[1][2]:
		return (f'{usr_team} won the game!')

	elif usr_team == BOARD[2][0] and usr_team == BOARD[2][1] and usr_team == BOARD[2][2]:
		return (f'{usr_team} won the game!')

	elif usr_team == BOARD[0][2] and usr_team == BOARD[1][2] and usr_team == BOARD[2][2]:
		return (f'{usr_team} won the game!')

	elif usr_team == BOARD[0][1] and usr_team == BOARD[1][1] and usr_team == BOARD[2][1]:
		return (f'{usr_team} won the game!')

	# bot

	if bot_team == BOARD[0][0] and bot_team == BOARD[1][0] and bot_team == BOARD[2][0]:
		return (f'{bot_team} won the game!')

	elif bot_team == BOARD[0][0] and bot_team == BOARD[0][1] and bot_team == BOARD[0][2]:
		return (f'{bot_team} won the game!')

	elif bot_team == BOARD[1][0] and bot_team == BOARD[1][1] and bot_team == BOARD[1][2]:
		return (f'{bot_team} won the game!')

	elif bot_team == BOARD[2][0] and bot_team == BOARD[2][1] and bot_team == BOARD[2][2]:
		return (f'{bot_team} won the game!')

	elif bot_team == BOARD[0][2] and bot_team == BOARD[1][2] and bot_team == BOARD[2][2]:
		return (f'{bot_team} won the game!')

	elif usr_team == BOARD[0][1] and bot_team == BOARD[1][1] and bot_team == BOARD[2][1]:
		return (f'{bot_team} won the game!')

	# Draw
	if draw_check > 3:
		if usr_team != BOARD[0][0] and usr_team != BOARD[0][1] and usr_team != BOARD[0][2]:
			return 'The game is drawn!'
		if usr_team != BOARD[1][0] and usr_team != BOARD[1][1] and usr_team != BOARD[1][2]:
			return 'The game is drawn!'
		if usr_team != BOARD[2][0] and usr_team != BOARD[2][1] and usr_team != BOARD[2][2]:
			return 'The game is drawn!'
		if usr_team != BOARD[0][0] and usr_team != BOARD[1][0] and usr_team != BOARD[2][0]:
			return 'The game is drawn!'
		if usr_team != BOARD[0][1] and usr_team != BOARD[1][1] and usr_team != BOARD[2][1]:
			return 'The game is drawn!'
		if usr_team != BOARD[0][2] and usr_team != BOARD[1][2] and usr_team != BOARD[2][2]:
			return 'The game is drawn!'

		if bot_team != BOARD[0][0] and bot_team != BOARD[0][1] and bot_team != BOARD[0][2]:
			return 'The game is drawn!'
		if bot_team != BOARD[1][0] and bot_team != BOARD[1][1] and bot_team != BOARD[1][2]:
			return 'The game is drawn!'
		if usr_team != BOARD[2][0] and usr_team != BOARD[2][1] and bot_team != BOARD[2][2]:
			return 'The game is drawn!'
		if bot_team != BOARD[0][0] and bot_team != BOARD[1][0] and bot_team != BOARD[2][0]:
			return 'The game is drawn!'
		if bot_team != BOARD[0][1] and bot_team != BOARD[1][1] and bot_team != BOARD[2][1]:
			return 'The game is drawn!'
		if bot_team != BOARD[0][2] and bot_team != BOARD[1][2] and bot_team != BOARD[2][2]:
			return 'The game is drawn!'


greet_user()
