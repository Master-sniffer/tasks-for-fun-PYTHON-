import array
import itertools 
import string
from collections import Counter
table = str.maketrans("", '', "!@#$%^&*_+|+\/:;[]{}<>n")
string=string.ascii_lowercase
ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '
import sys
import numpy as np
import numpy as geek
from random import randint
import random
import numpy
import array as ar
import timeit
import numpy as num
from numpy import array, matrix
print ("first task")
ar1 = ar.array ('i', [])
x=int(input("введите кол-во чисел в массиве\n"))
count=0
for i in range (x):
  j=randint(-100,100)
  ar1.append(j)
print (ar1)
for i in range (len(ar1)):
  if ar1[i]>0 and ar1[i]%2==0:
    count=count+ar1[i]
print ("сумма четных положительный четных чисел=", count)

print ("second task\n")
ar2 = ar.array ('i', [])
x=int(input("введите кол-во чисел в массиве\n"))
maxa=0
for i in range (x):
  j=randint(-1000,1000)
  ar2.append(j)
print (ar2)
for i in range (len(ar2)):
  if i==0:
    maxa=ar2[i]
  if ar2[i]>maxa and i%2==0:
    maxa=ar2[i]
print (maxa)

print ("third task\n")
N=int(input("how many rows in the matrix ?\n"))
M=int(input("how many columns in the matrix ?\n"))
A=np.random.randint(-10,10,(N,M))
print ("your matrix is\n")
B = A.transpose()
print(A)
H=int(input("Enter the number which is required to be found\n"))
count=0
zak=0
for i in range (len(B)):
  for j in range (len(B[i])):
    if zak==i:
      pass
    elif H==B[i][j]:
      count=count+1
      zak=i
print (count)

print ("fourth task\n")
ark=ar.array("i",[])
x=int(input("введите кол-во чисел в массиве\n"))
kak=int(input("хотите сами ввести числа ? -1 или автоматом ? -2 \n"))
if kak==2:
  M=int(input("в таком случае введите от какого числа\n"))
  N=int(input("И до какого\n"))
jazz=0
puff=""
if kak==1:
  print("готовьтесь вводить числа\n")
for k in range (x):
  if kak==1:
    jaj=int(input())
    jazz=jazz+jaj
    ark.append(jaj)
  elif kak==2:
    jaj=randint(M,N)
    jazz=jazz+jaj
    ark.append(jaj)
  else :
    print("game over, snake\n")
    exit()
print (f"вот-с ваш массив - {ark}\n")
pak=jazz/(len(ark))
for i in range (len(ark)):
  if ark[i]<pak:
    bat=ark[i]
    bat=""+str(bat)+", "
    puff=puff+bat
print (f"вот эти числа являются меньше сред арифметического "+puff)

print ("fifth task\n")
ark=ar.array("i",[])
x=int(input("введите кол-во чисел в массиве\n"))
kak=int(input("хотите сами ввести числа ? -1 или автоматом ? -2 \n"))
if kak==2:
  M=int(input("в таком случае введите от какого числа\n"))
  N=int(input("И до какого\n"))
jazz=0
puff=""
if kak==1:
  print("готовьтесь вводить числа\n")
for k in range (x):
  if kak==1:
    jaj=int(input())
    jazz=jazz+jaj
    ark.append(jaj)
  elif kak==2:
    jaj=randint(M,N)
    jazz=jazz+jaj
    ark.append(jaj)
  else :
    print("game over, snake\n")
    exit()
print (f"вот-с ваш массив - {ark}\n")
ark=ark.tolist()
a=min(ark)
ark.remove(a)
a=min(ark)
ark.remove(a)
print (ark)

print ("sixth task\n")
ark=ar.array("i",[])
x=int(input("введите кол-во чисел в массиве\n"))
kak=int(input("хотите сами ввести числа ? -1 или автоматом ? -2 \n"))
if kak==2:
  M=int(input("в таком случае введите от какого числа\n"))
  N=int(input("И до какого\n"))
