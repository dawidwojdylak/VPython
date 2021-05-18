# Metoda Monte Carlo i liczba pi.

# Proszę spojrzeć na rysunek
# https://alg24.com/pl/obliczanie-liczby-pi-metoda-monte-carlo
# Mamy okrąg o promieniu 1 wpisany w kwadrat. Teraz strzelamy losowo w kwadrat. Strzał to punkt (x,y). Jeśli liczba strzałów będzie bardzo duża to jest dość jasne, że

# N_okrąg / N_kwadrat = Pole_okręgu / Pole_kwadratu

# gdzie:
# N_okrąg to liczba trafień w okrąg
# N_kwadrat to liczba trafień w kwadrat
# Pole_okręgy to jest pole okręgu = pi*r**2 = pi  bo r = 1. Czyli mamy pi.
# Pole_kwadratu to jest pole kwadratu = 2*2 = 4.

# Zatem mamy
# pi = 4* N_okrąg / N_kwadrat.

# Używając generatora liczb losowych (patrz wykład) proszę policzyć pi. Proszę wygenerować plik tekstowy z

# 1) wyliczona liczba z tej metody,  stosunek wyliczonej liczby do dokladnej liczby pi
# 2)
# 3)
# 4)
# .
# .
# 99)
# 100)
# 10**3)
# 10**4)
# 10**5)
# 10**6)

# gdzie np. 2) oznacza, że mamy 2 przypadkowe strzały w kwadrat.
# 10**3) oznacza, że mamy 10**3 przypadkowych strzałów w kwadrat.
# Liczby wskazujące wiersze 1), 2) itd. mają być widoczne w pliku.

# Proszę zaobserwować, ile strzałów wystarczy aby dostać liczbę pi z dokładnością powiedzmy 5%.
###########################################################################################################

import random
import numpy as np


# przyjmuje, że wszystkie strzaly mieszcza sie w kwadreacie
def gdziePadlStrzal(x,y):
    if np.sqrt(x**2 + y**2) <=1:
        return True
    else:
        return False

def strzal():
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    return (x, y)

# n liczba strzalow
def obliczPI(n): 
    f = open('zad2.txt','w')
    No = 1
    Nk = 1
    pi = 1
    for i in range(0,n):
        x, y = strzal()
        if i < 101 or i == 10**3 or i == 10**4 or i == 10**5 or i == 10**6:  
            f.write(str(Nk - 1) + ") " + str(pi) + ", " + str(pi/np.pi) + "\n")  
        if gdziePadlStrzal(x,y) == True:
            No += 1
        Nk += 1
        pi = 4 * No/Nk
    f.close()

obliczPI(10**6)