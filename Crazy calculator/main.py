
import re
import math

def split_text(any_text):
    '''
    Функция для вычленения 2-х уравнений из строки файла
    '''
    result = re.split(r"[\[\]\']", any_text)
    return (result[2],result[4])
    
def deсision_4(a,b,c):
    '''
    Функция решения биквадратного уравнения
    '''
    D = b**2-4*a*c #Как для квадратного 
    if D < 0:
        return('нет корней')
    elif D == 0:
        y = (-b)/(2*a) # формула если корень один
        x1 = y**0.5 # Возводим в степень 1/2 т.е это корень 
        x2 = -(y**0.5) # Возводим в степень 1/2 т.е это корень 
        return [x1, x2]
    else:
        y1 = ((-b)+D**0.5)/(2*a) # Нашли первый корень при замене x^4 на y^2
        y2 = ((-b)-D**0.5)/(2*a)  # Нашли первый корень при замене x^4 на y^2
        x1 = y1**0.5 # Находим уже основные корни уравнения 
        x2 = -(y1**0.5)
        x3 = y2**0.5
        x4 = -(y2**0.5)
        return [x1, x2, x3, x4]


def arch(x):
    return (math.log(x+((x**2)-1)**0.5)).real
    
def ch(x):
    return ((math.exp(x)+math.exp(-x))/2).real

def deсision_3(a,b,c):
    '''
    Функция решения кубического уравнения
    '''
    q = (a**2-3*b)/9 # q = c + 2a^3/27-ab/3
    r =(2*(a**3)-9*a*b+27*c)/54
    s = q**3-r**2
    if s > 0:
        f = (math.acos(r/(q**1.5)))/3
        y1 = (-2)*(q**0.5)*(math.cos(f))-(a/3)
        y2 = (-2)*(q**0.5)*(math.cos(f+(2*math.pi/3)))-(a/3)
        y3 = (-2)*(q**0.5)*(math.cos(f-(2*math.pi/3)))-(a/3)
        return [y1, y2, y3]
    elif s < 0:
        f = arch(math.fabs(r)/(math.fabs(q))**(1.5))/3
        if r < 0:
            return (2*((math.fabs(q))**0.5)*ch(f))-(a/3)
        else:
            return ((-2)*((math.fabs(q))**0.5)*ch(f))-(a/3)
    elif s == 0:
        y1 = (-2)*(r**(1/3))-(a/3)
        y2 = (r**(1/3))-(a/3)
        if y1 == y2:
            return y1
        else:
            return [y1, y2]

def deсision_2(a,b,c):
    '''
    Функция решения квадратного уравнения
    '''
    discr = (b**2) - (4*a*c)
    print("Дискриминант D = %.2f" % discr) 
    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
    elif discr == 0:
        x1 = -b / (2 * a)
        print("x1 = %.2f" % x1)
        x2 = -0
    else:
        print("Корней нет")
        x1 = -0
        x2 = -0
    return (x1,x2)

def npdeсision_linear(ax,by,e,cx,dy,f):
    '''
    Функция решения линейного уравнения с помощью библиотеки numpy
    '''
    import numpy # импортируем библиотеку 
    a = numpy.array([[ax, by], [cx, dy]]) # Матрица (левая часть системы)
    b = numpy.array([e, f]) # Вектор (правая часть системы)
    x,y = numpy.linalg.solve(a, b)
    print("Корни уравнения: %.2f " %x,y)
    return (x,y)

def simple_deсision_linear(ax,by,e,cx,dy,f):
    '''
    Функция решения линейного уравнения простым способом
    '''
    x = 0
    y = 0
