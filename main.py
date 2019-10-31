# Case 2
# Developers:   Nikita Beushev ()
#               Alexandra Kozadeeva ()
#               Anzhelika Kurepova ()

import pandas as pd
import localization as lc

# input data
tax_category_data = pd.read_csv('tax_category_data.csv')
name_month = lc.month_dict

category = int(input(lc.QUESTION1))
deduction = int(input(lc.QUESTION2))

annual_income = 0
for month in range(12):
    income = int(input(lc.QUESTION3.format(name_month[month])))
    annual_income += income

taxable_income = int(annual_income - deduction)


# solution
def tax_calculation(taxable_income_int=taxable_income,
                    category_int=category):
# расчет накопленных сумм
    tax_1 = (int(tax_category_data['Income_' + str(category_int) + '_category'][0]) + 1) * float(tax_category_data['%'][0])
    tax_2 = tax_1 + (int(tax_category_data['Income_' + str(category_int) + '_category'][1]) -
                     int(tax_category_data['Income_' + str(category_int) + '_category'][0])) * float(tax_category_data['%'][1])
    tax_3 = tax_2 + (int(tax_category_data['Income_' + str(category_int) + '_category'][2]) -
                     int(tax_category_data['Income_' + str(category_int) + '_category'][1])) * float(tax_category_data['%'][2])
    tax_4 = tax_3 + (int(tax_category_data['Income_' + str(category_int) + '_category'][3]) -
                     int(tax_category_data['Income_' + str(category_int) + '_category'][2])) * float(tax_category_data['%'][3])
    tax_5 = tax_4 + (int(tax_category_data['Income_' + str(category_int) + '_category'][4]) -
                     int(tax_category_data['Income_' + str(category_int) + '_category'][3])) * float(tax_category_data['%'][4])
    tax_6 = tax_5 + (int(tax_category_data['Income_' + str(category_int) + '_category'][5]) -
                     int(tax_category_data['Income_' + str(category_int) + '_category'][4])) * float(tax_category_data['%'][5])

    if 0 <= annual_income <= int(tax_category_data['Income_' + str(category_int) + '_category'][0]):
        tax = taxable_income_int * float(tax_category_data['%'][0])
    elif annual_income <= int(tax_category_data['Income_' + str(category_int) + '_category'][1]):
        tax = tax_1 + (taxable_income_int - (int(tax_category_data['Income_' + str(category_int) + '_category'][0]) + 1)) \
                        * float(tax_category_data['%'][0])
    elif annual_income <= int(tax_category_data['Income_' + str(category_int) + '_category'][2]):
        tax = tax_2 + (taxable_income_int - (int(tax_category_data['Income_' + str(category_int) + '_category'][1]) + 1)) \
                        * float(tax_category_data['%'][1])
    elif annual_income <= int(tax_category_data['Income_' + str(category_int) + '_category'][3]):
        tax = tax_3 + (taxable_income_int - (int(tax_category_data['Income_' + str(category_int) + '_category'][2]) + 1)) \
                        * float(tax_category_data['%'][2])
    elif annual_income <= int(tax_category_data['Income_' + str(category_int) + '_category'][4]):
        tax = tax_4 + (taxable_income_int - (int(tax_category_data['Income_' + str(category_int) + '_category'][3]) + 1)) \
                        * float(tax_category_data['%'][3])
    elif annual_income <= int(tax_category_data['Income_' + str(category_int) + '_category'][5]):
        tax = tax_5 + (taxable_income_int - (int(tax_category_data['Income_' + str(category_int) + '_category'][4]) + 1)) \
                        * float(tax_category_data['%'][4])
    else:
        tax = tax_6 + (taxable_income_int - (int(tax_category_data['Income_' + str(category_int) + '_category'][5]) + 1)) \
                        * float(tax_category_data['%'][5])
    return tax


print(lc.TAX, format(tax_calculation(), '.2f'))
