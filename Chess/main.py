import numpy as np
import inputs,game

def winner(board):
  if ("👌" not in board) or ("🕴" in board[7]):
    print("  PC Winner  ")
    return False
  elif ("🕴" not in board) or ("👌" in board[0]):
    print("  Player Winner  ")
    return False

alp=np.array(["A"," B"," C"," D"," E"," F"," G"," H"])
dalp=np.array(["A","B","C","D","E","F","G","H"])
first=["ч","б","ч","б","ч","б","ч","б"] 
second=["б","ч","б","ч","б","ч","б","ч"] 
third=["ч","б","ч","б","ч","б","ч","б"] 
fourth=["б","ч","б","ч","б","ч","б","ч"]
fifth=["ч","б","ч","б","ч","б","ч","б"]
sixth=["б","ч","б","ч","б","ч","б","ч"]
seventh=["ч","б","ч","б","ч","б","ч","б"]
eight=["б","ч","б","ч","б","ч","б","ч"] 
board=np.matrix([first,second,third,fourth,fifth,sixth,seventh,eight])
board=np.reshape(board,(8,8)) 
name=input("Player Name : ")
with open("logmove.txt","a")as log:
  log.write(name+"\n")
print(f"\n         {alp}\n\n       1 {first} 1\n       2 {second} 2\n       3 {third} 3\ncenter 4 {fourth} 4 center\n       5 {fifth} 5\n       6 {sixth} 6\n       7 {seventh} 7\n       8 {eight} 8\n\n         {alp}\n\nWelcome",name, "Please Assign your Pawns on the board .\nNote: you Can't Assign your Pawns further than 4 row \n")

def print_board(matrix,alp=alp):
  c=1
  alp=alp
  print(f"\n   {dalp}\n")
  for i in matrix:
    print(c,i,c)
    c+=1 
  print(f"\n   {dalp}\n")


for i in range (6):
  board=inputs.inpu_user(board)
print_board(board)#just to print the board
print ("PC Turn inputs >> \n")
for i in range (6):
  board=inputs.pc_inpu(board)
print_board(board)# printing the board

while True: 

  #Player move
  board=game.player_move(board)#play
  print_board(board)#print

  if winner(board)==False:#winner
   break
  
  #PC move
  game.PC_move(board)#play
  print_board(board)#print

  if winner(board)==False:#winner
   break

  if game.PC_move(board)==False:
    print("-----  IT'S A DRAW  -----")
    break