#Входные коэффициенты: ax, by, cx, dy, e, f. Решите систему линейных уравнений
#ax + by = e
#cx + dy = f
#Формат ввода
#Вводятся 6 чисел ax, by, cx, dy, e, f- коэффициенты уравнений.
#Формат вывода
#Вывод программы зависит от вида решения этой системы.
#Если система не имеет решений, то программа должна вывести единственное число 0.
#Если система имеет единственное решение , то (x₀,y₀) 
#Если система имеет бесконечно много решений вида x=x₀, y — любое, то значение x₀.
#Если система имеет бесконечно много решений вида y=y₀, x — любое, то значение y₀.
#Если любая пара чисел (x,y) является решением, то программа должна вывести число x,y
    if ax == 0 and by == 0 and cx == 0 and dy == 0 and e == 0 and f == 0:
        print('любая пара чисел (x,y) является решением')
        x = 0.000001 ; y = 0.000001
    elif ax * dy == by * cx and ax * f != cx * e:
        print('система не имеет решений')
        x = 0E2 ; y = 0E2
    elif ax == 0 and by == 0 and e != 0:
        print('система не имеет решений')
        x = 0E2 ; y = 0E2
    elif cx == 0 and dy == 0 and f != 0:
        print('система не имеет решений')
        x = 0E2 ; y = 0E2
    elif ax == 0 and cx == 0 and (by * f) != (dy * e):
        print('система не имеет решений')
        x = 0E2 ; y = 0E2
    elif by == 0 and dy == 0 and (ax * f) != (cx * e):
        print('система не имеет решений')
        x = 0E2 ; y = 0E2
    elif (ax * dy) == (by * cx) and (ax * f) == (cx * e):
        if by == 0 and dy == 0:
            if ax != 0 and cx != 0:
                print('система имеет бесконечно много решений: y-любое, x=', e / ax)
                x = e / ax ; y = 0.000001
            elif ax == 0:
                if e == 0:
                    print('система имеет бесконечно много решений: y-любое, x=', f / cx)
                    x = f / cx ;  y = 0.000001
            elif cx == 0:
                if f == 0:
                    print('система имеет бесконечно много решений: y-любое, x=', e / ax)
                    x = e / ax ;  y = 0.000001
        elif ax == 0 and cx == 0:
            if by != 0:
                print('система имеет бесконечно много решений: x-любое, y=', e / by)
                x = 0.000001 ; y = e / by
            elif dy != 0:
                print('система имеет бесконечно много решений: x-любое, y=', f / dy)
                x = 0.000001 ; y = f / dy
        elif by != 0:
            print('система имеет бесконечно много решений, каждое из которых имеет вид y=px+q: p={p} q={q} '.format (p = -ax / by, q = e / by))
            x = 0E2 ; y = 0E2
        elif dy != 0:
            print('система имеет бесконечно много решений, каждое из которых имеет вид y=px+q: p={p} q={q} '.format (p= -cx / dy, q = f / dy))
            x = 0E2 ; y = 0E2
    else:
        x = (e * dy - by * f) / (ax * dy - by * cx) ; y = (ax * f - e * cx) / (ax * dy - by * cx)
        print('система имеет единственное решение (x₀,y₀)', x, y)
    return (x,y)

