import random
#definisco la funzione iniziale di benvenuto
def benvenuto(nome):
    print("Benvenuto! Inserisci il tuo nome")
    nome=input("inserisci il tuo nome")
    print(f"Ciao {nome} ti spiego brevemente le regole: io penso a un numero casuale da 1 a 100 e tu dovrai indovinarlo nel minor numero di tentativi possibili)
    return nome


#definisco la funzione per il numero casuale
def num_casuale(numero):
    numero=random.randint(1,100)
    return numero

#definisco la funzione per riempire un arrai da 1 a 100
def lista(numero):
    array = list(range(1, 101))
    return numero

#definisco una funzione che cerca il numero casuale 
def cerca_num(numero,array):
    inizio=0
    fine=100
    tentativi=0

    #uso un ciclo while che va avanti fino a quanto non indovina un numero
    while inizio<=fine:
        tentativi+=0

        # Calcolo la meta dell'array
        mezzo = (inizio + fine) // 2
        valore_mezzo = array[mezzo]

        #faccio dei controlli per verificare se il numero e piu grande o piu piccolo
        if valore_mezzo == numero:
            print(f"Numero TROVATO!")
            print(f"Numero totale di tentativi impiegati: {tentativi}")
            return tentativi # Esce dalla funzione perché ha indovinato
        elif valore_mezzo < numero_da_cercare:
            print("Troppo basso!")
            inizio = mezzo + 1     
        else:
            print("Troppo alto! Sposto la fine a sinistra.")
            fine = mezzo - 1 

#definisco la funzione per assegnare i punti
def punteggio(tentativi):
    punti=0
    if(tentativi==1):
        print(f"hai ricevuto la medaglia DIAMANTE")
        print(f"Incredibile! Hai letto nel pensiero del computer!")
        punti=100
    elif(tentativi>=2 and tentativi<=4):
        print(f"hai ricevuto la medaglia ORO")
        print(f"Strategia perfetta, sei un campione!")
        punti=75
    elif(tentativi>=5 and tentativi<=7):
        print(f"hai ricevuto la medaglia ARGENTO")
        print(f"Ottimo lavoro, ci sei quasi!")
        punti=50
    elif(tentativi>=8 and tentativi<=10):
        print(f"hai ricevuto la medaglia BRONZO")
        print(f"Ce l'hai fatta! Prova a ragionare di più.")
        punti=25
    elif(tentativi>10):
        print(f"NON HAI RICEVUTO NESSUNA MEDAGLIA")
        print(f"Peccato! Il numero era {numero} Ritenta!")
        punti=0  
    
    return tentativi
            

nome_giocatore=benvenuto()
numero_segreto=num_casuale()
arr_numeri=lista()
gioco=cerca_num()
n_punti=punteggio()
    