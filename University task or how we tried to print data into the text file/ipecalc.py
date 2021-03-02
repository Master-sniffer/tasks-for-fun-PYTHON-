#  Создать кальк для определения адреса сети, с помощью ввода ip и маски сети. 
# Показать в двоичной и дес сис исчесления и показать класс сети
from ipaddress import IPv4Address, IPv4Network


classA = IPv4Network(("10.0.0.0", "255.0.0.0")) #  с помощью библиотеки будем проверять к какому из этих 3 классов принадлежит наша сеть
classB = IPv4Network(("172.16.0.0", "255.240.0.0")) # с помощью библиотеки будем проверять к какому из этих 3 классов принадлежит наша сеть 
classC = IPv4Network(("192.168.0.0", "255.255.0.0")) # с помощью библиотеки будем проверять к какому из этих 3 классов принадлежит наша сеть

ip_user=str(input("Введите ip адрес\nПример: 129.35.58.207 "))
mask=str(input("Введите маску\nПример: 255.255.254.0 "))

clas=ip_user

ip_user=ip_user.split(".")
mask=mask.split(".")
add=["","","",""]

for la in range(len(ip_user)):
  num=int(ip_user[la])
  base = 2
  if not(2 <= base <= 9):
      quit()

  newNum = ''

  while num > 0:
      newNum = str(num % base) + newNum
      num //= base

  #print(newNum)
  ip_user[la]=newNum


for la in range(len(mask)):
  num=int(mask[la])
  base = 2
  if not(2 <= base <= 9):
      quit()

  newNum = ''

  while num > 0:
      newNum = str(num % base) + newNum
      num //= base

  #print(newNum)
  mask[la]=newNum


# da=ip_user[0]
# da=list(da)
# print (da)


for i in range (len(add)):
  lis2=ip_user[i]
  lis1=mask[i]

  lis1=list(lis1)
  lis2=list(lis2)

  
  change2=8-(len(lis2))
  change1=8-len(lis1)

  if change2>0:
    for _ in range(change2):
      lis2.insert(0,0)
  
  if change1>0:
    for _ in range(change1):
      lis1.insert(0,0)
    
  # print ((lis1))
  # print (lis2)

  result=""

  for j in range(len(lis1)):
    end=int(lis1[j]) * int(lis2[j])

    result+=str(end)
  
  add[i]=result

print (add , "Адрес сети в двоичном виде")

result=""
for i in range (len(add)):
  numb=int(add[i],2)
  result+=str(numb)+"."

result=result[:-1]
print (result, "Адрес сети в дес виде") 


clas=IPv4Address(clas)
if clas in classA:
  print (clas,"is A class network")

elif clas in classB:
  print (clas,"is B class network")

elif clas in classC:
  print (clas,"is C class network")

else:
  print ("cant see the class of the network\nciao!")
  exit(0)
