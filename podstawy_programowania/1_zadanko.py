'''
Użytkownik podaje z klawiatury dwie wartości,
maksymalną i minimalną przedziału z którego będzie wylosowane
5 liczb całkowitych
Wylosowane liczby wyświetl w formacie:
Liczba1: ...
Liczba2: ...
...
Liczba5: ...
'''

import random

x1 = eval(input("Podaj poczatek przedzialu: "))
x2 = eval(input("Podaj koniec przedzialu: "))
x=0
for i in range(5):
    liczba = random.randint(x1,x2)
    x= x+1
    print("Liczba nr ",x, ": ",liczba)