jazz=0
if kak==1:
  print("готовьтесь вводить числа\n")
for k in range (x):
  if kak==1:
    jaj=int(input())
    jazz=jazz+jaj
    ark.append(jaj)
  elif kak==2:
    jaj=randint(M,N)
    jazz=jazz+jaj
    ark.append(jaj)
  else :
    print("game over, snake\n")
    exit()
print (f"вот-с ваш массив - {ark}\n")
pakak=int(input("Введите от какого числа будем удалять значения\n"))
akaka=int(input("И до какого ?\n"))
for i in range (len(ark)-1):
  if ark[i]>=pakak and ark[i]<=akaka:
    ark.remove(ark[i]) 
print (f"вот что осталось от твоей матрицы -{ark} !\n")

print ("seventh task\n")
ark=np.array([])
x=int(input("введите кол-во чисел в массиве\n"))
kak=int(input("хотите сами ввести числа ? -1 или автоматом ? -2 \n"))
if kak==2:
  M=int(input("в таком случае введите от какого числа\n"))
  N=int(input("И до какого\n"))
jazz=0
bass=[]
if kak==1:
  print("готовьтесь вводить числа\n")
for k in range (x):
  if kak==1:
    jaj=int(input())
    jazz=jazz+jaj
    bass.append(jaj)
  elif kak==2:
    jaj=randint(M,N)
    jazz=jazz+jaj
    bass.append(jaj)
  else :
    print("game over, snake\n")
    exit()
ark=np.append(bass,0)
print (ark)
print (f"вот-с ваш массив - {ark}\n")
bass=-1
for i in range (len(ark)):
  if bass!=-1:
    pass
  elif (ark[i]<0):
    bork=ark.tolist()
    bass=bork.index((bork[i]))+1
lak=0
for i in range (bass,len(ark)):
  lak=lak+ark[i]
print (lak,"вот сток числе у тобi будет в сумме\n")

print ("eight task\n")
ark=[]
x=int(input("введите кол-во книг в массиве\n"))
jeka=""
for i in range (x):
  jeka=""
  gak=randint(1,15)
  for k in range (gak):
    kik=random.choice(ascii_letters)
    jeka=jeka+(kik)
  ark.append(jeka)
ark=sorted(ark)
print ("вот как бы книги, которые у нас есть ",ark)
jeka=str(input("Какую книгу вы хотите добавить ? Напишите ее здесь\n"))
ark.append(jeka)
ark=sorted(ark)
print ("ваша обновленная библиотека",ark)

print ("ninth task\n")
ark=ar.array("i",[])
x=int(input("введите кол-во чисел в массиве\n"))
kak=int(input("хотите сами ввести числа ? -1 или автоматом ? -2 \n"))
if kak==2:
  M=int(input("в таком случае введите от какого числа\n"))
  N=int(input("И до какого\n"))
jazz=0
matrix=[]
if kak==1:
  print("готовьтесь вводить числа\n")
for k in range (x):
  if kak==1:
    jaj=int(input())
    jazz=jazz+jaj
    ark.append(jaj)
  elif kak==2:
    jaj=randint(M,N)
    jazz=jazz+jaj
    ark.append(jaj)
  else :
    print("game over, snake\n")
    exit()
print (f"вот-с ваш массив - {ark}\n")
jazz=[]
kazz=[]
for i in range(len(ark)):
  if i%2==0 and ark[i]>0:
    jazz.append(ark[i])
    kazz.append(i)
jazz.sort()
matrix.append(kazz)
matrix.append(jazz)
print (matrix)
for j in range (len(matrix[0])):
  k=matrix[0][j]
  ark[k]=matrix[1][j]
print (ark)

print ("tenth task\n")
ark=[]
skok=int(input("сколько будет массивов ?\n"))
kak=int(input("хотите сами ввести числа ? -1 или автоматом ? -2 \n"))
if kak==2:
  M=int(input("в таком случае введите от какого числа\n"))
  N=int(input("И до какого\n"))