def calc_koeff_4(mnogochlen, current_var):
    '''
    Функция нахождение коэффициентов для би-квадратного уравнения
    '''
    s = mnogochlen.split()
    cur_var = current_var # Это входная рабочая переменная (x или y)
    # Инициализируем коэффициенты при x, y , c и их знаки
    zn_k4 = '+'   ; zn_k2 = '+'   ; zn_kc = '+'
    k4 = float(0) ; k2 = float(0) ; kc = float(0)
    
    for i in range(len(s)):
       # Сплитуем по текущей переменной (x,y)
       p = s[i].partition(cur_var)
       # Если коэффициент пристепени 4
       if p[2] == '^4' :
           # Обработка знака коэффициента
           if (s[i-1] == '0') or (s[i-1] not in ('-','+')):
               zn_k4 = '+'
           else:
               zn_k4 = s[i-1] 
           # Обработка тела коэффициента, если нет числа у X - число =1
           if p[0] == '':
               k4 = (float(zn_k4 + '1')) + k4
           else:
               # Обработка '+' у коэффициента к4
               pl = p[0].partition('+')
               if pl[1] == '+': 
                   if zn_k4 == '+':
                       if pl[2] == '':
                           k4 = float('1') + k4
                       else:
                           k4 = float(pl[2]) + k4
                   elif zn_k4 == '-': 
                       if pl[2] == '':
                           k4 = (-1 * float('1')) + k4
                       else:
                           k4 = (-1 * float(pl[2])) + k4                    
               else:
                    # Обработка '-' у коэффициента k4
                    mn = p[0].partition('-')
                    if mn[1] == '-':
                        if zn_k4 == '+':
                            # Минус на плюс = минус
                            zn_k4 = '-'
                            if mn[2] == '':
                                k4 = (float(zn_k4 + '1')) + k4
                            else:
                                k4 = (float(zn_k4 + mn[2])) + k4
                            # Минус на минус = плюс
                        elif zn_k4 == '-':
                            zn_k4 = '+'
                            if mn[2] == '':
                                k4 = (float(zn_k4 + '1')) + k4
                            else:
                                k4 = (float(zn_k4 + mn[2])) + k4                        
                    else:
                        # Итоговый коэффициент при степени ^4
                        k4 = float(zn_k4 + (p[0])) + k4
    
    # Если коэффициент при степени 2            
       elif  p[2] == '^2' :
           # Обработка знака коэффициента
           if (s[i-1] == '0') or (s[i-1] not in ('-','+')):
               zn_k2 = '+'
           else:
               zn_k2 = s[i-1] 
           # Обработка тела коэффициента, если нет коэфф. у (X|Y) - число =1
           if p[0] == '':
               k2 = (float(zn_k2 + '1')) + k2
           else:
               # Обработка '+' у коэффициента к4
               pl = p[0].partition('+')
               if pl[1] == '+': 
                   if zn_k2 == '+':
                       if pl[2] == '':
                           k2 = float('1') + k2
                       else:
                           k2 = float(pl[2]) + k2
                   elif zn_k2 == '-': 
                       if pl[2] == '':
                           k2 = (-1 * float('1')) + k2
                       else:
                           k2 = (-1 * float(pl[2])) + k2                    
               else:
                    # Обработка '-' у коэффициента k4
                    mn = p[0].partition('-')
                    if mn[1] == '-':
                        if zn_k2 == '+':
                            # Минус на плюс = минус
                            zn_k2 = '-'
                            if mn[2] == '':
                                k2 = (float(zn_k2 + '1')) + k2
                            else:
                                k2 = (float(zn_k2 + mn[2])) + k2
                            # Минус на минус = плюс
                        elif zn_k2 == '-':
                            zn_k2 = '+'
                            if mn[2] == '':
                                k2 = (float(zn_k2 + '1')) + k2
                            else:
                                k2 = (float(zn_k2 + mn[2])) + k2                       
                    else:
                        # Итоговый коэффициент при степени ^4
                        k2 = float(zn_k2 + (p[0])) + k2
    # Обработка свободных членов уравнения       
       elif (re.search(r'([\d+]*\.\d+$|\d+$|[\d+]*\.$)', p[0]) \
             and (p[1] != cur_var)):
    # Обработка знака коэффициента     
           if (s[i-1] == '0') or (s[i-1] not in ('-','+')):
               zn_kc = '+'
           else:
               zn_kc = s[i-1] 
           pl = p[0].partition('+')
           if pl[1] == '+':
               if zn_kc == '+':
                   if pl[2] == '':
                       kc = float('0') + kc
                   else:
                       kc = float(pl[2]) + kc
               elif zn_kc == '-':
                   if pl[2] == '':
                       kc = (-1 * float('1')) + kc
                   else:
                       kc = (-1 * float(pl[2])) + kc                    
           else:
               mn = p[0].partition('-')
               if mn[1] == '-':
                   if zn_kc == '+':
                       zn_kc = '-'
                       if mn[2] == '':
                           kc = (float(zn_kc + '1')) + kc
                       else:
                           kc = (float(zn_kc + mn[2])) + kc
                   elif zn_kc == '-':
                       zn_kc = '+'
                       if mn[2] == '':
                           kc = (float(zn_kc + '1')) + kc
                       else:
                           kc = (float(zn_kc + mn[2])) + kc                        
               else:
                   kc = float(zn_kc + (p[0])) + kc
    return(k4,k2,kc)

