# to check input if its letters then show error
lll=["a","b","c","d","e","f","g","h"]

def inpu_user (matrix):
  log=open("logmove.txt","a")
  num=["1","2","3","4","5","6","7","8"] #this is method to input User's checkers
  okay=0
  
  while okay==0:
    liss=str(input("Enter a Position (ex.>> 3f) :\n"))    
    if liss[0] in num and liss[1] in lll and len(liss)==2:
      x=int(liss[0])-1
      y=str(liss[1])
      if okay==0 :
       okay=1
    else:
     print("Sorry! Ues the right format ex.>> 3f")

  
  if (y=="a" or y=="A") and matrix[x,0]=="ч":# x=row 0=Column
    matrix[x,0]="👌" # first player Pawn
    log.write("P1 > "+liss+"\n")
  elif (y=="b" or y=="B") and matrix[x,1]=="ч":
    matrix[x,1]="👌" #first player Pawn
    log.write("P1 > "+liss+"\n")
  elif (y=="c" or y=="C") and matrix[x,2]=="ч":
    matrix[x,2]="👌" #first player Pawn
    log.write("P1 > "+liss+"\n")
  elif  (y=="d" or y=="D") and matrix[x,3]=="ч":
    matrix[x,3]="👌"#first player Pawn
    log.write("P1 > "+liss+"\n")
  elif (y=="E" or y=="e") and matrix[x,4]=="ч":
    matrix[x,4]="👌"#first player Pawn
    log.write("P1 > "+liss+"\n")
  elif (y=="F" or y=="f") and matrix[x,5]=="ч":
    matrix[x,5]="👌"#first player Pawn
    log.write("P1 > "+liss+"\n")
  elif (y=="G" or y=="g") and matrix[x,6]=="ч":
    matrix[x,6]="👌"#first player Pawn
    log.write("P1 > "+liss+"\n")
  elif (y=="H" or y=="h") and matrix[x,7]=="ч":
    matrix[x,7]="👌"#first player Pawn
    log.write("P1 > "+liss+"\n")
  else :
    print ("Wrong input\nIts a White Cells or out of range input\n")
    return (inpu_user(matrix))
  
  log.close()
  return matrix

def pc_inpu(matrix):
  log=open("logmove.txt","a")
  num1=["1","2","3","4","5","6","7","8"]
  okay=0
  
  while okay==0:
    liss=str(input("Enter a Position (ex.>> 3f) :\n"))    
    if liss[0] in num1 and liss[1] in lll and len(liss)==2:
      x=int(liss[0])-1
      y=str(liss[1])
      if okay==0 :
       okay=1
    else:
     print("Sorry! Ues the right format ex.>> 3f")
     
  if (y=="a" or y=="A") and matrix[x,0]=="ч":# x for row and 0 for column
    matrix[x,0]="🕴"
    log.write("PC > "+liss+"\n")
  elif (y=="b" or y=="B") and matrix[x,1]=="ч":
    matrix[x,1]="🕴"
    log.write("PC > "+liss+"\n")
  elif (y=="c" or y=="C") and matrix[x,2]=="ч":
    matrix[x,2]="🕴"
    log.write("PC > "+liss+"\n")
  elif  (y=="d" or y=="D") and matrix[x,3]=="ч":
    matrix[x,3]="🕴"
    log.write("PC > "+liss+"\n")
  elif (y=="E" or y=="e") and matrix[x,4]=="ч":
    matrix[x,4]="🕴"
    log.write("PC > "+liss+"\n")
  elif (y=="F" or y=="f") and matrix[x,5]=="ч": 
    matrix[x,5]="🕴"
    log.write("PC > "+liss+"\n")
  elif (y=="G" or y=="g") and matrix[x,6]=="ч":
    matrix[x,6]="🕴"
    log.write("PC > "+liss+"\n")
  elif (y=="H" or y=="h") and matrix[x,7]=="ч":
    matrix[x,7]="🕴"
    log.write("PC > "+liss+"\n")
  else :
    print ("Wrong input\nIt's a White Cells or out of range input\n")
    return (pc_inpu(matrix))
  
  log.close()
  return matrix
