# Szereg Leibnitza.

# pi = 4*(1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + ...)

# gdzie pi to jest liczba pi.
# Proszę napisać program, który liczy pi w ten sposób. Program powinien tworzyć plik tekstowy w którem ma być wypisane:

# 1) wyliczona liczba z szeregu,  stosunek wyliczonej liczby do dokladnej liczby pi
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
# 10**7)

# Np. wiersz 2) oznacza, że bierzemy 2 wyrazy szeregu Leibnitza tzn. 4*(1 - 1/3).
# Wiersz 86) oznacza, że bierzemy 86 wyrazów szeregu Leibnitza itd.
# Wypisujemy dla wszystkich liczb całkowitych od 1 do 100 a potem skok na 10**3, 10**4, 10**5, 10**6, 10**7.
# Liczby wskazujące wiersze 1), 2) itd. mają być widoczne w pliku.
# Im więcej wyrazów szeregu Leibnitza tym lepiej powinniśmy przybliżyć liczbę pi i stosunek powinien być bliższy jedynki.
#########################################################################################################################

import time
import numpy as np

# n - ilosc wyrazow szeregu Leibniza
def findPI_v1(pi, n):
    f = open('zad1.txt','w')
    for i in range(1, n + 1):
        if i % 2 == 0:
            pi += 4 * ((-1) / (2 * i - 1))
        else:
            pi += 4 / (2 * i - 1)
        if i <= 100 or i == 10**3 or i == 10**4 or i == 10**5 or i == 10**6 or i == 10**7:
            #print("i:", i, ", pi = ", pi)
            f.write("i: " + str(i) + ", pi = " + str(pi) + ", pi/np.pi = " + str(pi/np.pi) + "\n")
    f.close()
    return pi

# wolniejszy sposób
def findPI_v2(pi, n):
    for i in range(1, n + 1):
        pi += 4* ((-1)**(i - 1) / ( 2 * i - 1))

# dt1 to pomiar czasu wykonania algorytmu
pi = 0
t1 = time.time()
print(findPI_v1(pi, 10**7))
t2 = time.time()
print("dt1 = " , t2 - t1)

# pi = 0
# t3 = time.time()
# print(findPI_v2(pi, 10**7))
# t4 = time.time()
# print("dt2 = ", t4 - t3)