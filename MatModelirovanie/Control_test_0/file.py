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


  def task_A(self, matr1, matr2):
    print("now")


  def task_B(self, matr1, matr2):
    print("now")

  def task_C(self, matr1, matr2):
    print("now")


  def task_D(self, matr1, matr2):
    print("now")

  def task_E(self, matr1, matr2):
    print("now")


  def task_F(self, matr1, matr2):
    print("now")


  def task_G(self, matr1, matr2):
    print("now")


  def task_H(self, matr1, matr2):
    print("now")


  def task_I(self, matr1, matr2):
    print("now")





# АТР класса
Mat=MatModel()

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
