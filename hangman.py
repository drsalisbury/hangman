import random
from operator import itemgetter
import time
import os

def get_players():
	players = list()
	num_players = int(input("How many players? "))
	print(f"Players: {num_players}")
	for index in range(num_players):
		player_name = input(f"Name of player #{index + 1}: ")
		player = {
			"name": player_name,
			"score": 0
		}
		players.append(player)
	return players

def get_num_rounds():
	num_rounds = int(input("How many rounds? "))
	print(f"Rounds: {num_rounds}")
	return num_rounds

def get_difficulty():
	difficulty = int(input("What difficulty? (1=easy, 2=intermediate, 3=hard) "))
	print(f"Difficulty: {difficulty}")
	return difficulty

def load_words():
	with open("words.txt") as words_file:
		words = words_file.readlines()
	stripped_words = list()
	for word in words:
		stripped_word = word.rstrip().upper()
		stripped_words.append(stripped_word)
	return stripped_words

def get_word(words, difficulty):
	while True:
		word = random.choice(words)
		length = len(word)
		if length > 3 and length < 6 and difficulty == 1:
	 		return word
		if length > 5 and length < 8 and difficulty == 2:
			return word
		if length > 7 and difficulty == 3:
			return word
		
def print_hangman(stage):
	print("______________")
	print("| |         ][")
	print("| |         ][")

	if stage > 0:
		print("| |        /..\\")
		print("| |        \\__/")
	else:
		print("| |")
		print("| |")
	
	if stage == 0 or stage == 1:
		print("| |")
		print("| |")
		print("| |")
		print("| |")
	elif stage == 2:
		print("| |         ||")
		print("| |         ||")
		print("| |         ||")
		print("| |")
	elif stage == 3:
		print("| |       \\_||")
		print("| |         ||")
		print("| |         ||")
		print("| |")
	elif stage == 4:
		print("| |       \\_||_/")
		print("| |         ||")
		print("| |         ||")
		print("| |")
	elif stage == 5:
		print("| |       \\_||_/")
		print("| |         ||")
		print("| |        _||")
		print("| |       |")
	elif stage == 6:
		print("| |       \\_||_/")
		print("| |         ||")
		print("| |        _||_")
		print("| |       |    |")

	print("| |")
	print("====================")

def print_board(board):
	print("Word: ")
	for index in range(len(board)):
		print(board[index], end = " ")
	print()

def print_letters(guessed):
	print("Letters not guessed: ")
	all_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	for index in range(len(all_letters)):
		if all_letters[index] in guessed:
			print("_", end = " ")
		else:
			print(all_letters[index], end = " ")
	print()

def get_empty_board (word):
	return "_" * len(word)

def get_new_board (word, board, letter):
	for index in range(len(word)):
		if word[index] == letter:
			board = board[:index] + letter + board[index + 1:]
	return board

def get_guess(players, current_player):
	letter = input(f"{players[current_player]['name']}, what letter would you like to guess? ")
	return letter.upper()

def compare_boards(board1, board2):
	changes = 0
	for index in range(len(board1)):
		if board1[index] != board2[index]:
			changes += 1
	return changes

def print_scoreboard(players):
	print("Scoreboard: ")
	sorted_players = sorted(players, key = itemgetter('score'), reverse = True)
	place = 1
	for player in sorted_players:
		print(f"{place}. {player['name']}: {player['score']}")
		place += 1

def print_winner(players):
	sorted_players = sorted(players, key = itemgetter('score'), reverse = True)
	print("And the winner is... ")
	time.sleep(2)
	print(sorted_players[0]['name'].upper())
		

def game():
	os.system("clear")
	print("Welcome to Hangman by Daphne Salisbury")
	players = get_players()
	num_rounds = get_num_rounds()
	difficulty = get_difficulty()
	words = load_words()
	for round in range(num_rounds):
		print(f"Round {round + 1}")
		current_player = 0
		stage = 0
		guessed = list()
		word = get_word(words, difficulty)
		board = get_empty_board(word)
		while board != word and stage < 6:
			os.system("clear")
			print_hangman(stage)
			print_board(board)
			print_letters(guessed)
			letter = get_guess(players, current_player)
			guessed.append(letter)
			new_board = get_new_board(word, board, letter)
			changes = compare_boards(board, new_board)
			board = new_board
			if changes == 0:
				stage += 1
				print("\nThat letter was not in the word, next player")
				current_player += 1
				if current_player == len(players):
					current_player = 0
			else:
				players[current_player]['score'] += 10 * changes
				print("\nGood job, that letter was in the word")
		if stage == 6:
			print_hangman(stage)
			print("Word Not Completed")
		else: 
			print("Word Completed")	
		print_board(word)
		print(f"Round {round + 1} Over")
		print_scoreboard(players)

	print_winner(players)
		

if __name__ == "__main__":
	game()






