a = float(input("Wpisz długość boku numer 1: "))
b = float(input("Wpisz długość boku numer 2: "))

if b == a:
    print("Długość boków prostokąta nie może być taka sama")
    exit()
print(f"Pole powierzchni prostokąta o boku numer 1 równym {a} i boku numer 2 równym {b} jest równe {a*b}")
