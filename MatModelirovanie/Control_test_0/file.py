#Вариант 18
# задания изменить
# поработать с append
# WORK WITH THE TASK 6 AND CHECK OTHERS

import numpy as np # можем делать все и через списки, но numpy быстрее
import copy
import time

class MatModel():
  def __init__(self):
    print("\n")

  def make_matrix(self,matrix):
    matrica =[]
    for x in range(len(matrix)):
        matrica.append([])
        for y in range(len(matrix)):
            matrica[x].append(matrix[x][y])

    return matrica


  def matrixAPP(self,matrica):
      matr =[]
      for x in range(len(matrica)):
          matr.append(matrica[x])
      return np.array(matr) 


  def task_1(self, matr1, matr2 , steps, stat1, stat2):
    for n in range(steps):
      matr2 = np.dot(matr2,matr1)
    print(matr2[stat1][stat2])


  def task_2(self, matr1,matr2,steps,A):
    for _ in range(steps):
        matr2 = np.dot(matr2,matr1)
    matr2 = np.dot(A,matr2)   
    print(matr2) # добавить бы тут ретюрну


  def task_3(self, matr1, matr2,matr3, steps,stat1,stat2):
    for l in range(1, steps): #шаги(сколько шагов, столко и циклов)
        for i in range(len(matr1)):
            for j in range(len(matr1)):
                matr3[i][j] = 0
                for m in range(len(matr1)):
                    if m != j:
                        matr3[i][j] += matr2[m][j] * matr1[i][m]
        for x in range(len(matr3)): # аналог deepcopy
            for y in range(len(matr3)):
                matr2[x][y] = matr3[x][y]
    print(matr2[stat1][stat2])   


  def task_4(self, matr1, matr2,matr3,matr4, steps, stat1,stat2):
    for l in range(1, steps):
        for i in range(len(matr1)):
            for j in range(len(matr1)):
                matr3[i][j] = 0
                for m in range(len(matr1)):
                    if m != j:
                        matr3[i][j] += matr2[m][j] * matr1[i][m]
        matr2 = np.copy(matr3)
        matr4 = matr4 + np.array(matr2)
    print(matr4[stat1][stat2]) 


  def task_5(self, matr1, matr2,matr3, matr4, matr5, steps,stat1,stat2):
    matr4.append(self.make_matrix(matr2))

    for l in range(1, steps):
        for i in range(len(matr1)):
            for j in range(len(matr1)):
                matr3[i][j] = 0
                for m in range(len(matr1)):
                  if m != j:
                      matr3[i][j] += matr2[m][j] * matr1[i][m]
        matr2=np.copy(matr3)
        #np.append(matr4,self.make_matrix(matr2))
        matr4.append(self.make_matrix(matr2))

    #print (matr4)
    for i in range(len(matr1)):
        #np.append(matr5,[])
        matr5.append([])
        for j in range(len(matr1)):
            matr5[i].append(0)
            #np.append(matr5[i],0)
            for k in range(len(matr4)):
                matr5[i][j] += matr4[k][i][j]*(steps+1)
    # for n in matr5:    
    #     #print(n)            
    print(matr5[stat1][stat2])


  def task_6(self, matr1, matr2,steps,stat1):
    matr3 = []
    matr3.append(self.matrixAPP(matr2))
    for i in range(steps-1):
        matr2 = np.dot(matr2,matr1)
        matr3.append(self.matrixAPP(matr2))


    matr4 = []
    for i in range(len(matr1)):
        matr4.append(matr1[i][i])
    matr4 = np.array(matr4) 
    matr5 = self.matrixAPP(matr4)
    matr6 = self.matrixAPP(matr4)
    matr7 = []
    matr7.append(self.matrixAPP(matr5))
    for l in range(1, steps):
        for j in range(len(matr1)):
            matr6[j] = matr3[l][j][j]
            for m in range(l):
              matr6[j] -= matr7[m][j]*matr3[l-m-1][j][j]
            matr5[j] = matr6[j]

        matr7.append(self.matrixAPP(matr5))
    print(matr7[-1][stat1])





  def task_7(self, matr1, matr2,matr3,matr4,steps,stat1):
    for l in range(1, steps):
        for i in range(len(matr1)):
            for j in range(len(matr1)):
                matr3[i][j] = 0
                for m in range(len(matr1)):
                    if m != j:
                        matr3[i][j] += matr2[m][j] * matr1[i][m]
        matr2 = np.copy(matr3)
        matr4 = matr4 + np.array(matr2)
    print(matr4[stat1][stat1]) 


  def task_8(self, matr1, matr2,matr3,matr4,steps):
    #matr 3 e
    matr4.append(self.matrixAPP(matr2))
    for i in range(steps-1):
        matr2 = np.dot(matr2,matr1)
        matr4.append(self.matrixAPP(matr2))
        
    MatrixA = []
    for i in range(len(matr1)):
        MatrixA.append(matr1[i][i])
    MatrixA = np.array(MatrixA) 
    MatrixB = self.matrixAPP(MatrixA)
    MatrixC = self.matrixAPP(MatrixA)
    MatrixF = []
    MatrixF.append(self.matrixAPP(MatrixB))

    for l in range(1, steps):
        for j in range(len(matr1)):
            #print (matr4)
            MatrixC[j] = matr4[l][j][j]
            for m in range(l):
                MatrixC[j] -= MatrixF[m][j]*matr4[l-m-1][j][j]
            MatrixB[j] = MatrixC[j]
        MatrixF.append(self.matrixAPP(MatrixB))
    for i in range(len(matr1)):
      for j in range(len(MatrixF)):
        matr3[i] += MatrixF[j][i]*(j+1)
    print(matr3[5])


  def task_9(self, matr1):
    matr1 = np.transpose(matr1)
    MatrixA = []
    for i in range(len(matr1)):
        MatrixA.append([])
        for j in range(len(matr1)):
            if (i==j):
                MatrixA[i].append(1)
            else:
                MatrixA[i].append(0)
    MatrixA = np.array(MatrixA)
    matr1 = matr1 - MatrixA
    matr1[-1] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    matr1 = np.linalg.inv(matr1)
    matr1 = np.dot(matr1,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]) #матрица B задана в условии 5.2
    print(matr1)


  def task_A(self, Max_SZ, Chanel,Matriza,lambd , Tense ):
    for i in range(Max_SZ+Chanel+1):#lines
        for j in range(Max_SZ+Chanel+1):#columns
            if i == j - 1:
                Matriza[i][j] = lambd
            elif j == i-1:
                Matriza[i][j] = Tense*(i-(i-Chanel)*(i>Chanel))


    MATR=[] #matrics

    for i in Matriza:
        MATR.append(list(i))
    print('Матрица интенсивностей', MATR)
    return Matriza


  def task_BC(self, Some_Matrix_2, lambd):
    Matr_otkaz = Some_Matrix_2[-1] #p_otkas
    obs = 1 - Matr_otkaz #int_obs
    obsAndAbs = obs * lambd #obs abs
    return Matr_otkaz,obs,obsAndAbs


  def task_D(self, Max_SZ, Some_Matrix_2, Chanel):
    Matr_queue_M = 0 #l_queue
    for i in range(1, Max_SZ+1):
      Matr_queue_M += i * Some_Matrix_2[Chanel+i]
    return Matr_queue_M

  def task_E(self, Max_SZ,Chanel, Tense,Some_Matrix_2  ):
    Matr_queue = 0 # t_queue
    for i in range(0,Max_SZ):
      Matr_queue += ((i+1)/(Chanel*Tense)) * Some_Matrix_2[Chanel+i]
    return Matr_queue


  def task_F(self, Chanel, Some_Matrix_2, Max_SZ):
    Num_Chan = 0 # n_canalov
    for i in range(1, Chanel+1):
        Num_Chan+= i*Some_Matrix_2[i]
    for i in range(Chanel+1, Chanel+Max_SZ+1):
        Num_Chan+= Chanel*Some_Matrix_2[i]
    return Num_Chan


  def task_G(self, Some_Matrix_2, Chanel):
    Mat_not_queue = 0 # p not queye
    for i in range(Chanel):
        Mat_not_queue += Some_Matrix_2[i]
    return Mat_not_queue

  def task_H(self, matr1, matr2):
    print("now")


  def task_I(self, matr1, matr2):
    print("now")
  

  def Make_Some_Matrix(self, Matriza):
    Matriza_2 = np.zeros((Max_SZ+Chanel+1, Max_SZ+Chanel+1))  # D
    for i in range(Max_SZ+Chanel+1):
        Matriza_2[i][i] = np.sum(Matriza[i])

    Matriza_TRANS = Matriza.transpose()
    Some_Matrix = Matriza_TRANS - Matriza_2 # M
    Some_Matrix[-1] = np.ones((Max_SZ+Chanel+1))
    Some_Matrix_2 = np.linalg.inv(Some_Matrix) # M1

    Matriza = np.zeros((Max_SZ+Chanel+1)) # B
    Matriza[-1] = 1

    Some_Matrix_2 = Some_Matrix_2.dot(Matriza)
    return Some_Matrix_2


  def Desintegrate(self,h,n,v): #integrate
      k=np.zeros((n*4))
      arg=np.zeros((n))

      for i in range(0,n):
          k[i*4]=self.proizvod(v)[i]
          arg[i]=v[i]+h*k[i*4]/2
      
      for i in range(0,n):
          k[i*4+1]=self.proizvod(arg)[i]
          arg[i]=v[i]+h*k[i*4+1]/2
          
      for i in range(0,n):
          k[i*4+2]=self.proizvod(arg)[i]
          arg[i]=v[i]+h*k[i*4+2]        
          
      for i in range(0,n):
          k[i*4+3]=self.proizvod(arg)[i]

      result=np.zeros(n)   
      for i in range(0,n):
          result[i]=v[i]+h*(k[i*4]+2*k[i*4+1]+2*k[i*4+2]+k[i*4+3])/6

      return result
  
  
  def proizvod(self,v): #f
    y=np.zeros((len(v)))
    y[0]=1 #производная времени
    y[1]=v[2]*Tense - v[1]*lambd #производная вероятность нулевого состояния
    y[2]=v[1]*lambd+v[3]*2*Tense - v[2]*(lambd+Tense) #производная вероятность первого состояния
    y[3]=v[2]*lambd+v[4]*3*Tense - v[3]*(lambd+(2*Tense)) #производная вероятность второго состояния
    y[4]=v[3]*lambd+v[5]*4*Tense - v[4]*(lambd+(3*Tense)) #производная вероятность третьего состояния
    y[5]=v[4]*lambd+v[6]*5*Tense - v[5]*(lambd+(4*Tense)) #производная вероятность четвертого состояния
    y[6]=v[5]*lambd - v[6]*(lambd+(5*Tense)) #производная вероятность пятого состояния
    y[7]=v[6]*lambd #производная вероятность шестого состояния
    y[8] = v[0]*v[6]*lambd #интеграл времени
    return y





