T = "T"
N = "N"
e = float(input("Podaj 1. przekątną rombu: "))
f = float(input("Podaj 2. przekątną rombu: "))

print(f"Pole rombu o przekątnej nr 1 równej {e} i przekątnej nr 2 równej {f} jest równe {(e*f)/2}")

confirmation = input("Istnieje kilka metod oblicznia pola rombu. Czy chcesz użyć drugiej metody? Różnią się użyciem innych danych. (T/N): ")
if confirmation == N:
    exit()

if confirmation == float or int:
    print("Nie podałeś/aś T lub N, lecz liczbę. Może to pomyłka?")
    exit()

if confirmation == T:
    a = float(input("Podaj długość podstawy rombu: "))
    h = float(input("Podaj wysokość rombu: "))
print(f"Pole rombu o podstawie równej {a} i wysokości równej {h} jest równe {a*h}")
