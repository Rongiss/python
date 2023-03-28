listBuy = []
percent = 0.07
for i in range(5):
    listBuy.append(float(input("Input summ youre bay ")))
total = sum(listBuy)
print(f'\nSumm {total:.2f}\nPeresent {total * percent:.2f}'
      f'\nTotal sum {total + total * percent:.2f}')