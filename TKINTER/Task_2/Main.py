import math
from plotly import offline
import plotly.graph_objects as go


x=int(input("Введи 1, если хочешь выбрать опцию -sqrt из 3 \nВведи 2, если хочешь выбрать опцию -1 \nВведи 3, если хочешь выбрать опцию -(sqrt из 3) / 3 \nВведи 4, если хочешь выбрать опцию 0\nВведи 5, если хочешь выбрать опцию (sqrt из 3) / 3 \nВведи 6, если хочешь выбрать опцию 1 \nВведи 7, если хочешь выбрать опцию sqrt из 3\n\n"))
y=int(input("Введите размер ряда \tу нас, к сожалению, нет бесконечных мощностей, чтобы вычислять это бесконечно, поэтому ограничимся этими пределами\n\n"))

if x==1.0 or x==1:
  xrow = []
  yrow = []

  start=-math.sqrt(3)
  nu=3
  number=start
  for i in range (y):
    xrow.append(number)
    #xrow.append(number)
    yrow.append(nu)
    #yrow.append(-nu)

    k=(start**nu)/nu
    
    if i==0:
      number-=k
    
    elif i%2!=0:
      number+=k
    
    elif i%2==0:
      number-=k
    
    else:
      exit(0)

    nu+=2


elif x==2.0 or x==2:
  xrow = []
  yrow = []

  start=-1
  nu=3
  number=start
  for i in range (y):
    xrow.append(number)
    xrow.append(number)
    yrow.append(nu)
    yrow.append(-nu)

    k=(start**nu)/nu
    
    if i==0:
      number-=k
    
    elif i%2!=0:
      number+=k
    
    elif i%2==0:
      number-=k
    
    else:
      exit(0)

    nu+=2


elif x==3.0 or x==3:
  xrow = []
  yrow = []

  start=-(math.sqrt(3)/3)
  nu=3
  number=start
  for i in range (y):
    xrow.append(number)
    xrow.append(number)
    yrow.append(nu)
    yrow.append(-nu)

    k=(start**nu)/nu
    
    if i==0:
      number-=k
    
    elif i%2!=0:
      number+=k
    
    elif i%2==0:
      number-=k
    
    else:
      exit(0)

    nu+=2


elif x==4.0 or x==4:
  xrow = []
  yrow = []

  start=0
  nu=3
  number=start
  for i in range (y):
    xrow.append(number)
    xrow.append(number)
    yrow.append(nu)
    yrow.append(-nu)

    k=(start**nu)/nu
    
    if i==0:
      number-=k
    
    elif i%2!=0:
      number+=k
    
    elif i%2==0:
      number-=k
    
    else:
      exit(0)

    nu+=2


elif x==5.0 or x==5:
  xrow = []
  yrow = []

  start=math.sqrt(3)/3
  nu=3
  number=start
  for i in range (y):
    xrow.append(number)
    xrow.append(number)
    yrow.append(nu)
    yrow.append(-nu)

    k=(start**nu)/nu
    
    if i==0:
      number-=k
    
    elif i%2!=0:
      number+=k
    
    elif i%2==0:
      number-=k
    
    else:
      exit(0)

    nu+=2


elif x==6.0 or x==6:
  xrow = []
  yrow = []

  start=1
  nu=3
  number=start
  for i in range (y):
    xrow.append(number)
    xrow.append(number)
    yrow.append(nu)
    yrow.append(-nu)

    k=(start**nu)/nu
    
    if i==0:
      number-=k
    
    elif i%2!=0:
      number+=k
    
    elif i%2==0:
      number-=k
    
    else:
      exit(0)

    nu+=2


elif x==7.0 or x==7:
  xrow = []
  yrow = []

  start=math.sqrt(3)
  nu=3
  number=start
  for i in range (y):
    xrow.append(number)
    xrow.append(number)
    yrow.append(nu)
    yrow.append(-nu)

    k=(start**nu)/nu
    
    if i==0:
      number-=k
    
    elif i%2!=0:
      number+=k
    
    elif i%2==0:
      number-=k
    
    else:
      exit(0)

    nu+=2

fig = go.Figure()
fig.add_trace(go.Scatter(x=xrow, y=yrow,
                    mode='lines',
                    name='lines'))
offline.plot(fig , filename="task.html")
fig.show()
