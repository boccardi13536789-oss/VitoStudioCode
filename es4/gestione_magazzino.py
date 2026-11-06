# Inizializziamo il magazzino
lista_magazzino = [
    ["mangime cavalli", 15, 23, 5],
    ["mangime galline", 8, 15, 5],
    ["mangime polli", 8, 15, 5],
    ["mangime mucche", 20, 26, 5],
    ["mangime vitelli", 18, 24, 5],
    ["mangime conigli", 7, 13, 5]
]

# Creiamo la variabile per il totale del denaro (il conto economico del magazzino)
prezzo_totale = 1000 

# funzione per visualizzare lo stato del magazzino
def visualizza_magazzino(lista_magazzino):
    print("STATO DEL MAGAZZINO")
    for i, articolo in enumerate(lista_magazzino):
        nome, prezzo_acquisto, prezzo_vendita, quantita = articolo
        print(f"{i}. Prodotto: {nome} | Prezzo d' acquisto: {prezzo_acquisto}€ | Prezzo di vendita: {prezzo_vendita}€| Quantità: {quantita}")

# funzione per caricare un prodotto nel magazzino
def carica_prodotto(lista_magazzino, nome, quantita_acquistata, prezzo_totale):
    # Cerchiamo il prodotto nella lista per aggiornare i dati
    for articolo in lista_magazzino:
        if articolo[0] == nome:
            prezzo_acquisto = articolo[1]
            prezzo_uscita = prezzo_acquisto * quantita_acquistata
            prezzo_totale = prezzo_totale - prezzo_uscita
            articolo[3] = articolo[3] + quantita_acquistata # Aggiorna la quantità interna alla lista
            print(f"Hai speso {prezzo_uscita}€")
    return prezzo_totale

# funzione per vendere un prodotto dal magazzino
def vendi_prodotto(lista_magazzino, nome, quantita_venduta, prezzo_totale):
    # Cerchiamo il prodotto nella lista per aggiornare i dati
    for articolo in lista_magazzino:
        if articolo[0] == nome:
            prezzo_vendita = articolo[2]
            prezzo_entrata = prezzo_vendita * quantita_venduta
            prezzo_totale = prezzo_totale + prezzo_entrata
            articolo[3] = articolo[3] - quantita_venduta # Aggiorna la quantità interna alla lista
            print(f"Hai incassato {prezzo_entrata}€")
    return prezzo_totale

# funzione per visualizzare il totale del magazzino
def visualizza_totale_magazzino(lista_magazzino):
    totale = 0
    for articolo in lista_magazzino:
        nome, prezzo_acquisto, prezzo_vendita, quantita = articolo
        totale += prezzo_vendita * quantita
    print(f"Il totale del magazzino è: {totale}€")

# faccio un ciclo while per far scegliere all'utente cosa fare
while True:
    print(f"\nDenaro disponibile: {prezzo_totale}€")
    print("Cosa vuoi fare?")
    print("1. Visualizza lo stato del magazzino")
    print("2. Carica un prodotto nel magazzino")
    print("3. Vendi un prodotto dal magazzino")
    print("4. Visualizza il totale del magazzino")
    print("5. Esci")
    scelta = int(input("Inserisci il numero della tua scelta: "))
    
    if scelta == 1:
        visualizza_magazzino(lista_magazzino)
    elif scelta == 2:
        nome = input("Inserisci il nome del prodotto da caricare: ")
        quantita = int(input("Inserisci la quantità da caricare: "))
        prezzo_totale = carica_prodotto(lista_magazzino, nome, quantita, prezzo_totale)
    elif scelta == 3:
        nome = input("Inserisci il nome del prodotto da vendere: ")
        quantita = int(input("Inserisci la quantità da vendere: "))
        prezzo_totale = vendi_prodotto(lista_magazzino, nome, quantita, prezzo_totale)
    elif scelta == 4:
        visualizza_totale_magazzino(lista_magazzino)
    elif scelta == 5:
        break
    else:
        print("Scelta non valida, riprova.")