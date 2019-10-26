# Case 1
# Developers:   Nikita Beushev (70%)
#               Alexandra Kozadeeva (60%)
#               Anzhelika Kurepova (55%)

# TODO:


import calendar
JAN = 'янв'
FEB = 'фев'
MAR = 'мар'
APR = 'апр'
MAY = 'май'
JUN = 'июнь'
JUL = 'июль'
AUG = 'авг'
SEP = 'сен'
OCT = 'окт'
NOV = 'нов'
DEC = 'дек'
QUESTION = 'Сколько денег вы заработали в {}: '

# string constants
name_month = [JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC]

annual_income = 0
for month in range(12):
    income = int(input(QUESTION.format(name_month[month])))
    annual_income += income
print(annual_income)
