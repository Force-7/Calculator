import sys

def Dodawanie(wyb1, wyb2):
    return wyb1 + wyb2

def Odejmowanie(wyb1, wyb2):
    return wyb1 - wyb2

def Mnozenie(wyb1, wyb2):
    return wyb1 * wyb2

def Dzielenie(wyb1, wyb2):
    return wyb1 / wyb2

def Modulo(wyb1, wyb2):
    return wyb1 % wyb2

def Potegowanie(wyb1, wyb2):
    return wyb1 ** wyb2

def silnia(n):
    if n > 1:
        return n * silnia(n-1)
    else:
        return 1




print("Prosty Kalkulator!")
print("""Wybierz, co chcesz zrobić
    1.Dodawanie
    2.Odejmowanie
    3.Mnożenie
    4.Dzielenie
    5.Reszta z dzielenia(Modulo)
    6.Potęgowanie
    7.Silnia
    8.Wyjście""")

wyb0 = int(input("Wybierz liczbę od 1 do 7: "))
if wyb0 == 8:
    print("Pomyślnie wyłączyłeś program")
    sys.exit()


if wyb0 < 0 or wyb0 > 8:
    print("Podałeś niewłaściwą liczbę, Spróbuj ponowanie!")
    sys.exit()

elif wyb0 == 7:
    wyb3 = int(input("Podaj liczbę z której chcesz uzyskać silnie: "))
    print(wyb3,"! =", silnia(wyb3))
    sys.exit()

wyb1 = float(input("Podaj pierwszą liczbę: "))
wyb2 = float(input("Podaj drugą liczbę: "))

if wyb0 == 1:
    print(wyb1, "+", wyb2, "=",
        Dodawanie(wyb1,wyb2))

elif wyb0 == 2:
    print(wyb1, "-", wyb2, "=",
        Odejmowanie(wyb1,wyb2))

elif wyb0 == 3:
    print(wyb1, "*", wyb2, "=",
        Mnozenie(wyb1,wyb2))

elif wyb0 == 4:
    print(wyb1, "/", wyb2, "=",
        Dzielenie(wyb1,wyb2))

elif wyb0 == 5:
    print(wyb1, "%", wyb2, "=",
        Modulo(wyb1,wyb2))

elif wyb0 == 6:
    print(wyb1, "**", wyb2, "=",
        Potegowanie(wyb1,wyb2))