jazz=0
count=0
for i in range (skok):
  if kak==1:
    print("готовьтесь вводить числа\n")
  x=int(input("введите кол-во чисел в массиве\n"))
  count=count+x
  matrix=[]
  for k in range (x):
    if kak==1:
      jaj=int(input())
      jazz=jazz+jaj
      matrix.append(jaj)
    elif kak==2:
      jaj=randint(M,N)
      jazz=jazz+jaj
      matrix.append(jaj)
    else :
      print("game over, snake\n")
      exit()
  ark.append(matrix)
print (f"вот-с ваш массив - {ark}\n")
baka="эти множества совпадают "
kik=1
for i in range (len(ark)):
  for k in range (len(ark[i])):
    bik=ark[i][k]
    kik=i
    if kik+1<len(ark):
      kik=i+1
      for kak in range (len(ark[kik])): #вход в след массив
        if bik==ark[kik][kak]:
          krz=str(bik)
          baka=baka+krz+","
print (baka)

print ("eleventh task\n")
ark=ar.array("i",[])
x=int(input("Сколко раз вы хотите вписать в этот список всякую всячину ???!?!?!?!?\n"))
print ("сейчас надо будет вводить числа, насчет 3 ! готовсь ! МАРШ !\n")
for i in range(x):
  k=int(input())
  bark=ark.tolist()
  for j in range (len(bark)):
    ark.append(bark[j])
  ark.append(k)
print (ark)

print ("twelfth task, ae\n")
print ("Hello ladies and getntlemen ! Today we will have some fun. First we will have some fun with arrays and then we will try list. Time will be written, so keep ur pants dry and smile on !\n")
print ("Now i will make a will add some words in our magical box,called array. then i will ask u to write how many times word itmathrepetitor will be written \n ")
x=int(input("How many times this word will be written ?\n"))
a=timeit.default_timer()
ark=np.array([])
jj=""
for i in range (10):
  k=random.choice(ascii_letters)
  jj=jj+k  
ark=numpy.append(ark, jj)
print (ark)
for i in range (x):
  k="itmathrepetitor"
  ka="silence"
  ark=numpy.append(ark,k)
  vhod=np.where(ark=="itmathrepetitor")
  ark=numpy.append(ark,ka)
  ark=numpy.delete(ark,vhod)
print (ark)
print (f"WOW, TIME OF THIS BABY IS {timeit.default_timer()-a}")
kaz=timeit.default_timer()-a
print ("Now let's try to do the same , but with the list, yeap\n")
a=timeit.default_timer()
jj=""
for i in range (10):
  k=random.choice(ascii_letters)
  jj=jj+k  
ark=[]
ark.append(jj)
print (ark)
for i in range (x):
  k="itmathrepetitor"
  ka="silence"
  ark.append(k)
  ark.append(ka)
  ark.remove(k)
print (ark)
print (f"WOW , LIST TIME IS HERE {timeit.default_timer()-a}")
zak=timeit.default_timer()-a
if zak > kaz:
  print ("LIST IS FASTER THAN ARRAY EEEE\n")
else :
  print("ARRAY FASTER THAN LIST")

print ("thirteenth task, ae\n")
print ("Before we start. There is a text file right on left of u , called text.txt please add some rows in it, if u can afford it\n")
print("First try we will try with array, yeap ! Prepare\n")
a = timeit.default_timer()
ark=np.array([])
f = open('text.txt', 'r')
coconut=0
uno=np.array([])
des=np.array([])
tre=np.array([])
for line in f:
  first=len(line)
  second=coconut
  line = line.strip()
  third=line
  coconut=coconut+1
  uno=numpy.append(uno,first)
  des=numpy.append(des,second)
  tre=numpy.append(tre,third)
f.close()
T1= matrix([uno,des,tre])
print (T1)
kaz=timeit.default_timer()-a
print("")
print ("lets try with lists\n")
a = timeit.default_timer()
uno=[]
des=[]
tre=[]
f = open('text.txt', 'r')
for line in f:
  first=len(line)
  second=coconut
  line = line.strip()
  third=line
  coconut=coconut+1
  uno.append(first)
  des.append(second)
  tre.append(third)
