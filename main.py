# Case 2
# Developers:
#
#

# string constants
name_month = [JAN, FAB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC]

annual_income = 0
for month in range(12):
    print('{} {}:'.format(QUESTION,name_month[month], end ='')
    income = float(input())
    annual_income += income
print(annual_income)