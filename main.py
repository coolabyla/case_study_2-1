# Case 2
# Developers:   Nikita Beushev ()
#               Alexandra Kozadeeva ()
#               Anzhelika Kurepova ()

# localization
import local as lc
category = int(input(lc.QUESTION1))
deduction = int(input(lc.QUESTION2))

# string constants
name_month = [lc.JAN, lc.FEB, lc.MAR, lc.APR, lc.MAY, lc.JUN, lc.JUL, lc.AUG, lc.SEP, lc.OCT, lc.NOV, lc.DEC]

annual_income = 0
for month in range(12):
    income = int(input(lc.QUESTION3.format(name_month[month])))
    annual_income += income

taxable_income = int(annual_income - deduction)

# TODO: (Anzhelika) one person
if category == 1 and annual_income >= 0 and annual_income <= 9075:
    tax = (0.1 * taxable_income)
elif category == 1 and annual_income >= 9076 and annual_income <= 36_900:
    tax = (0.15 * (taxable_income - 9076) + 0.1 * (9076 - 0))
elif category == 1 and annual_income >= 36_901 and annual_income <= 89_350:
    tax = (0.25 * (taxable_income - 36_901) + 0.1 * (9_076 - 0) + 0.15 * (36_901 - 9076))
elif category == 1 and annual_income >= 89_351 and annual_income <= 186_350:
    tax = (0.28 * (taxable_income - 89_351) + 0.1 * (9076 - 0) + 0.15 * (36_901 - 9076) +
          + 0.25 * (89_351 - 36_901))
elif category == 1 and annual_income >= 186_351 and annual_income <= 405_100:
    tax = (0.33 * (taxable_income - 186_351) + 0.1 * (9076 - 0) + 0.15 * (36_901 - 9076) +
          + 0.25 * (89_351 - 36_901) + 0.28 * (186_351 - 89_351))
elif category == 1 and annual_income >= 405_101 and annual_income <= 406_750:
    tax = (0.35 * (taxable_income - 405_101) + 0.1 * (9076 - 0) + 0.15 * (36_901 - 9076) +
          + 0.25 * (89_351 - 36_901) + 0.28 * (186_351 - 89_351) + 0.33 * (405_101 - 186_351))
elif category == 1 and annual_income >= 406_751:
    tax = (0.396 * (taxable_income - 406_751) + 0.1 * (9076 - 0) + 0.15 * (36_901 - 9076) +
          + 0.25 * (89_351 - 36_901) + 0.28 * (186_351 - 89_351) + 0.33 * (405_101 - 186_351) +
          + 0.35 * (406_751 - 405_101))

# TODO: (Alexandra) married couple





















# TODO: (Nikita) single parent
if category == 3 and 0 <= annual_income <= 12950:
    tax = (0.1 * taxable_income)
elif category == 3 and 12_951 <= annual_income <= 49_400:
    tax = (0.15 * (taxable_income - 12_951) + 0.1 * (12951 - 0))
elif category == 3 and 49_401 <= annual_income <= 127_550:
    tax = (0.25 * (taxable_income - 49_401) + 0.1 * (9_076 - 0) + 0.15 * (49_401 - 12_951))
elif category == 3 and 127_551 <= annual_income <= 206_600:
    tax = (0.28 * (taxable_income - 127_551) + 0.1 * (12_951 - 0) + 0.15 * (49_401 - 12_951) +
           + 0.25 * (127_551 - 49_401))
elif category == 3 and 206_601 <= annual_income <= 405_100:
    tax = (0.33 * (taxable_income - 206_601) + 0.1 * (12951 - 0) + 0.15 * (49_401 - 12_951) +
           + 0.25 * (127_551 - 49_401) + 0.28 * (206_601 - 127_551))
elif category == 3 and 405_101 <= annual_income <= 432_200:
    tax = (0.35 * (taxable_income - 405_101) + 0.1 * (12951 - 0) + 0.15 * (49_401 - 12_951) +
           + 0.25 * (127_551 - 49_401) + 0.28 * (206_601 - 127_551) + 0.33 * (405_101 - 206_601))
else:
    tax = (0.396 * (taxable_income - 432_201) + 0.1 * (12951 - 0) + 0.15 * (49_401 - 12951) +
           + 0.25 * (127_551 - 49_401) + 0.28 * (206_601 - 127_551) + 0.33 * (405_101 - 206_601 +
           + 0.35 * (432_201 - 405_101)))

print(lc.TAX, format(tax, '.2f'))