f.close()
print (f"{uno}\n{des}\n{tre}\n")
zaz=timeit.default_timer()-a
if zaz > kaz:
  print("list is faster\n")
else:
  print ("array is faster\n")


print ("fourteenth task, ae\n")
print ("First, we gonna try dat crap with students in arrays\n")
a = timeit.default_timer()
fac=np.array([])
students=np.array([])
rak=sum(1 for line in open('stud.txt', "r"))
for i in range (rak):
  buc=np.array([])
  with open("stud.txt") as f:
    lines=f.readlines()
    buck=lines[i]
  k=open("group.txt","r")
  lines=k.readlines()
  lines=str(lines)
  lines=lines.split(",")
  brack=lines[i]
  brack = brack.translate(table)
  k.close() #dadadad

  buc=numpy.append(buc,buck)
  students=numpy.append(students,buc)
  fac=numpy.append(fac,brack)
for i in range (rak):
  print (fac[i]," ",students[i])
kaz= timeit.default_timer() - a

print ("\nNow we will try lists !\n")
a = timeit.default_timer()
fac=[]
stud=[]
rak=sum(1 for line in open('stud.txt', "r"))
for i in range (rak):
  with open("stud.txt","r") as f:
    lines=f.readlines()
    stud=lines[i]
  k=open("group.txt","r")
  lines=k.readlines()
  lines=str(lines)
  lines=lines.split(",")
  fac=lines[i]
  fac = fac.translate(table)
  k.close()
  print (fac," ",stud)
zaz= timeit.default_timer() - a
if zaz>kaz:
  print("\nline is faster , oooo\n")
else :
  print("\nARRRAY WINS THIS FIGHT AGAIN !!!\n")

print ("fifteenth task, ae\n")
print ("First, we gonna try dat crap with students in arrays\n")
surname=np.array([])
name=np.array([])
susa=np.array([])
db=np.array([])
kurs=np.array([])
group=np.array([])
ocenka=np.array([])
rak=sum(1 for line in open('stupeni.txt', "r"))
for i in range (rak):
  with open("stupeni.txt","r") as f:
    bamka=0
    lines=f.readlines()
    lines=lines[i]
    lines = lines.strip()
    lines=lines.split(" ")
    surname=numpy.append(surname,lines[0])
    name=numpy.append(name,lines[1])
    susa=numpy.append(susa,lines[2])
    db=numpy.append(db,int(lines[3]))
    kurs=numpy.append(kurs,int(lines[4]))
    group=numpy.append(group,int(lines[5]))
    numka=lines[6]
    numka = numka.replace(","," ")
    numka=numka.split(" ")
    for i in range (len(numka)):
      bamka=bamka+(int(numka[i]))
    ocenka=numpy.append(ocenka,bamka)
for i in range (1,4):
  i=int(i)
  result = np.where(kurs == i)
  result = list(itertools.chain(*result))  #думай над курсом
  lis=[]
  for k in range (len(result)):
    lis.append(surname[result[k]])
    lis.sort()
  for k in range (len(result)):
    surname[result[k]]=lis[k]
print ("Here are the sorted surnames !\n", surname)
jeka=Counter(group)
gr=max(group)
gr=int(gr)+1
karg=np.zeros(gr)
bp=np.array([])
marxis=np.array([])
for i in range (gr):
  bp=numpy.append(bp,3000)
  marxis=numpy.append(marxis,0)
for po in range (len(group)):
  j=int(group[po])
  kuzu=int(ocenka[po])
  karg[j]=karg[j]+kuzu
  if db[po]<bp[j]:
    bp[j]=db[po]
  if marxis[j]<(ocenka[po]):
    marxis[j]=ocenka[po]
bp=bp[bp!=3000]
marxis=marxis[marxis!=0]
karg = karg[karg != 0]
kagak=group.tolist()
kapot=np.array([])
biber=np.unique([group])
bib=np.array([])
for i in range (len(marxis)):
  result = np.where(ocenka == marxis[i])
  bib=numpy.append(bib,surname[result])

