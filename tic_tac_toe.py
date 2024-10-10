import random

def initialization():
	print("--- Welcome to Tic-Tac-Toe ---")
	grid_size = eval(input("Enter Grid Size between 3 - 6 : "))
	game_state = initialize_game_state(grid_size)
	plr1_name = input("Enter player-1 name : ")
	plr2_name = input("Enter player-2 name : ")
	ply_info = {1: {'name' : plr1_name, 'sign' : 'X'}, 2 : {'name' : plr2_name, 'sign' : 'O'}}
	display(game_state)
	for i in range(1, len(ply_info)+1):
		print(f"{ply_info[i]['name'].title()} your sign will : {ply_info[i]['sign']}") 
	return game_state, ply_info

def initialize_game_state(size):
	game_state = {row : {col : ' ' for col in range(1, size+1)} for row in range(1, size+1)}
	return game_state
 	
def display(game_state):
	size = len(game_state)
	for row in range(size):
		print(' ---'*size)
		print('|',end='')
		for col in range(size):
			print(f' {game_state[row+1][col+1]} |',end='')
		print()
	print(' ---'*size)

def check_winner(game_state):
    size = len(game_state)

    for row in range(1, size+1):
        if game_state[row][1] == game_state[row][2] == game_state[row][3] != ' ':
            return game_state[row][1]

    for col in range(1, size+1):
        if game_state[1][col] == game_state[2][col] == game_state[3][col] != ' ':
            return game_state[1][col] 
		
    if game_state[1][1] == game_state[2][2] == game_state[3][3] != ' ':
        return game_state[1][1]
    
    if game_state[1][3] == game_state[2][2] == game_state[3][1] != ' ':
        return game_state[1][3]
    
    return None

def start_game(game_state, plyr_info): 
	chance = random.randint(1,2)
	print(f"{plyr_info[chance]['name']} you win toss...")
	for i in range(len(game_state)**2):
		while True:
			row, col = eval(input(f"{plyr_info[chance]['name']} - Enter Location (Format : x,y): "))
			if all(x in range(1,len(game_state)+1) for x in [row, col]):
			# if row in len(game_state) and col < len(game_state):
				if game_state[row][col] in ' ':
					game_state[row][col] = plyr_info[chance]['sign']
					break
				else:
					print("Try another location...")
			else:
				print("Enter location within range 1 -",len(game_state))
		display(game_state)
		if x:=check_winner(game_state):
			for info in plyr_info.values():
				if info['sign'] == x:
					return info['name']

		chance = 3-chance

def stop_game(winner):
	if winner:
		print(f"Congrats {winner}..! you wins the game")
	else:
		print("Game Over")

def ttt():
	game_state, plyr_info = initialization()
	winner = start_game(game_state, plyr_info)
	stop_game(winner)
	
ttt()
