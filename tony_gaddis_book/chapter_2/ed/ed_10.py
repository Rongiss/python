# 48 булочек это
# 1.5 стакана сахара
# 1 стакан муки
# 2.75 стакана муки
# Для 1 булочки понадобиться все разделить на 48

SUGARE = 1.5 / 48 #
OIL = 1 / 48
FLOUR = 2.75 / 48

howMany = int(input("How many bun "))

print(f"Youre need\nsugare {SUGARE*howMany:.2f}\n"
      f"oli {OIL* howMany:.2f}\n"
      f"flour {FLOUR*howMany:.2f}")