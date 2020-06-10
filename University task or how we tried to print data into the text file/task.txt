#Разработать программное средство с использованием ООП для
#представления успеваемости студентов по дисциплине: 
#1)
#Промежуточная аттестация максимум 20 баллов, разбитые
#по количеству работ (практики, контрольная и тестирование в 1
#половине семестра);
#2)
#Работа в семестре 20 баллов (практики, контрольная и
#тестирование во 2 половине семестра);
#3)
#Экзамен 60 баллов;
#4)
#Выставление итоговой оценки.
#Объект класса должен содержать поля для сохранения имени
#студента и истории получения баллов (по практикам, контрольным и
#тестированиям) с учетом даты получения оценки по схеме: выполнено,
#защищено.

import first

class university:
  def promeznost (self,score):
    self.score=score
    promofor=first.practise()
    score=score+promofor[1]
    return score,promofor
  
  def rabotaisemen(self,score):
    self.score=score
    promofor=first.rabota()
    score=score+promofor[1]
    return score,promofor
  
  def exam (self):
    score=int(input("сколько баллов он получили за экзамен ?\n"))
    if score > 60:
      score=60
    import datetime
    lala=[]
    a=input("введите дату выполнения через пробел. Сначала вводится год , потом месяц, а потом день\n").split(" ")
    for i in range (len(a)):
      a[i]=int(a[i])
      lala.append(a[i])
    if lala[0]<2000 or lala[1]>12 or lala[2]>31 :
      return self.exam ()
    sdacha=datetime.datetime(lala[0],lala[1],lala[2])
    garik=str(score)
    sdacha=str(sdacha)
    result="За экзамен получено баллов - "+garik+" сдан экзамен был в эту дату - "+sdacha+" | "
    return result,score

choice=int(input ("Здравствуйте ! Вас приветствует программа успеваемости студентов. Для того , чтобы ввести N-ное число студентов и инфу к ним введите - 1, чтобы узнать инфу о других студентах - 2 \n"))
if choice==2:
  print ("Михалков|Пи19-1|выполнил 01-09-1939|защитил 3 - 08.05.1945|контрольная 3 - 10.05.2008|самостоятельная 5 - 11.06.2001|экзамен 50 - 11.09.2201|\nГаврилов|Пи19-1|выполнил 01-09-1939|защитил 5 - 08.05.1945|контрольная 10 - 10.05.2008|самостоятельная 2 - 11.06.2001|экзамен 50 - 11.09.2201|\nГагарин|Пи1990-10|выполнил 01-09-1920|защитил 69 - 08.05.1961|контрольная 0 - 10.05.2008|самостоятельная 7 - 11.06.2001|экзамен 20 - 11.09.2201|\nПутин|Пи2-1|выполнил 01-10-1910|защитил 10 - 20.12.1920|контрольная 3 - 10.05.2008|самостоятельная 5 - 11.06.2001|экзамен 50 - 11.09.2201|\nРамзан|Пи18-2|выполнил 01-09-1939|защитил 3 - 08.05.1945|контрольная 20 - 10.05.1991|самостоятельная 2 - 11.06.2001|экзамен 59 - 11.09.2201|\nМакс|Пи19-9|выполнил 02-11-2021|защитил 0 - 08.05.2022|контрольная 3 - 10.05.2008|самостоятельная 5 - 11.06.2001|экзамен 50 - 11.09.2201|\n")
elif choice==1:
  cccount=int(input("сколько будет учеников ?\n"))
  for i in range (cccount):
    score=0
    name=str(input("как зовут ученика ?\n"))
    group=str(input("в какой группе он находится ?\n"))
    discipline=str(input("какой предмет у ученика ?\n"))
    raka=university()
    asd=raka.exam()
    score=score+asd[1]
    jaka=university()
    ass=jaka.promeznost(score)
    score=score+ass[0]
    maka=university()
    ak=maka.rabotaisemen(score)
    score=score+ak[0]
    score=str(score)
    i="номер ученика - "+str(i)+" | "
    name="его\ее зовут -"+name+" | "
    group="учится в "+group+" | "
    discipline="предмет - "+discipline+" | "
    result=""
    lkj=str(ak[1])
    poi=str(ass[1])
    mnb=str(asd[0])
    result=i+result+name+group+discipline+mnb+poi+lkj
    f=open("text.txt","w")
    f.write(result)
    f.close()
  
  print ("сейчас откроем файл и посмотрим, что мы туда записали\n")
  f=open("text.txt","r")
  for line in f:
    print (line)
else :
  exit()

  
