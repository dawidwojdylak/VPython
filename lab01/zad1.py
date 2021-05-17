# 1. Proszę napisać funkcję, która przyjmuje dowolną listę z liczbami 
# i zwraca listę z dwoma liczbami: suma i iloczyn liczb z listy.
# W programie nie wolno używać range() oraz wbudowanej funkcji sum().



#########################################################################
def fun(a):
    sum = 0
    mult = 1
    for i in a:
        sum = sum + i
        mult = mult * i

    result = [sum, mult]
    return result
#########################################################################
#  TEST
list1 = [1,2,3,4,5,6,7,8,9]
res1 = fun(list1)
print(res1)
list2 = [3,4,5]
print(fun(list2))


#########################################################################
# n = int (input ("Prosze wprowadzic dlugosc listy: "))
# list2 = []
# i = 0
# while i < n:
#     list2.append(int(input("Prosze wprowadzic liczbe: ")))
#     i = i + 1
# print("Wprowadzona lista: ", list2)
# res2 = fun(list2)
# print(res2)
