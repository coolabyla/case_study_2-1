import pandas as pd

month_dict_raw = pd.read_csv('month_dict.csv')
month_dict = []

for i in range(0, len(month_dict_raw['Months'])):
    month_dict.append(month_dict_raw['RUS'][i])

QUESTION1 = '''К какой категории вас можно отнести? 
1 - Один субъект
2 - Супружеская пара
3 - Родитель-одиночка\n'''
QUESTION2 = 'Какова ваша сумма налогового вычета? '
QUESTION3 = 'Каков ваш доход в {}? '
TAX = 'Ваш подоходный налог:'
