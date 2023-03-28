# Константы для ставок федерального и регионального налога с продаж
STATE_TAX_RATE = 0.05
COUNTY_TAX_RATE = 0.025

# Получить сумму покупки.
purchase = float(input("Введите сумму покупки: "))

state_tax = purchase * STATE_TAX_RATE
county_tax = purchase * COUNTY_TAX_RATE
total_tax = county_tax + state_tax
total_sum = purchase +total_tax

# Напечатать информацию о продаже.
print ("Сумма покупки:", format(purchase, '.2f'))
print ("Федеральный налог:", format(state_tax, '.2f'))
print ("Региональный налог:", format(county_tax, '.2f'))
print ("Суммарный налог:", format(total_tax, '.2f'))
print ("Сумма продажи:", format(total_sum, '.2f'))