for i in range(10000):
  ju=kagak.count(i)
  if ju!=0:
    kapot=numpy.append(kapot,ju)
  
for i in range (len (kapot)):
  karg[i]=karg[i]/kapot[i]
  print (f"The average score in group N {biber[i]} is {karg[i]}\nThe maximum age in group N {biber[i]} is {bp[i]}\nThe best student of the group N {biber[i]} is {bib[i]} with the score {marxis[i]}\n ")


print ("Now we try list\n")
surname=[]
name=[]
susa=[]
db=[]
kurs=[]
group=[]
ocenka=[]
rak=sum(1 for line in open('stupeni.txt', "r"))
for i in range (rak):
  with open("stupeni.txt","r") as f:
    bamka=0
    lines=f.readlines()
    lines=lines[i]
    lines = lines.strip()
    lines=lines.split(" ")
    surname.append(lines[0])
    name.append(lines[1])
    susa.append(lines[2])
    db.append(int(lines[3]))
    kurs.append(int(lines[4]))
    group.append(int(lines[5]))
    numka=lines[6]
    numka = numka.replace(","," ")
    numka=numka.split(" ")
    for i in range (len(numka)):
      bamka=bamka+(int(numka[i]))
    ocenka.append(bamka)
for i in range (1,4):
  i=int(i)
  result = np.where(kurs == i)
  result = list(itertools.chain(*result))  #думай над курсом
  lis=[]
  for k in range (len(result)):
    lis.append(surname[result[k]])
    lis.sort()
  for k in range (len(result)):
    surname[result[k]]=lis[k]
print ("Here are the sorted surnames !\n", surname)
jeka=Counter(group)
gr=max(group)
gr=int(gr)+1
karg=[0] * gr
bp=[]
marxis=[]
for i in range (gr):
  bp.append(3000)
  marxis.append(0)
for po in range (len(group)):
  j=int(group[po])
  kuzu=int(ocenka[po])
  karg[j]=karg[j]+kuzu
  if db[po]<bp[j]:
    bp[j]=db[po]
  if marxis[j]<(ocenka[po]):
    marxis[j]=ocenka[po]
for i in range ((gr)):
  if 3000 in bp:
    bp.remove(3000)
  if 0 in marxis:
    marxis.remove(0)
  if 0 in karg:
    karg.remove(0)
kagak=group
kapot=[]
biber=np.unique([group])
bib=np.array([])
for i in range (len(marxis)):
  result = np.where(ocenka == marxis[i])
  bib=numpy.append(bib,surname[result])

for i in range(10000):
  ju=kagak.count(i)
  if ju!=0:
    kapot.append(ju)
  
for i in range (len (kapot)):
  karg[i]=karg[i]/kapot[i]
  print (f"The average score in group N {biber[i]} is {karg[i]}\nThe maximum age in group N {biber[i]} is {bp[i]}\nThe best student of the group N {biber[i]} is {bib[i]} with the score {marxis[i]}\n ")
print ("Array is faster  !\n")

print ("sixteenth task, ae\n")
a = timeit.default_timer()
print ("First, we gonna try dat crap with matrix in arrays\n")
first=np.array([])
second=np.array([])
mar1=[]
mar2=[]
for i in range (4):
  like=[]
  x=randint(-100,100)
  y=randint(-100,100)
  z=randint(-100,100)
  h=randint(-100,100)
  like.append(x)
  like.append(y)
  like.append(z)
  like.append(h)
  first=numpy.append(first,like)
  like=[]
  x=randint(-100,100)
  y=randint(-100,100)
  z=randint(-100,100)
  h=randint(-100,100)
  like.append(x)
  like.append(y)
  like.append(z)
  like.append(h)
  second=numpy.append(second,like)
