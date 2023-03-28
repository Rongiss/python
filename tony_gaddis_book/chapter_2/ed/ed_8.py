FED_TAX = 0.07
OFFICE_TAX = 0.18
totalPrice = float(input('input total sum '))

officeTax = totalPrice * OFFICE_TAX
fedTax = totalPrice * FED_TAX
print(f'Total price {totalPrice:.2f}')
print(f"Fed tax {fedTax:.2f}")
print(f"office tax {officeTax:.2f}")
print(f"Total {totalPrice + officeTax + fedTax:.2f}")