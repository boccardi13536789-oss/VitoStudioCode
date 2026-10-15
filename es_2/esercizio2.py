'''Scrivi un programma che chieda all’utente di inserire una frase (o un breve testo) e poi fornisca alcune informazioni:
numero di caratteri totali
numero di lettere, cifre e altri caratteri
numero di parole (parole separate da spazi)
numero di vocali e consonanti (solo per le lettere)
la parola più lunga e la parola più corta'''

#importo la classe string per inserire la stringa
import string

#funzione per chiedere all'utente di inserire un testo
def chiedi_testo():
    print ("inserisci una frase o un breve testo")
    return input();

# funsione per calcolare i caratteri del testo
def numero_caratteriTot(testo):
    return len(testo)

#funzione per calcolare il numero di lettere, cifre e caratteri
def numero_caratteriSpec(testo):
   lettere=0
   cifre=0
   altri=0
   for c in testo:
    if c.isalpha():
        lettere+=1
    elif c.isdigit():
        cifre+=1
    else:
        altri+=1 
    return lettere, cifre, altri

#funzione per calcolare il numero di parole
def numero_parole(testo):
    parole = testo.split()
    return len(parole)

#funzione per calcolare il numero di vocali e di consonanti
def numero_vocali_consonanti(testo):
    vocali_set = "aeiouAEIOUàèéìòù"
    num_vocali = 0
    num_consonanti = 0
    
    for c in testo:
        if c.isalpha():
            if c in vocali_set:
                num_vocali += 1
            else:
                num_consonanti += 1
                
    return num_vocali, num_consonanti 

#funzione per trovare la parola piu lunga e la piu corta   
def parola_Lunga_corta (testo):
    parola_lunga = parole[0]
    parola_corta = parole[0]
    
    # Controlliamo tutte le altre parole una per una
    for p in parole:
        if len(p) > len(parola_lunga):
            parola_lunga = p
        if len(p) < len(parola_corta):
            parola_corta = p
            
    return parola_lunga, parola_corta

#richiamo le funzioni
tot_caratteri = numero_caratteriTot(testo)
lettere, cifre, altri = numero_caratteriSpec(testo)
n_parole = numero_parole(testo)
vocali, consonanti = numero_vocali_consonanti(testo)
piu_lunga, piu_corta = parola_Lunga_corta(testo)
    
# Stampa dei risultati
print(f"* Caratteri totali: {tot_caratteri}")
print(f"* Lettere: {lettere} | Cifre: {cifre} | Altri caratteri: {altri}")
print(f"* Numero di parole: {n_parole}")
print(f"* Vocali: {vocali} | Consonanti: {consonanti}")
print(f"* Parola più lunga: '{piu_lunga}'")
print(f"* Parola più corta: '{piu_corta}'")