def calc_koeff_3(mnogochlen, current_var):
    '''
    Функция нахождение коэффициентов для кубического уравнения
    '''
    s = mnogochlen.split()
    cur_var = current_var # Это входная рабочая переменная
    # Инициализируем коэффициенты при x, y , c и их знаки
    zn_k3 = '+'   ; zn_k1 = '+'   ; zn_kc = '+'
    k3 = float(0) ; k1 = float(0) ; kc = float(0)
       
    for i in range(len(s)):
       # Сплитуем по текущей переменной (x|y)
       p = s[i].partition(cur_var)
       # Если коэффициент при степени 3
       if p[2] == '^3' :
           # Обработка знака коэффициента
           if (s[i-1] == '0') or (s[i-1] not in ('-','+')):
               zn_k3 = '+'
           else:
               zn_k3 = s[i-1] 
           # Обработка тела коэффициента, если нет коэфф. у (x|y) - число =1
           if p[0] == '':
               k3 = (float(zn_k3 + '1')) + k3
           else:
               # Обработка '+' у коэффициента к3
               pl = p[0].partition('+')
               if pl[1] == '+': 
                   if zn_k3 == '+':
                       if pl[2] == '':
                           k3 = float('1') + k3
                       else:
                           k3 = float(pl[2]) + k3
                   elif zn_k3 == '-': 
                       if pl[2] == '':
                           k3 = (-1 * float('1')) + k3
                       else:
                           k3 = (-1 * float(pl[2])) + k3                    
               else:
                    # Обработка '-' у коэффициента k3
                    mn = p[0].partition('-')
                    if mn[1] == '-':
                        if zn_k3 == '+':
                            # Минус на плюс = минус
                            zn_k3 = '-'
                            if mn[2] == '':
                                k3 = (float(zn_k3 + '1')) + k3
                            else:
                                k3 = (float(zn_k3 + mn[2])) + k3
                            # Минус на минус = плюс
                        elif zn_k3 == '-':
                            zn_k3 = '+'
                            if mn[2] == '':
                                k3 = (float(zn_k3 + '1')) + k3
                            else:
                                k3 = (float(zn_k3 + mn[2])) + k3                        
                    else:
                        # Итоговый коэффициент при степени ^3
                        k3 = float(zn_k3 + (p[0])) + k3
                        
    
    # Если коэффициент при степени 1            
       elif  (p[1] == cur_var and p[2] != '^3') :
           # Обработка знака коэффициента
           if (s[i-1] == '0') or (s[i-1] not in ('-','+')):
               zn_k1 = '+'
           else:
               zn_k1 = s[i-1] 
           # Обработка тела коэффициента, если нет коэфф. у (x|y) - число =1
           if p[0] == '':
               k1 = (float(zn_k1 + '1')) + k1
           else:
               # Обработка '+' у коэффициента к1
               pl = p[0].partition('+')
               if pl[1] == '+': 
                   if zn_k1 == '+':
                       if pl[2] == '':
                           k1 = float('1') + k1
                       else:
                           k1 = float(pl[2]) + k1
                   elif zn_k1 == '-': 
                       if pl[2] == '':
                           k1 = (-1 * float('1')) + k1
                       else:
                           k1 = (-1 * float(pl[2])) + k1                    
               else:
                    # Обработка '-' у коэффициента k1
                    mn = p[0].partition('-')
                    if mn[1] == '-':
                        if zn_k1 == '+':
                            # Минус на плюс = минус
                            zn_k1 = '-'
                            if mn[2] == '':
                                k1 = (float(zn_k1 + '1')) + k1
                            else:
                                k1 = (float(zn_k1 + mn[2])) + k1
                            # Минус на минус = плюс
                        elif zn_k1 == '-':
                            zn_k1 = '+'
                            if mn[2] == '':
                                k1 = (float(zn_k1 + '1')) + k1
                            else:
                                k1 = (float(zn_k1 + mn[2])) + k1                      
                    else:
                        # Итоговый коэффициент при степени ^1
                        k1 = float(zn_k1 + (p[0])) + k1
    # Обработка свободных членов уравнения       
       elif (re.search(r'([\d+]*\.\d+$|\d+$|[\d+]*\.$)', p[0]) \
             and (p[1] != cur_var)):
    # Обработка знака коэффициента     
           if (s[i-1] == '0') or (s[i-1] not in ('-','+')):
               zn_kc = '+'
           else:
               zn_kc = s[i-1] 
           pl = p[0].partition('+')
           if pl[1] == '+':
               if zn_kc == '+':
                   if pl[2] == '':
                       kc = float('0') + kc
                   else:
                       kc = float(pl[2]) + kc
               elif zn_kc == '-':
                   if pl[2] == '':
                       kc = (-1 * float('1')) + kc
                   else:
                       kc = (-1 * float(pl[2])) + kc                    
           else:
               mn = p[0].partition('-')
               if mn[1] == '-':
                   if zn_kc == '+':
                       zn_kc = '-'
                       if mn[2] == '':
                           kc = (float(zn_kc + '1')) + kc
                       else:
                           kc = (float(zn_kc + mn[2])) + kc
                   elif zn_kc == '-':
                       zn_kc = '+'
                       if mn[2] == '':
                           kc = (float(zn_kc + '1')) + kc
                       else:
                           kc = (float(zn_kc + mn[2])) + kc                        
               else:
                   kc = float(zn_kc + (p[0])) + kc
    return(k3,k1,kc)
               
