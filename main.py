# Case 2
# Developers:   Nikita Beushev ()
#               Alexandra Kozadeeva ()
#               Anzhelika Kurepova ()

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
QUESTION3 = 'Какой у вас необлагаемый налогом доход? '
category = input(QUESTION1)
deduction = int(input(QUESTION3))

# string constants
name_month = [JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC]

annual_income = 0
for month in range(12):
    income = int(input(QUESTION2.format(name_month[month])))
    annual_income += income
print(annual_income)

# TODO: (Anzhelika) one person
if category == 'один субъект' and annual_income >= 0 and annual_income <= 9075:
    print(0.1 * (annual_income - deduction))
elif category == 'один субъект' and annual_income >= 9076 and annual_income <= 36_900:
    print(0.15 * (annual_income - 9076 - deduction) + 0.1 * (9076 - 0))
elif category == 'один субъект' and annual_income >= 36_901 and annual_income <= 89_350:
    print(0.25 * (annual_income - 36_901 - deduction) + 0.1 * (9_076 - 0) + 0.15 * (36_901 - 9076))
elif category == 'один субъект' and annual_income >= 89_351 and annual_income <= 186_350:
    print(0.28 * (annual_income - 89_351 - deduction) + 0.1 * (9076 - 0) + 0.15 * (36_901 - 9076) +
          + 0.25 * (89_351 - 36_901))
elif category == 'один субъект' and annual_income >= 186_351 and annual_income <= 405_100:
    print(0.33 * (annual_income - 186_351 - deduction) + 0.1 * (9076 - 0) + 0.15 * (36_901 - 9076) +
          + 0.25 * (89_351 - 36_901) + 0.28 * (186_351 - 89_351))
elif category == 'один субъект' and annual_income >= 405_101 and annual_income <= 406_750:
    print(0.35 * (annual_income - 405_101 - deduction) + 0.1 * (9076 - 0) + 0.15 * (36_901 - 9076) +
         + 0.25 * (89_351 - 36_901) + 0.28 * (186_351 - 89_351) + 0.33 * (405_101 - 186_351))
elif category == 'один субъект' and annual_income >= 406_751:
    print(0.396 * (annual_income - 406_751 - deduction) + 0.1 * (9076 - 0) + 0.15 * (36_901 - 9076) +
          + 0.25 * (89_351 - 36_901) + 0.28 * (186_351 - 89_351) + 0.33 * (405_101 - 186_351) +
          + 0.35 * (406_751 - 405_101))

# TODO: (Alexandra) married couple





















# TODO: (Nikita) single parent
if category == 'один субъект' and annual_income >= 0 and annual_income <= 12950:
    print(0.1 * (annual_income - deduction))
elif category == 'один субъект' and annual_income >= 12951 and annual_income <= 49_400:
    print(0.15 * (annual_income - 12951 - deduction) + 0.1 * (12951 - 0))
elif category == 'один субъект' and annual_income >= 49_401 and annual_income <= 127_550:
    print(0.25 * (annual_income - 49_401 - deduction) + 0.1 * (9_076 - 0) + 0.15 * (49_401 - 12951))
elif category == 'один субъект' and annual_income >= 127_551 and annual_income <= 206_600:
    print(0.28 * (annual_income - 127_551 - deduction) + 0.1 * (12951 - 0) + 0.15 * (49_401 - 12951) +
          + 0.25 * (127_551 - 49_401))
elif category == 'один субъект' and annual_income >= 206_601 and annual_income <= 405_100:
    print(0.33 * (annual_income - 206_601 - deduction) + 0.1 * (12951 - 0) + 0.15 * (49_401 - 12951) +
          + 0.25 * (127_551 - 49_401) + 0.28 * (206_601 - 127_551))
elif category == 'один субъект' and annual_income >= 405_101 and annual_income <= 432_200:
    print(0.35 * (annual_income - 405_101 - deduction) + 0.1 * (12951 - 0) + 0.15 * (49_401 - 12951) +
         + 0.25 * (127_551 - 49_401) + 0.28 * (206_601 - 127_551) + 0.33 * (405_101 - 206_601))
else:
    print(0.396 * (annual_income - 432_201 - deduction) + 0.1 * (12951 - 0) + 0.15 * (49_401 - 12951) +
          + 0.25 * (127_551 - 49_401) + 0.28 * (206_601 - 127_551) + 0.33 * (405_101 - 206_601 +
          + 0.35 * (432_201 - 405_101)))
