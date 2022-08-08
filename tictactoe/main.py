board = [' ' for x in range(10)]

def insertLetter(letter, pos):
  board[pos] = letter

def spaceIsFree(pos):
  return board[pos] == ' '

def printBoard(board):
  print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
  print('-----------')
  print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
  print('-----------')
  print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
  

def checkVerticalLines(board, letter):
  return (board[1] == letter and board[4] == letter and board[7] == letter) or (board[2] == letter and board[5] == letter and board[8] == letter) or (board[3] == letter and board[6] == letter and board[9] == letter)

def checkHorizontalLines(board, letter):
  return (board[1] == letter and board[2] == letter and board[3] == letter) or (board[4] == letter and board[5] == letter and board[6] == letter) or (board[7] == letter and board[8] == letter and board[9] == letter)

def checkDiagonalLines(board, letter):
  return (board[1] == letter and board[5] == letter and board[9] == letter) or (board[3] == letter and board[5] == letter and board[7] == letter)

def isWinner(board, letter):
  return checkVerticalLines(board, letter) or checkHorizontalLines(board, letter) or checkDiagonalLines(board, letter)

def playerMove():
  run = True
  while run:
    move = input('Please select a position to place an \'X\' (1-9): ')
    try:
      move = int(move)
      if move > 0 and move < 10:
        if spaceIsFree(move):
          run = False
          insertLetter('X', move)
        else:
          print('Sorry, this space is occupied!')        
      else:
        print('Please type a number within the range!')
    except:
      print('Please type a number!')


def compMove():
  possibleMoves = [index for index, letter in enumerate(board) if letter == ' ' and index != 0]
  move = 0

  #Solution 1 and 2
  #Check if there is a move that results in a win or if we can block a player winning move
  for let in ['O', 'X']:
    for i in possibleMoves:
      boardCopy = board[:]
      boardCopy[i] = let
      if(isWinner(boardCopy, let)):
        move = i
        return move

  #Solution 3
  #Look for all available corners and randomly select one
  openCorners = []
  for i in possibleMoves:
    if i in [1,3,7,9]:
      openCorners.append(i)

  if len(openCorners) > 0:
    move = selectRandom(openCorners)
    print(move)
    return move

  #Solution 4
  #Check if center is open
  if 5 in possibleMoves:
    move = 5
    return move

  #Solution 5
  #Check open edges and select one randomly
  openEdges = []
  for i in possibleMoves:
    if i in [2,4,6,8]:
      openEdges.append(i)

  if len(openEdges) > 0:
    move = selectRandom(openEdges)
    return move
  
  return move

  

def selectRandom(availableSpaces):
  import random
  ln = len(availableSpaces)
  r = random.randrange(0, ln)
  return availableSpaces[r]

def isBoardFull(board):
  return not(board.count(' ') > 1)    

def play():
  print('Welcome to Tic Tac Toe!')
  printBoard(board)

  while not(isBoardFull(board)):
    if not(isWinner(board, 'O')):
      playerMove()
      printBoard(board)
    else:
      print('Sorry, O\'s won this time!')
      break

    if not(isWinner(board, 'X')):
      move = compMove()
      if move != 0:
        insertLetter('O', move)
        print('Computer placed an \'O\' in position', move, ':')
        printBoard(board)
    else:
      print('X\'s won this time! Good job!')
      break

  if isBoardFull(board):
    print('Tie Game!')

if __name__ == '__main__':
  play()