# АТР класса
Mat=MatModel()

"""

# Задание 1
print ("Система имеем 16 дискретных состояний. Изменение состояний происходит в дискретные моменты времени с заданной вероятность. Схема марковского процесса изображена на рисунке. Требуется определить:\nВероятность того, что за 5 шагов система перейдет из состояния 13 в состояние 7")

# вероятность того, что за 5 шагов система перейдет из состояния 13 в состояние 7;
steps = 4 # k
stat1 = 12 #i
stat2 =6 # j


# Схема марковского процесса, которая была на рисунке, сейчас находится ниже
# sample
matr = np.array([[0.28	,0.48,	0,	0,	0.13,	0.11,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
[0,	0.22,	0	,0,	0.55,	0,	0.23,	0,	0,	0,	0,	0,	0,	0,	0,	0],
[0,	0.17,	0.06,	0,	0.46,	0,	0.31,	0,	0,	0,	0,	0,	0,	0,	0,	0],
[0,	0,	0,	0.21,	0,	0.39,	0.4,	0,	0,	0,	0,	0,	0,	0,	0,	0],
[0.41,	0	,0.19,	0,	0.08,	0.13	,0	,0.08	,0	,0.11	,0	,0	,0	,0	,0	,0],
[0	,0.03	,0	,0.15	,0.35	,0.05	,0	,0	,0.26	,0	,0.16	,0	,0	,0	,0,	0],
[0	,0	,0	,0	,0	,0.42	,0.58	,0	,0	,0	,0	,0	,0	,0	,0	,0],
[0,	0,	0,	0,	0,	0,	0.01,	0.03,	0.22,	0,	0,	0.21,	0.2,	0,	0,	0.33],
[0	,0	,0	,0	,0	,0	,0.13,	0.29,	0.28,	0.3	,0	,0	,0	,0	,0	,0],
[0,	0,	0,	0,	0.16,	0.07,	0.04,	0,	0.17,	0.12,	0.09,	0.17,	0.06,	0.11,	0.01,	0],
[0,	0,	0,	0,	0,	0,	0.24,	0	,0,	0,	0.27,	0.16,	0,	0.17,	0.01,	0.15],
[0	,0	,0,	0	,0	,0	,0	,0	,0	,0	,0	,0.12	,0.88	,0	,0	,0],
[0,	0,	0,	0,	0,	0,	0,	0.32,	0	,0.6	,0,	0.01,	0.07,	0,	0,	0],
[0	,0	,0	,0	,0	,0	,0	,0	,0.1,	0.18	,0.23	,0	,0.18	,0.31	,0	,0],
[0,	0,	0,	0	,0	,0	,0,	0,	0	,0	,0.53,	0,	0,	0.39,	0.08,	0],
[0	,0	,0	,0	,0	,0	,0	,0	,0	,0.33	,0	,0	,0	,0,	0.2	,0.47]])

#a
matr1=np.copy(matr)
#b
matr2 =np.copy(matr) # копируем матрицу для дальнейших действий с ней
   
Mat.task_1(matr1, matr2 , steps, stat1, stat2)

print ("\nвероятности состояний системы спустя 6 шагов, если в начальный момент вероятность состояний были следующими A=(0,05;0,05;0;0,09;0,11;0,1;0,14;0,06;0,08;0,03;0,07;0,01;0,09;0,07;0,01;0,04);\n")

matr1=np.copy(matr)
matr2 =np.copy(matr)

A=(0.05,0.05,0,0.09,0.11,0.1,0.14,0.06,0.08,0.03,0.07,0.01,0.09,0.07,0.01,0.04) 

#возможно 
#steps=5

Mat.task_2(matr1,matr2,steps,A)


print ("\nвероятность первого перехода за 9 шагов из состояния 11 в состояние 8;\n")
steps=9
stat1=10
stat2=7

matr1=np.copy(matr)
matr2=np.copy(matr)
matr3=np.copy(matr)


Mat.task_3(matr1, matr2,matr3, steps,stat1,stat2)



print ("\nвероятность перехода из состояния 11 в состояние 6 не позднее чем за 8 шагов;\n")

steps=8
stat1=10
stat2=5

matr1=np.copy(matr)
matr2=np.copy(matr)
matr3=np.copy(matr)
matr4=np.copy(matr)


Mat.task_4(matr1, matr2,matr3,matr4, steps, stat1,stat2)



print ("\nсреднее количество шагов для перехода из состояния 15 в состояние 13;\n")


medSTEPS = time.time()
steps=2000
stat1=14
stat2=12

matr1=np.copy(matr)
matr2=np.copy(matr)
matr3=np.copy(matr)
matr4=[]
matr5=[]


Mat.task_5(matr1, matr2,matr3, matr4, matr5, steps,stat1,stat2)



print ("\nвероятность первого возвращения в состояние 16 за 7 шагов;\n")


steps=7
stat1=15
#stat2=15 #we kinda dont need it cause we have the same up

matr1=np.copy(matr)
matr2=np.copy(matr)
matr1=np.array(matr1)
matr2=np.array(matr2)



Mat.task_6(matr1, matr2,steps,stat1)



print ("\nвероятность возвращения в состояние 8 не позднее чем за 9 шагов;\n")
steps=9
stat1=7
#stat2=7 #we kinda dont need it cause we have the same up
 
matr1=np.copy(matr)
matr2=np.copy(matr)
matr3=np.copy(matr)
matr4=np.copy(matr)



Mat.task_7(matr1, matr2,matr3,matr4,steps,stat1)



print ("\nсреднее время возвращения в состояние 9;\n")
steps=1000
matr1=np.copy(matr)
matr2=np.copy(matr)

matr3 = np.zeros((16)) # e
matr4 = [] # d


Mat.task_8(matr1, matr2,matr3,matr4,steps)


print ("\nустановившиеся вероятности. \n")

matr1=np.copy(matr)

Mat.task_9(matr1)


"""



