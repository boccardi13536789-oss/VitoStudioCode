#questa è una lista vuota
lista=[] 
#questa è una lista inizializzata
lista=[1, 2.5,"tre", [5,"sei"]]
print(lista)

for elementochevoglio in lista:
    print(elementochevoglio)

#come fare un for in python
for indice in range(1,10,2):
    print(indice)

    i=0
    while (i<10):
        print("sto facendo qualcosa")
        i+=1

#do while in python non esiste, ma si può fare così:
i=0
while True:
    print("silenzio")
    if (i>1):
        break
    else:
        i+=1    