def calc_koeff_2(mnogochlen, current_var):
    '''
    Функция нахождение коэффициентов для квадратного уравнения
    '''
    # s - список значений и знаков многочлена
    s = mnogochlen.split()
    cur_var = current_var # Это входная рабочая переменная
    
    # Инициализируем коэффициенты при x, y , c и их знаки
    zn_k2 = '+'   ; zn_k1 = '+'   ; zn_kc = '+'
    k2 = float(0) ; k1 = float(0) ; kc = float(0)
    # Цикл по списку s
    for i in range(len(s)):
       # Сплитуем по текущей переменной (x|y)
       p = s[i].partition(cur_var)
       # Если коэффициент пристепени 2
       if p[2] == '^2' :
           # Обработка знака коэффициента
           if (s[i-1] == '0') or (s[i-1] not in ('-','+')):
               zn_k2 = '+'
           else:
               zn_k2 = s[i-1] 
           # Обработка тела коэффициента, если нет коэфф. у (x|y) - число =1
           if p[0] == '':
               k2 = (float(zn_k2 + '1')) + k2
           else:
               # Обработка '+' у коэффициента к4
               pl = p[0].partition('+')
               if pl[1] == '+': 
                   if zn_k2 == '+':
                       if pl[2] == '':
                           k2 = float('1') + k2
                       else:
                           k2 = float(pl[2]) + k2
                   elif zn_k2 == '-': 
                       if pl[2] == '':
                           k2 = (-1 * float('1')) + k2
                       else:
                           k2 = (-1 * float(pl[2])) + k2                    
               else:
                    # Обработка '-' у коэффициента k2
                    mn = p[0].partition('-')
                    if mn[1] == '-':
                        if zn_k2 == '+':
                            # Минус на плюс = минус
                            zn_k2 = '-'
                            if mn[2] == '':
                                k2 = (float(zn_k2 + '1')) + k2
                            else:
                                k2 = (float(zn_k2 + mn[2])) + k2
                            # Минус на минус = плюс
                        elif zn_k2 == '-':
                            zn_k2 = '+'
                            if mn[2] == '':
                                k2 = (float(zn_k2 + '1')) + k2
                            else:
                                k2 = (float(zn_k2 + mn[2])) + k2                        
                    else:
                        # Итоговый коэффициент при степени ^2
                        k2 = float(zn_k2 + (p[0])) + k2
    
    # Если коэффициент при степени 1            
       elif  (p[1] == cur_var and p[2] != '^2') :
           # Обработка знака коэффициента
           if (s[i-1] == '0') or (s[i-1] not in ('-','+')):
               zn_k1 = '+'
           else:
               zn_k1 = s[i-1] 
           # Обработка тела коэффициента, если нет коэфф. у (x|y) - число =1
           if p[0] == '':
               k1 = (float(zn_k1 + '1')) + k1
           else:
               # Обработка '+' у коэффициента к1
               pl = p[0].partition('+')
               if pl[1] == '+': 
                   if zn_k1 == '+':
                       if pl[2] == '':
                           k1 = float('1') + k1
                       else:
                           k1 = float(pl[2]) + k1
                   elif zn_k1 == '-': 
                       if pl[2] == '':
                           k1 = (-1 * float('1')) + k1
                       else:
                           k1 = (-1 * float(pl[2])) + k1                    
               else:
                    # Обработка '-' у коэффициента k1
                    mn = p[0].partition('-')
                    if mn[1] == '-':
                        if zn_k1 == '+':
                            # Минус на плюс = минус
                            zn_k1 = '-'
                            if mn[2] == '':
                                k1 = (float(zn_k1 + '1')) + k1
                            else:
                                k1 = (float(zn_k1 + mn[2])) + k1
                            # Минус на минус = плюс
                        elif zn_k1 == '-':
                            zn_k1 = '+'
                            if mn[2] == '':
                                k1 = (float(zn_k1 + '1')) + k1
                            else:
                                k1 = (float(zn_k1 + mn[2])) + k1                      
                    else:
                        # Итоговый коэффициент при степени ^1
                        k1 = float(zn_k1 + (p[0])) + k1
    # Обработка свободных членов уравнения       
       elif (re.search(r'([\d+]*\.\d+$|\d+$|[\d+]*\.$)', p[0]) \
             and (p[1] != cur_var)):
    # Обработка знака коэффициента     
           if (s[i-1] == '0') or (s[i-1] not in ('-','+')):
               zn_kc = '+'
           else:
               zn_kc = s[i-1] 
           pl = p[0].partition('+')
           if pl[1] == '+':
               if zn_kc == '+':
                   if pl[2] == '':
                       kc = float('0') + kc
                   else:
                       kc = float(pl[2]) + kc
               elif zn_kc == '-':
                   if pl[2] == '':
                       kc = (-1 * float('1')) + kc
                   else:
                       kc = (-1 * float(pl[2])) + kc                    
           else:
               mn = p[0].partition('-')
               if mn[1] == '-':
                   if zn_kc == '+':
                       zn_kc = '-'
                       if mn[2] == '':
                           kc = (float(zn_kc + '1')) + kc
                       else:
                           kc = (float(zn_kc + mn[2])) + kc
                   elif zn_kc == '-':
                       zn_kc = '+'
                       if mn[2] == '':
                           kc = (float(zn_kc + '1')) + kc
                       else:
                           kc = (float(zn_kc + mn[2])) + kc                        
               else:
                   kc = float(zn_kc + (p[0])) + kc
    return(k2,k1,kc)

