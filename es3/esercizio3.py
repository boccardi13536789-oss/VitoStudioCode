'''Gestire una lista della spesa con python'''

lista=["pane","pasta"]
#funzione per definire la lista della spesa
def aggiungi_prodotto(lista):
    prodotto=input ("inserisci prodotto: ")
    lista.append(prodotto)
    return lista

#funzione per visualizzare la lista
def visualizza_lista(lista):
    print("Lista della spesa:", lista)
    return lista

#funzione per rimuovere il prodotto dalla lista
def rimuovi_prodotto(lista):
    prodotto = input("Quale prodotto vuoi rimuovere? ")
    if prodotto in lista:
        lista.remove(prodotto)
        print("Prodotto rimosso!")
    else:
        print("Prodotto non trovato.")
    return lista
    
#faccio un while per far inserire i prodotti finchè l'utente non decide di smettere
while True:
    print("1. Aggiungi prodotto")
    print("2. Visualizza lista")
    print("3. Rimuovi prodotto")
    print("4. Esci")

    scelta = input("Scegli un'opzione: ")
    if scelta == "1": 
        lista = aggiungi_prodotto(lista)
    elif scelta == "2":
        visualizza_lista(lista)
    elif scelta == "3":
        lista = rimuovi_prodotto(lista)
    elif scelta == "4":
        break
    else:
        print("Opzione non valida.")