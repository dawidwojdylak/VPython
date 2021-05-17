#Proszę napisać program, który pyta o liczbę i po wpisaniu 
# liczby program generuje informację czy liczba jest pierwsza, parzysta lub nieparzysta.
#Następnie program pyta o kolejną liczbę itd. Po wpisaniu "koniec", program kończy działanie.


def isPrime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    prime = int(n**0.5) + 1
    for div in range(3, prime, 2):
        if n % div == 0:
            return False
    return True

answer = input("Prosze wprowadzic liczbe (koniec konczy program): ")
while answer != "koniec":
    n = int(answer)
    if  n % 2 == 0:
        print("Podana liczba jest parzysta")
    else:
        print("Podana liczba jest nieparzysta")

    if isPrime(n):
        print("Podana liczba jest pierwsza")
    else:
        print("Podana liczba nie jest pierwsza")
    print("\n")
    answer = input("Prosze wprowadzic liczbe: ")

print("Koniec programu...")
