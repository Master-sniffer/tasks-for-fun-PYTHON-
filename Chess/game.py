lll=["a","b","c","d","e","f","g","h"]
num=str("12345678")

#Player Move
def player_move(Matrix):
  okay=0
  d=0
  c=0
  hint=""
  for i in range(7):
    for j in range(7):
      if Matrix[i,j]=="👌":
        if Matrix[i-1,j-1]=="ч" or Matrix[i-1,j+1]=="ч":
         hint=str(i+1)+lll[j]
        elif (Matrix[i-1,j-1]=="🕴" or Matrix[i-1,j+1]=="🕴") and (Matrix[i-2,j-2]=="ч" or Matrix[i-2,j+2]=="ч"):
         hint=str(i+1)+lll[j]
        elif Matrix[i-1,j-1]!="ч" and Matrix[i-1,j+1]!="ч" and Matrix[i-2,j-2]!="ч" and Matrix[i-2,j+2]!="ч":# if there is no hint and no moves so he lose 
          d+=1
        c+=1
  print(c)
  if d==c:
    print("--- PLAYER LOOSE ---")
    exit()

  while okay==0:
    NN=input("\nExample: Move (1a-2b) or Attack(1a:3c)\n Player Enter Movement>> ")#user input

    if len(NN)==5:#5 charector allowed 

      if NN[0] in num and NN[1] in lll and NN[3] in num and NN[4] in lll and (NN[2]=="-" or NN[2]==":"):
        #check input if it look like 1a-2b to move or 1a:3c to Attack
        
        log=open("logmove.txt","a")
        N=str(NN)
        old_x=int(N[0])-1#the current Pawn ROW
        old_y=lll.index(N[1])#the current Pawn Column
        new_x=int(N[3])-1#the NEW Pawn ROW
        new_y=lll.index(N[4])#the New Pawn Column 

        if Matrix[old_x,old_y]=="🕴":#if he choose PC Pawn
          print("It's a PC Pawn Not Allowed to move it\nTry Again")
          
        
        if Matrix[old_x,old_y]=="ч" or Matrix[old_x,old_y]=="б" or Matrix[new_x,new_y]=="б":
          print("You Picked Up A Blanked Pawn \nTry Again")
          
        
        if N[2]=="-":#for movment
        
          if old_x-1==new_x and (old_y+1==new_y or old_y-1==new_y):#to check if the movment is 1 step forward 
        
            if Matrix[old_x,old_y]=="👌" and Matrix[new_x,new_y]=="ч":#to check if the next cells is avalible for the player 
              Matrix[old_x,old_y],Matrix[new_x,new_y]= Matrix[new_x,new_y],Matrix[old_x,old_y]#swip the Pawns 
              log.write("P1 "+str(N)+"\n")#write in logmove.txt
              okay=1
              return Matrix

        if N[2]==":" :#Attack
          
          if old_x-2==new_x and old_y+2==new_y :#to check if the movment is 2 step forward column on the right
            
            if Matrix[old_x,old_y]=="🕴" and Matrix[new_x,new_y]=="ч"and Matrix[new_x+1,new_y-1]=="🕴":#check the current pawn and new cells and column on the right if behind it is PC Pawn
              Matrix[old_x,old_y],Matrix[new_x,new_y]= Matrix[new_x,new_y],Matrix[old_x,old_y]#swip the Pawns 
              Matrix[new_x+1,new_y-1]="ч"#delete the PC Pawn
              log.write("P1 "+str(N)+"\n")
              okay=1
              return Matrix
            
          if old_x-2==new_x and old_y-2==new_y:#to check if the movment is 2 step forward column on the left
            
            if Matrix[old_x,old_y]=="👌" and Matrix[new_x,new_y]=="ч"and Matrix[new_x+1,new_y+1]=="🕴":#check the current pawn and new cells and column on the left if after it is PC Pawn
              Matrix[old_x,old_y],Matrix[new_x,new_y]= Matrix[new_x,new_y],Matrix[old_x,old_y]#swip the Pawns 
              Matrix[new_x+1,new_y+1]="ч"#delete the PC Pawn
              log.write("P1 "+str(N)+"\n")
              okay=1
              return Matrix 

        log.close()   

    else:
        print("Wrong input please Try Again>>> Example: to move>1a-2b or to Attack >1a:3c \nLength should be 5")
    print("💡 Hint: Move or Attack by",hint)

#PC Move
def PC_move (matrix):
  log=open("logmove.txt","a")
  ki=0
  k=1
  for i in range (7):
    for j in range (7):
      if matrix[i,j]=="🕴" and  k==1:  
        if matrix[i+1,j-1]=="👌" and j-1!=0 and j-1!=7:
          if matrix[i+2,j-2]=="ч":
            matrix[i+2,j-2]="🕴"
            matrix[i,j]="ч"
            matrix[i+1,j-1]="ч" #somewhere here
            k=0
            l=str(i+1)+lll[j]+":"+str(i+3)+lll[j-2]
            log.write("PC "+l+"\n")#LOG
        elif matrix[i+1,j+1]=="👌" and j+1!=0 and j+1!=7:
          if matrix[i+2,j+2]=="ч":
            matrix[i+2,j+2]="🕴"
            matrix[i+1,j+1]="ч"
            matrix[i,j]="ч" #input in log file is needed
            k=0
            l=str(i+1)+lll[j]+":"+str(i+3)+lll[j+2]
            log.write("PC "+l+"\n")#LOG

  if k==1: #if checker cant hit anyone, it just chooses the first random checker and uses it
    for i in range(7):
      for j in range(7):
        if matrix[i,j]=="🕴" and k!=-1:
          if j-1!=-1:
            if matrix[i+1,j-1]=="ч":
              matrix[i+1,j-1]="🕴"
              matrix[i,j]="ч" #here log is needed
              k=-1
              l=str(i+1)+lll[j]+"-"+str(i+2)+lll[j-1]
              log.write("PC "+l+"\n")
          elif j+1!=8:  
            if matrix[i+1,j+1]=="ч":
              matrix[i+1,j+1]="🕴"
              matrix[i,j]="ч" #here log is needed
              k=-1
              l=str(i+1)+lll[j]+":"+str(i+2)+lll[j+1]
              log.write("PC "+l+"\n")
          else:
            ki=ki+1
            if ki==6:
              print("----PLAYER WIN----")
              exit()
  elif k==1:
      return False#it's Ready here just print PLayer win because
    #if k==1 thats mean PC didnt move and this mean no way to go and this mean PLAYER WIN GOT IT! 
    
  log.close()
  return (matrix)






    
