import math
from time import perf_counter

def m(a,x,y,d):
    return math.sin(x+2*y)**2/abs(x-math.exp(a*x*y)) + 0.3* (x - (a+4.2)/d/y)**(1/3)+math.log(a*x**2, 5)

def z(k, x , y):
    return math.log(x)+math.pi*(math.pi/2* (-math.pi/2 - math.atan(y*y)))+math.tan(k*x/2)

import re
def time(string):
    repl =r"TBD"
    pattern = r'(([0,1][0-9])|(2[0-3])):[0-5][0-9]:[0-5][0-9]' # ([0,1][0-9]) это 01 - 19, а (2[0-3]) это 20 - 23 (HH) соответственно [0-5][0-9] это 00 - 59(MM) тоже самое [0-5][0-9] это 00 - 59 (SS)
    string = re.sub(pattern, repl, string)
    pattern= r'(([0,1][0-9])|(2[0-3])):[0-5][0-9]' # ([0,1][0-9]) это 01 - 19, а (2[0-3]) это 20 - 23 (HH) соответственно [0-5][0-9] это 00 - 59(MM)
    return re.sub(pattern, repl, string) # Ищем шаблон (pattern) в строке и заменяем его на указанную подстроку(в данном случае заменяем время на TBD

print(time('Уважаемые! Если вы к 09:00 не вернете чемодан, то уже в 09:00:01 я за себя не отвечаю. PS. С временем 25:50 всё нормально!'))
