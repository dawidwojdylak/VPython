# 2. Liczba doskonała to jest liczba naturalna, 
# która jest sumą wszystkich swych dzielników właściwych 
# (to znaczy od niej mniejszych). Np. 6 jest liczbą doskonałą, 
# bo suma jej dzielników (1,2,3) wynosi 6. Proszę napisać program, 
# który wylicza cztery pierwsze liczby doskonałe.

l = 0
i = 1
n = 4
result = [] 

def dividers(n):
    list_of_dividers = [] 
    for i in range(1, (int(n/2) + 1)): 
        if n % i == 0 and n != i:
            list_of_dividers.append(i) 
    return list_of_dividers 

 
def find_ideal():
    n = 1    
    howMany = 0
    ideals = []
    while howMany < 4: 
            sum = 0
            for i in dividers(n):
                sum = sum + i 

            if n == sum:
                howMany += 1
                ideals.append(n)
            n += 1
    print(ideals)

find_ideal()

