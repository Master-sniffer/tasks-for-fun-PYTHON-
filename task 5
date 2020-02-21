
class Persona:
  def vozrast (self,one):
    self.one=one
    self.one=int(self.one)
    self.age= 2020-self.one
    return self.age

  def abiturient (self, surname,bd,fac):
    age=self.vozrast(bd)
    print (" Моя фамилия :", surname,"\n", "Дата рождения :", bd , "\n Мой факультет :" , fac, "\n Мне " , age , "лет" )
    
    if age < 25:
      molodoi.append(surname)
    elif age < 35 and age >=25 :
      miaso.append(surname)
    elif age >=35 and age <=200 :
      stari.append(surname)
  
  def student (self, surname, bd , fac , course):
    age=self.vozrast(bd)
    print (" Моя фамилия :", surname,"\n", "Дата рождения :", bd , "\n Мой факультет :" , fac , "\n я на " , course , " курсе" , "\n Мне " , age , "лет")

    if age < 25:
      molodoi.append(surname)
    elif age < 35 and age >=25 :
      miaso.append(surname)
    elif age >=35 and age <=200 :
      stari.append(surname)
  
  def prepodavatel (self,surname,bd, fac, wstat, exp):
    age=self.vozrast(bd)
    print (" Моя фамилия : ", surname,"\n", "Дата рождения : ", bd , "\n Мой факультет :" , fac, "\n мой стаж : ",wstat, "\n мой опыт : " , exp ," лет" , "\n Мне " , age , "лет")

    if age < 25:
      molodoi.append(surname)
    elif age < 35 and age >=25 :
      miaso.append(surname)
    elif age >=35 and age <=200 :
      stari.append(surname)    

class abiturient(Persona):
  def infa (self, surname ,bd,fac):
    super().abiturient(surname,bd,fac)

class student(Persona):
  def infa (self, surname, bd, fac ,course):
    super().student(surname,bd,fac,course)

class prepod(Persona):
  def infa (self,surname,bd, fac, wstat, exp):
    super().prepodavatel(surname,bd, fac, wstat, exp)



x=str(input(("Здравствуйте ! Что вы хотите сделать ? Найти человека в возрастном диапозоне - Y . Вбить информацию о человеке - N . \n")))
if x == "N" or x=="n":
  x=str(input("Вы выбрали 2 функцию. Пожалуйста, введите, кого вы хотите вбить : A - абитуриент, B - студент, C - препод \n"))
  if x=="A" or x=="a":
    a= str(input("Введите фамилию абитуриента :"))
    b= int(input("Введите год рождения абика :"))
    c= str(input("Введите название факультета :"))

    k= abiturient()
    k.infa(a,b,c)

  elif x=="B" or x=="b":
    a= str(input("Введите фамилию студента :"))
    b= int(input("Введите год рождения студента :"))
    c= str(input("Введите название факультета :"))
    d= int(input("На каком сейчас курсе студент :"))

    k= student()
    k.infa(a,b,c,d)

  elif x=="C" or x=="c":
    a= str(input("Введите фамилию преподавателя :"))
    b= int(input("Введите год рождения :"))
    c = str(input("введите название факультета :"))
    d= int(input("введите рабочий стаж :"))
    e= int (input("Введите опыт преподавателя :"))

    k=prepod()
    k.infa(a,b,c,d,e)

elif x=="Y" or "y":
  stari=["Vasiliev", "kartechkin"]
  molodoi=["druzhko", "harlamov"]
  miaso=["Doodoo", "pewdiepie"]
  x=int(input("введите примерный возраст человека \n"))
  if (25 > x): 
    print (molodoi)
  elif x>=25 and x<35 :
    print (miaso)
  elif x>=35 :
    print (stari)
else:
  print ("game over, snake")
