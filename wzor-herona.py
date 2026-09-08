from math import sqrt

a = (int or float)(input("Podaj długość boku 1: "))
b = (int or float)(input("Podaj długość boku 2: "))
c = (int or float)(input("Podaj długość boku 3: "))

p = (a+b+c)/2
wzor = sqrt(p*(p-a)*(p-b)*(p-c))

if wzor == 0:
    print("Taki trójkąt nie istnieje")
    exit()

print(f"Korzystając ze wzoru Herona, możemy określić, że trójkąt o bokach {a} {b} i {c} ma pole {wzor}")


