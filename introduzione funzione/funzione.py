#importo una classe che genera un numero casuale
import random

#definisco come si chiama la funzione, poi definisco cosa gli serve e poi restituirà la somma

def boccardi_somma(num1,num2):
    return num1+num2
#funzione per la sottrazione
def boccardi_sottrazione(num1,num2):
    return num1-num2
#funzione per la moltiplicazione
def boccardi_moltiplicazione(num1,num2):
    return num1*num2
#funzione per la divisione
def boccardi_divisione(num1,num2):
    if (num2!=0):
        return num1/num2
    return "Errore"
    
#generare un numero qualsiasi intero che va da -999 a +999
numero1=random.randint(-999,999)
numero2=random.randint(-999,999)

#risultato
print(numero1)
print(numero2)

print(f"la somma di{numero1} e di {numero2} è di {boccardi_somma(numero1,numero2)}")
print(f"la sottrazione di{numero1} e di {numero2} è di {boccardi_sottrazione(numero1,numero2)}")
print(f"la moltiplicazione di{numero1} e di {numero2} è di {boccardi_moltiplicazione(numero1,numero2)}")
print(f"la divisione di{numero1} e di {numero2} è di {boccardi_divisione(numero1,numero2)}")