first=first.reshape(4,4)
second=second.reshape(4,4)
print (first)
print (second)
x=int(input ("What you want to do with this matrixes ? *+* - 1 , *-* - 2, * multiply* - 3 , *divide* - 4\n "))
if x==1:
  a=int (input("вы хотите сами ввести число - просто введите число или же сделать это на матрицу ( введите -1 )\n"))
  if a==-1:
    print (first+second)
  else:
    x=int (input("Введите число\n"))
    a=int(input("Введите номер матрицы\n"))
    if a==1:
      for i in range (len(first)):
        for j in range (len(first[i])):
          first[i][j]=first[i][j]+x
      print (first)
    if a==2:
      for i in range (len(second)):
        for j in range (len(second[i])):
          second[i][j]=second[i][j]+x
      print (second)
if x==2:
  a=int (input("вы хотите сами ввести число - просто введите число или же сделать это на матрицу ( введите -1 )\n"))
  if a==-1:
    print (first-second)
  else:
    x=int (input("Введите число\n"))
    a=int(input("Введите номер матрицы\n"))
    if a==1:
      for i in range (len(first)):
        for j in range (len(first[i])):
          first[i][j]=first[i][j]-x
      print (first)
    if a==2:
      for i in range (len(second)):
        for j in range (len(second[i])):
          second[i][j]=second[i][j]-x
      print (second)
if x==4:
  a=int (input("вы хотите сами ввести число - просто введите число или же сделать это на матрицу ( введите -1 )\n"))
  if a==-1:
    print (first/second)
  else:
    x=int (input("Введите число\n"))
    a=int(input("Введите номер матрицы\n"))
    if a==1:
      for i in range (len(first)):
        for j in range (len(first[i])):
          first[i][j]=first[i][j]/x
      print (first)
    if a==2:
      for i in range (len(second)):
        for j in range (len(second[i])):
          second[i][j]=second[i][j]/x
      print (second)
if x==3:
  a=int (input("вы хотите сами ввести число - просто введите число или же сделать это на матрицу ( введите -1 )\n"))
  if a==-1:
    print (first*second)
  else:
    x=int (input("Введите число\n"))
    a=int(input("Введите номер матрицы\n"))
    if a==1:
      for i in range (len(first)):
        for j in range (len(first[i])):
          first[i][j]=first[i][j]*x
      print (first)
    if a==2:
      for i in range (len(second)):
        for j in range (len(second[i])):
          second[i][j]=second[i][j]*x
      print (second)
kaz=timeit.default_timer()-a
a = timeit.default_timer()
print ("Now we will try lists\n")
first=[]
second=[]
for i in range (4):
  like=[]
  x=randint(-100,100)
  y=randint(-100,100)
  z=randint(-100,100)
  h=randint(-100,100)
  like.append(x)
  like.append(y)
  like.append(z)
  like.append(h)
  first.append(like)
  like=[]
  x=randint(-100,100)
  y=randint(-100,100)
  z=randint(-100,100)
  h=randint(-100,100)
  like.append(x)
  like.append(y)
  like.append(z)
  like.append(h)
  second.append(like)
print (first)
print (second)
x=int(input ("What you want to do with this matrixes ? *+* - 1 , *-* - 2, * multiply* - 3 , *divide* - 4\n "))
if x==1:
  a=int (input("вы хотите сами ввести число - просто введите число или же сделать это на матрицу ( введите -1 )\n"))
  if a==-1:
    print (first+second)
  else:
    x=int (input("Введите число\n"))
    a=int(input("Введите номер матрицы\n"))
    if a==1:
      for i in range (len(first)):
        for j in range (len(first[i])):
          first[i][j]=first[i][j]+x
      print (first)
    if a==2:
      for i in range (len(second)):
        for j in range (len(second[i])):
          second[i][j]=second[i][j]+x
      print (second)
if x==2:
  a=int (input("вы хотите сами ввести число - просто введите число или же сделать это на матрицу ( введите -1 )\n"))
  if a==-1:
    print (first-second)
  else:
    x=int (input("Введите число\n"))
    a=int(input("Введите номер матрицы\n"))
    if a==1:
      for i in range (len(first)):
        for j in range (len(first[i])):
          first[i][j]=first[i][j]-x
      print (first)
    if a==2:
      for i in range (len(second)):
        for j in range (len(second[i])):
          second[i][j]=second[i][j]-x
      print (second)