print("\n\nЗадание 2\nЗадана система массового обслуживания со следующими характеристиками:\nЗадана система массового обслуживания со следующими характеристиками:\nинтенсивность поступления\nλ=36\nканалов обслуживания\nm=6\nинтенсивность обслуживания\nμ=8\nмаксимальный размер очереди\nn=7\nИзначально требований в системе нет.\n\nСоставьте граф марковского процесса, запишите систему уравнений Колмогорова и найдите установившиеся вероятности состояний.")


lambd = 36  #l
Chanel =  6 # m
Tense = 8 #my
Max_SZ = 7 #n

Matriza = np.zeros((Max_SZ+Chanel+1, Max_SZ+Chanel+1)) # P
#devide by two parts
# for i in range(Max_SZ+Chanel+1):#lines
#     for j in range(Max_SZ+Chanel+1):#columns
#         if i == j - 1:
#             Matriza[i][j] = lambd
#         elif j == i-1:
#             Matriza[i][j] = Tense*(i-(i-Chanel)*(i>Chanel))


# MATR=[] #matrics

# for i in Matriza:
#     MATR.append(list(i))
# print('Матрица интенсивностей', MATR)

Matriza=Mat.task_A(Max_SZ, Chanel,Matriza,lambd ,Tense)


###
# Matriza_2 = np.zeros((Max_SZ+Chanel+1, Max_SZ+Chanel+1))  # D
# for i in range(Max_SZ+Chanel+1):
#     Matriza_2[i][i] = np.sum(Matriza[i])

