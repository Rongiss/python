# условия покупики акций
howManyActIn = 2000
howManyIn = 40

# Процент брокера
PECENT_DILL = 0.03

# Условия продажи акций
howManyActOut = 2000
howManyOut = 42.75

buyAcnion = howManyActIn * howManyIn
brocerSummIn = buyAcnion * PECENT_DILL

sellAcnion =  howManyOut * howManyActOut
brocerSummOut = sellAcnion * PECENT_DILL


print(f"Summ in {buyAcnion:.2f}")
print(F"Broker summ in {brocerSummIn:.2f}")
print(f"Sell {sellAcnion:.2f}")
print(f"brocer out {brocerSummOut:.2f}")
print(f"Profit {brocerSummOut + sellAcnion - buyAcnion + brocerSummIn:.2f}")