import calendar

cal = calendar.TextCalendar()

print(cal.prmonth(2018,6))

#日曜始まり
cal = calendar.TextCalendar(6)

print(cal.prmonth(2018,6))

from calendar import TextCalendar
cal = TextCalendar(6)
print(cal.prmonth(2018,7))

cal = TextCalendar(6)
cals = cal.formatmonth (2018,8)
print(cals)

import math
num = math.sqrt(81)
print(num)

#mathを書かなくてよいImport
from math import *
#平方根
print(sqrt(81))
#円周率
print(pi)

import random
print(random.randint(15,20))
print(random.randint(15,20))
