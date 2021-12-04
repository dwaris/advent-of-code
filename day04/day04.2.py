#!/usr/bin/env python3
import numpy as np

result = 0

input = np.loadtxt('day04/input.txt',dtype=int,max_rows=1,delimiter=',')
boards = np.loadtxt('day04/input.txt',skiprows=1,dtype=int)
boards = np.array_split(boards,len(boards)/5)

old_boards = []

def game_loop():
	for draw in input:
		for board in boards:
			if hash(str(board)) in old_boards:
				continue
			
			for row in board:
				for i , num in enumerate(row):
					if num == draw:
						row[i] = -1

		for board in boards:
			if hash(str(board)) in old_boards:
				continue

			for row in board:
				if np.max(row) == np.min(row):
					winning = board
					last = draw
					old_boards.append(hash(str(winning)))

			for col in np.column_stack(board):
				if np.max(col) == np.min(col):
					winning = board
					last = draw
					old_boards.append(hash(str(winning)))

	return (winning,last)

winning, last = game_loop()
winning_sum = np.sum(winning[winning>=0])
result = winning_sum * last

print(f"Result: {result}")