def calc_koeff(mnogochlen):
    '''
    Функция нахождение коэффициентов для линейного уравнения
    '''
    # s - список значений и знаков многочлена
    s = mnogochlen.split()
    # Инициализируем коэффициенты при x, y , c и их знаки, fl_rabn - признак перехода через '='
    zn_kx = '+'   ; zn_ky = '+'   ; zn_kc = '+';   fl_rabn = 'false'
    kx = float(0) ; ky = float(0) ; kc = float(0)
    #while 0 <= y < i:
    for i in range(len(s)):
       #print ('s[%s]=%s' %(i,s[i]))
       p = s[i].partition('x')
       if p[1] == 'x' :
           # Обработка знака коэффициента
           if (s[i-1] == '0') or (s[i-1] not in ('-','+')):
               zn_kx = '+'
           else:
               zn_kx = s[i-1] 
           # Обработка тела коэффициента, если нет числа у X - число =1
           if p[0] == '':
               kx = (float(zn_kx + '1')) + kx
           else:
               # Обработка '+' у коэффициента к
               pl = p[0].partition('+')
               if pl[1] == '+': 
                   if zn_kx == '+':
                       if pl[2] == '':
                           kx = float('1') + kx
                       else:
                           kx = float(pl[2]) + kx
                   elif zn_kx == '-': 
                       if pl[2] == '':
                           kx = (-1 * float('1')) + kx
                       else:
                           kx = (-1 * float(pl[2])) + kx                    
               else:
                    # Обработка '-' у коэффициента x
                    mn = p[0].partition('-')
                    if mn[1] == '-':
                        if zn_kx == '+':
                            # Минус на плюс = минус
                            zn_kx = '-'
                            if mn[2] == '':
                                kx = (float(zn_kx + '1')) + kx
                            else:
                                kx = (float(zn_kx + mn[2])) + kx
                            # Минус на минус = плюс
                        elif zn_kx == '-':
                            zn_kx = '+'
                            if mn[2] == '':
                                kx = (float(zn_kx + '1')) + kx
                            else:
                                kx = (float(zn_kx + mn[2])) + kx                        
                    else:
                        # Итоговое число при X
                        kx = float(zn_kx + (p[0])) + kx
                        #xx = ('%1.0f' %kx)
                        #print (kx)
       p = s[i].partition('y')
       if p[1] == 'y' :
           # Обработка знака коэффициента
           if (s[i-1] == '0') or (s[i-1] not in ('-','+')):
               zn_ky = '+'
           else:
               zn_ky = s[i-1] 
           # Обработка тела коэффициента, если нет числа у Y - число =1
           if p[0] == '':
               ky = (float(zn_ky + '1')) + ky
           else:    
               pl = p[0].partition('+')
               if pl[1] == '+': 
                   if zn_ky == '+':
                       if pl[2] == '':
                           ky = float('1') + ky
                       else:
                           ky = float(pl[2]) + ky
                   elif zn_ky == '-':
                       if pl[2] == '':
                           ky = (-1 * float('1')) + ky
                       else:
                           ky = (-1 * float(pl[2])) + ky                    
               else:
                    mn = p[0].partition('-')
                    if mn[1] == '-':
                        if zn_ky == '+':
                            zn_ky = '-'
                            if mn[2] == '':
                                ky = (float(zn_ky + '1')) + ky
                            else:
                                ky = (float(zn_ky + mn[2])) + ky
                        elif zn_ky == '-':
                            zn_ky = '+'
                            if mn[2] == '':
                                ky = (float(zn_ky + '1')) + ky
                            else:
                                ky = (float(zn_ky + mn[2])) + ky                       
                    else:
                        # Итоговое число при Y
                        ky = float(zn_ky + (p[0])) + ky
                        #print (str(ky)+'y')
    ###### Обработка после =
       if fl_rabn == 'false':
           f = s[i].partition('=')
           if f[1] == '=' :
               fl_rabn = 'true'
           else:
               fl_rabn = 'false'    
    # Обработка свободных членов уравнения       
       if (re.search(r'([\d+]*\.\d+$|\d+$|[\d+]*\.$)', p[0]) \
           and (p[1] not in ('x','y'))):
           
           if (s[i-1] == '0') or (s[i-1] not in ('-','+')):
               zn_kc = '+'
           else:
               zn_kc = s[i-1] 
           pl = p[0].partition('+')
           if pl[1] == '+':
               if zn_kc == '+':
                   if pl[2] == '':
                       kc = float('0') + kc
                   else:
                       kc = float(pl[2]) + kc
               elif zn_kc == '-':
                   if pl[2] == '':
                       kc = (-1 * float('1')) + kc
                   else:
                       kc = (-1 * float(pl[2])) + kc                    
           else:
               mn = p[0].partition('-')
               if mn[1] == '-':
                   if zn_kc == '+':
                       zn_kc = '-'
                       if mn[2] == '':
                           kc = (float(zn_kc + '1')) + kc
                       else:
                           kc = (float(zn_kc + mn[2])) + kc
                   elif zn_kc == '-':
                       zn_kc = '+'
                       if mn[2] == '':
                           kc = (float(zn_kc + '1')) + kc
                       else:
                           kc = (float(zn_kc + mn[2])) + kc                        
               else:
                   kc = float(zn_kc + (p[0])) + kc
    #### Умножаем на (-1) если коэффициенты после знака '='
       if fl_rabn == 'true':
           kx = -(1) * kx ; ky = (-1) * ky ; kc = kc
       else:
           kx = kx ; ky = ky ; kc = (-1) * kc

    return (kx, ky, kc)