# Matriza_TRANS = Matriza.transpose()
# Some_Matrix = Matriza_TRANS - Matriza_2 # M
# Some_Matrix[-1] = np.ones((Max_SZ+Chanel+1))
# Some_Matrix_2 = np.linalg.inv(Some_Matrix) # M1

# Matriza = np.zeros((Max_SZ+Chanel+1)) # B
# Matriza[-1] = 1

# Some_Matrix_2 = Some_Matrix_2.dot(Matriza)
###


Some_Matrix_2=Mat.Make_Some_Matrix(Matriza) # M1


# Matr_otkaz = Some_Matrix_2[-1] #p_otkas
# obs = 1 - Matr_otkaz #int_obs
# obsAndAbs = obs * lambd #obs abs

Matr_otkaz,obs,obsAndAbs=Mat.task_BC(Some_Matrix_2, lambd) #P otkaz, int obs , obs abs


# Matr_queue_M = 0 #l_queue
# for i in range(1, Max_SZ+1):
#     Matr_queue_M += i * Some_Matrix_2[Chanel+i]

Matr_queue_M=Mat.task_D( Max_SZ, Some_Matrix_2, Chanel)

    
# Matr_queue = 0 # t_queue
# for i in range(0,Max_SZ):
#     Matr_queue += ((i+1)/(Chanel*Tense)) * Some_Matrix_2[Chanel+i]

