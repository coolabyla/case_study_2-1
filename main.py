# Case 2
# Developers:   Nikita Beushev (70%)
#               Alexandra Kozadeeva (60%)
#               Anzhelika Kurepova (55%)

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
QUESTION4 = input('К какой категории вас можно отнести? ')
QUESTION5 = int(input('Какой у вас необлагаемый налогом доход? '))

# string constants
name_month = [JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC]

annual_income = 0
for month in range(12):
    income = int(input(QUESTION2.format(name_month[month])))
    annual_income += income
print(annual_income)

# TO DO: (Anzhelika) one person
if QUESTION4 == 'один субъект' and annual_income >= 0 and annual_income <= 9075:
    print(0.1 * (annual_income - QUESTION5))
elif QUESTION4 == 'один субъект' and annual_income >= 9076 and annual_income <= 36_900:
    print(0.15 * (annual_income - 9076 - QUESTION5) + 0.1 * (9076 - 0))
elif QUESTION4 == 'один субъект' and annual_income >= 36_901 and annual_income <= 89_350:
    print(0.25 * (annual_income - 36_901 - QUESTION5) + 0.1 * (9_076 - 0) + 0.15 * (36_901 - 9076))
elif QUESTION4 == 'один субъект' and annual_income >= 89_351 and annual_income <= 186_350:
    print(0.28 * (annual_income - 89_351 - QUESTION5) + 0.1 * (9076 - 0) + 0.15 * (36_901 - 9076) +
          + 0.25 * (89_351 - 36_901))
elif QUESTION4 == 'один субъект' and annual_income >= 186_351 and annual_income <= 405_100:
    print(0.33 * (annual_income - 186_351 - QUESTION5) + 0.1 * (9076 - 0) + 0.15 * (36_901 - 9076) +
          + 0.25 * (89_351 - 36_901) + 0.28 * (186_351 - 89_351))
elif QUESTION4 == 'один субъект' and annual_income >= 405_101 and annual_income <= 406_750:
    print(0.35 * (annual_income - 405_101 - QUESTION5) + 0.1 * (9076 - 0) + 0.15 * (36_901 - 9076) +
         + 0.25 * (89_351 - 36_901) + 0.28 * (186_351 - 89_351) + 0.33 * (405_101 - 186_351))
elif QUESTION4 == 'один субъект' and annual_income >= 406_751:
    print(0.396 * (annual_income - 406_751 - QUESTION5) + 0.1 * (9076 - 0) + 0.15 * (36_901 - 9076) +
          + 0.25 * (89_351 - 36_901) + 0.28 * (186_351 - 89_351) + 0.33 * (405_101 - 186_351) +
          + 0.35 * (406_751 - 405_101))

# TO DO: (Alexandra) married couple





















# TO DO: (Nikita) single parent