def main(): 
    """
    Это основная часть программы
    """
    # Список regex для нахождения степеней в строке файла  
    patterns = [ r'\^4', r'\^3', r'\^2', r'\^[^2,3,4]' ]
    # Этот regex для определения что есть степень в строке файла
    pat_stepen = r'\^'
    i = 0 # Это счетчик обработанных строк файла
    my_file = open("cистемы.txt")
    for line_my_file in my_file:
    #print (line_r)
    #f = open(file_n)
    #for line_my_file in f.readlines():
        i += 1 # Увеличиваем счетчик обработанных строк
        # Проверка, что в стоке файла есть показатель степени ^,если нет - это то система линейных ур.
        if re.search(pat_stepen, line_my_file):
                # Показатель степени есть, начинаем определять какой он [4,3,2]
                for pattern in patterns:
                    # Устанавливаем по regex, какая система уравнений
                    if re.search(pattern, line_my_file):
                        if pattern == r'\^4':
                                print (i,'Это биквадратное')
                                # Сплитуем членов системы
                                (arg1,arg2) = split_text(line_my_file)
                                print (arg1,"<===>",arg2)
                                # Определение коэффициентов биквадратного уравнения
                                for arg in (arg1,arg2):
                                    if re.search(r'x\^4', arg):
                                        (kx4,kx2,kc) = calc_koeff_4(arg,'x')
                                    elif re.search(r'y\^4', arg):
                                        (ky4,ky2,kf) = calc_koeff_4(arg,'y')
                                print (kx4,'x4   ',kx2,'x2   ',kc)
                                #print (ky4,'y4   ',ky2,'y2   ',kf)
                                # Передача уравнений в функцию решения биквадратного
                                (x1, x2, x3, x4) = deсision_4(kx4,kx2,kc)
                                (y1, y2, y3, y4) = deсision_4(ky4,ky2,kf)
                                print (x1,' ',x2,' ',x3,' ',x4)
                                print (y1,' ',y2,' ',y3,' ',y4)
                                break # Переход к следующей строке файла
                        elif  pattern == r'\^3':
                                print (i,'Это кубическое:')
                                # Сплитуем членов системы
                                (arg1,arg2) = split_text(line_my_file)
                                print (arg1,"<===>",arg2)
                                # Определение коэффициентов кубического уравнения
                                for arg in (arg1,arg2):
                                    if re.search(r'x\^3', arg):
                                        (kx3,kx,kc) = calc_koeff_3(arg,'x')
                                    elif re.search(r'y\^3', arg):
                                        (ky3,ky,kf) = calc_koeff_3(arg,'y')
                                print (kx3,'x3   ',kx,'x   ',kc)
                                print (ky3,'y3   ',ky,'y   ',kf)
                                # Передача уравнений в функцию решения кубического
                                (x_1,x_2) = deсision_3(kx3,kx,kc)
                                (y_1,y_2) = deсision_3(ky3,ky,kf)
                                print (x_1,' ',x_2,' ',y_1,' ',y_2)                                 
                                break # Переход к следующей строке файла
                        elif pattern == r'\^2':
                                print (i,'Это квадратное:')
                                # Сплитуем членов системы
                                (arg1,arg2) = split_text(line_my_file)
                                print (arg1,"<===>",arg2)
                                # Определение коэффициентов квадратного уравнения
                                for arg in (arg1,arg2):
                                    if re.search(r'x\^2', arg):
                                        (kx2,kx,kc) = calc_koeff_2(arg,'x')
                                    elif re.search(r'y\^2', arg):
                                        (ky2,ky,kf) = calc_koeff_2(arg,'y')
                                print (kx2,'x2   ',kx,'x   ',kc)
                                #print (ky2,'y2   ',ky,'y   ',kf)
                                # Передача коэффициентов в функцию решения квадратного
                                (x_1,x_2) = deсision_2(kx2,kx,kc)
                                #(y_1,y_2) = deсision_2(ky2,ky,kf)
                                print (x_1,'   ',x_2)
                                #print (y_1,'   ',y_2)
                                break # Переход к следующей строке файла
                        elif pattern == r'\^[^2,3,4]':
                                print (i,'Показатель степени <2 или >4:')
                                break # Переход к следующей строке файла
                        else:
                                print (i,'Строка вообще неформат:')
                                break # Переход к следующей строке файла
        else:
                print (i,'Это система линейных уравнений:')
                # Определяем членов системы
                (arg1,arg2) = split_text(line_my_file)
                print (arg1,"<===>",arg2)
                # Определение коэффициентов линейного уравнения
                (ax,by,e) = calc_koeff(arg1)
                (cx,dy,f) = calc_koeff(arg2)
                print ('ax=%s, by=%s, e=%s' %(ax,by,e))
                print ('cx=%s, dy=%s, f=%s' %(cx,dy,f))
                # Передача коэффициентов в функцию решения линейных уравнений
                (x,y) = npdeсision_linear(ax,by,e,cx,dy,f)
                #(x,y) = simple_deсision_linear(ax,by,e,cx,dy,f)
    my_file.close()      

if __name__ == '__main__': #Так визуально удобней 
    main()