Matr_queue=Mat.task_E( Max_SZ,Chanel, Tense,Some_Matrix_2  )


# Num_Chan = 0 # n_canalov
# for i in range(1, Chanel+1):
#     Num_Chan+= i*Some_Matrix_2[i]
# for i in range(Chanel+1, Chanel+Max_SZ+1):
#     Num_Chan+= Chanel*Some_Matrix_2[i]

Num_Chan=Mat.task_F( Chanel, Some_Matrix_2, Max_SZ)


# Mat_not_queue = 0 # p not queye
# for i in range(Chanel):
#     Mat_not_queue += Some_Matrix_2[i]

Mat_not_queue=Mat.task_G( Some_Matrix_2, Chanel)

Stoi = 1 / lambd

print('Вероятность отказа', Matr_otkaz)
print('Интенсивность обслуживания',obs)
print('Абсолютная интенсивность обслуживания',obsAndAbs)
print('Средняя длина очереди', Matr_queue_M)
print('Среднее время в очереди', Matr_queue)
print('Среднее количество занятых каналов', Num_Chan)
print('Вероятность, что заявка не окажется в очереди', Mat_not_queue)
print('Среднее время простоя системы', Stoi)

def rescale(x0, s1):
    s2 = 1
    x0 = s2*x0/s1
    return x0


