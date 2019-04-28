# game.py is a simple exercise done while training Python skills
# 
#  -----------------------------------------------------------------
#  "Free Pizza and Beer Licence" (Revision 1, 2019-):
#  You can do whatever you want with this stuff with your own risk. 
#  No guarantee whatsoever given or any responsibility taken.
#  If you t2hink this stuff is worth it, you can buy to 
#  a person in need a beer AND/OR a pizza in return.
#  -----------------------------------------------------------------

from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print(" ".join(row))

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

# For debuggin purposes
print(ship_row)
print(ship_col)

for turn in range(4):
  print("Turn", turn + 1)
  guess_row = int(input("Guess Row: "))
  guess_col = int(input("Guess Col: "))

  if guess_row == ship_row and guess_col == ship_col:
    print("Congratulations! You sank my ship!")
    break
  else:
    if guess_row not in range(5) or \
      guess_col not in range(5):
      print("Oops, that's not even in the play area.")
    elif board[guess_row][guess_col] == "X":
      print( "You guessed that one already." )
    else:
      print("You missed my ship!")
      board[guess_row][guess_col] = "X"
    if turn == 3:
      print("Game Over!")
    print_board(board)