# Case 1
# Developers:   Nikita Beushev (70%)
#               Alexandra Kozadeeva (60%)
#               Anzhelika Kurepova (55%)

# TODO:


import calendar
JAN = 'январе'
FEB = 'феврале'
MAR = 'марте'
APR = 'апреле'
MAY = 'мае'
JUN = 'июне'
JUL = 'июле'
AUG = 'августе'
SEP = 'сентябре'
OCT = 'октябре'
NOV = 'ноябре'
DEC = 'декабре'
QUESTION1 = 'К какой категории вас можно отнести? '
QUESTION2 = 'Сколько денег вы заработали в {}: '
QUESTION3 = 'Какой у вас необлагаемый налогом доход?'

# string constants
name_month = [JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC]

annual_income = 0
for month in range(12):
    income = int(input(QUESTION2.format(name_month[month])))
    annual_income += income
print(annual_income)