s1 = 0
for i in range(6):
    s1 += Some_Matrix_2[i]
X1 = []   
for i in range(6):
    X1.append(rescale(Some_Matrix_2[i], s1))

x=np.zeros((1))
x[0]=0
p0 = np.zeros((1))
p1 = np.zeros((1))
p2 = np.zeros((1))
p3 = np.zeros((1))
p4 = np.zeros((1))
p5 = np.zeros((1))
p6 = np.zeros((1))
p0[0] = X1[0]
p1[0] = X1[1]
p2[0] = X1[2]
p3[0] = X1[3]
p4[0] = X1[4]
p5[0] = X1[5]
p6[0] = 0
sr=np.zeros((1))
sr[0] = p5[0]*lambd
t_sr=np.zeros((1))
t_sr[0] = 0

h=0.001

v=np.zeros(9)
v[0]=0 #time
v[1]=X1[0] #zero sst time
v[2]=X1[1] #first sst time
v[3]=X1[2] #second sst time
v[4]=X1[3] #third sst time
v[5]=X1[4] #fourth sst time
v[6]=X1[5] #fifth sst time
v[7]=0 #sixth sst time
v[8]=0 #integral of sst time

for t in range(1,20000):
    v=Mat.Desintegrate(h,9,v)
    x=np.append(x,v[0]) 
    p0=np.append(p0,v[1])
    p1=np.append(p1,v[2])
    p2=np.append(p2,v[3])
    p3=np.append(p3,v[4])
    p4=np.append(p4,v[5])
    p5=np.append(p5,v[6])
    p6=np.append(p6,v[7])
    sr=np.append(sr, v[6] * lambd)
    t_sr_faf=np.append(t_sr, v[8])

print("среднее время, когда в системе нет очереди.: ", t_sr_faf[-1])


#  b)     Ответ: 0.10514804845222071
# c)	Найдите относительную и абсолютную интенсивность обслуживания.
# 0.8948519515477793 (относительная)
# 4.4742597577388965 (абсолютная)
# d)	Найдите среднюю длину в очереди.
# 2.208109017496635
# e)	Найдите среднее время в очереди.
# 0.44162180349932706
# f)	Найдите среднее число занятых каналов.
# 4.4742597577388965
# g)	Найдите вероятность того, что поступающая заявка не будет ждать в очереди.
# 0.263963660834455
# h)	Найти среднее время простоя системы массового обслуживания.
# 0.2
# i)	Найти среднее время, когда в системе нет очереди.
# 1.2998092622058512
