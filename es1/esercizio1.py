'''Acquisire una lista di 10 numeri interi random e comunicare la somma e la media dei numeri in
lista utilizzando 2 funzioni, rispettivamente somma e media'''

import random
#funzione per la somma della lista
def somma(lista):
    somma = 0
    for elemento in lista:
        somma += elemento
    return somma

#funzione per la media della lista
def media(lista):
    return somma(lista) / len(lista)

lista=[]


#mi permette di mettere una lista in coda lista append 
for indice in range(10):
    lista.append(random.randint(1, 100))

print(lista)
print("La somma è: ", somma(lista))
print("La media è: ", media(lista))