if x==4:
  a=int (input("вы хотите сами ввести число - просто введите число или же сделать это на матрицу ( введите -1 )\n"))
  if a==-1:
    print (first/second)
  else:
    x=int (input("Введите число\n"))
    a=int(input("Введите номер матрицы\n"))
    if a==1:
      for i in range (len(first)):
        for j in range (len(first[i])):
          first[i][j]=first[i][j]/x
      print (first)
    if a==2:
      for i in range (len(second)):
        for j in range (len(second[i])):
          second[i][j]=second[i][j]/x
      print (second)
if x==3:
  a=int (input("вы хотите сами ввести число - просто введите число или же сделать это на матрицу ( введите -1 )\n"))
  if a==-1:
    print (first*second)
  else:
    x=int (input("Введите число\n"))
    a=int(input("Введите номер матрицы\n"))
    if a==1:
      for i in range (len(first)):
        for j in range (len(first[i])):
          first[i][j]=first[i][j]*x
      print (first)
    if a==2:
      for i in range (len(second)):
        for j in range (len(second[i])):
          second[i][j]=second[i][j]*x
      print (second)
zak=timeit.default_timer()-a
if kaz<zak:
  print ("array is faster\n")
else :
  print ("list is faster\n")

print ("seventeenth task, yeap !\n")
ark=ar.array("i",[1,2,3,4,5,6,7,8,9,10])
x=int (input("Сколько раз будут проводить движения ?\n"))
for i in range (x):
  ab=int(input("Движение влево - 1 , движение вправо - 2\n"))
  rag=int(input("На сколько клеток двигаемся ?\n"))
  if ab==1:
    kaz=ark.tolist()
    ark=ar.array("i",[])
    for k in range (rag):
      ark.append(0)
    for k in range (len(kaz)): 
      ark.insert (0,kaz[k])
    print (ark)
  elif ab==2:
    for i in range (rag):
      ark.insert(0,0)
  print (ark)

print ("eighteenth task, yeap !\n")
ark=ar.array("i",[])
x=int (input("Введите сколько раз мы будем заполнять случайные числа\n"))
for i in range (x):
  ka=randint(-1000,1000)
  ark.append(ka)
print (ark)
for i in range (len(ark)):
  if ark[i]<0:
    ark[i]=-1
for i in range (len(ark)):
  if -1 in ark:
    ark.remove(-1)
print (ark)

print ("nineteenth task, yeap !\n")
print ("type in numbers. If the number will be = 0 u will stop entering numbers\n")
x=1
ark=ar.array("i",[])
while x!=0:
  x=int(input("Введите число\n"))
  if x==0:
    pass
  else:
    ark.append(x)
print (ark)
x=int(input("Введите число, которые вы хотите вставить в место\n"))
y=int(input("Введите место, где надо вбить\n"))
ark.insert(y,x)
print (ark)

print ("twenteeth task, boiiii !\n")
ark=np.array([])
dark=np.array([])
bark=np.array([])
x=int (input("Сколько будет числе в массиве ?\n"))
for i in range (x):
  k=int(input("Введите число\n"))
  ark=numpy.append(ark,k)
  k=randint(-100,100)
  dark=numpy.append(dark,k)
print (ark)
print (dark)
for i in range (x):
  k=ark[i]+dark[i]
  bark=numpy.append(bark,k)
print (bark)

print ("twenty first task, boiiii !\n")
ark=np.array([])
counta=0
counti=0
counto=0
for i in range (2000):
  x=randint(-5,4)
  if x>0:
    counta=counta+1
  elif x==0:
    counto=counto+1
  elif x<0:
    counti=counti+1
print ("значений больше 0 ", counta,"\nзначений равные 0 ", counto,"\n","значений меньше 0 ", counti,"\n")
  
