#!/usr/bin/env python
# coding: utf-8

# # Introduzione a python

# In[12]:


print("Hello world!")


# In[1]:


nome=input("inserisci il tuo nome ") 

for i in range(10):
    print(nome)


# In[8]:


for numero in range(1,11):
    print(numero)


# In[2]:


numero1 = int(input("inserisci il primo numero:"))
numero2 = int(input("inserisci il secondo numero:"))
somma = numero1 + numero2
print("La somma è:", somma)


# In[3]:


sottrazione = numero1 - numero2
print("La differenza è:", sottrazione)


# In[6]:


numero1 = int(input("inserisci il primo numero:"))
numero2 = int(input("inserisci il secondo numero:"))
prodotto = numero1 * numero2
print("La prodotto è:", prodotto)


# In[7]:


divisione = numero1 / numero2
print("La divisione è:", int(divisione))


# In[9]:


operazione = input("Inserisci l'operazione (+,-,*,/): ")

numero1 = float(input("Inserisci il primo numero: "))
numero2 = float(input("Inserisci il secondo numero: "))

if operazione == "+":
    risultato = numero1 + numero2
elif operazione == "-":
    risultato = numero1 - numero2
elif operazione == "*":
    risultato = numero1 * numero2
elif operazione == "/":
    risultato = numero1 / numero2
else:
    risultato = "Operazione non valida"
    
print("Il risultato è:", risultato)


# In[10]:


n = int(input("Inserisci un numero intero positivo: "))
somma = 0

for numero in range(1, n+1 ):
    somma += numero
print("La somma dei primi",n, "numeri interi è",somma)


# In[10]:


N = int(input("Inserisci un numero intero positivo N: "))

somma = 0

for numero in range(2, 2 * N + 1, 2):
    somma += numero
    
print(f"La somma dei primi {N} numeri pari è {somma}")


# In[11]:


n = int(input("Inserisci un numero intero positivo: "))

print("Quadrati dei primi", n,"numeri:")

for numero in range(1, n+1 ):

    quadrato = numero ** 2
    print("Il quadrato di", numero, "è", quadrato)


# In[3]:


numero = int(input("inserisci un numero: "))

if numero % 2 == 0:    # numero divisibile (%) per 2 con resto (==) di 0
    print(numero, "è un numero pari.")
else:
    print(numero, "è un numero dispari.")
    


# In[11]:


n = int(input("inserisci un numero intero positivo: "))
fattoriale = 1

for numero in range(1, n + 1):
    fattoriale = fattoriale*numero #1*2*3*4...
print("il fattoriale di", n, "è:", fattoriale)


# In[8]:


n=int(input("inserisci un numero intero: "))

fattoriale=1

if n<0:
    print("numero negativo")
elif n==0:
    print("il fattoriale è 1")
else:
    for numero in range(1,n+1):
        fattoriale*=numero
print(f"il fattoriale di {n} è {fattoriale}")


# In[16]:


numeri = [] #dizionario
n = int(input("Quanti numeri vuoi inserire? "))

for i in range(n):
    numero = float(input("inserisci un numero: "))
    numeri.append(numero)

media = sum(numeri) / len(numeri)

print("la media dei numeri inseriti è:", media, numeri)


# In[16]:


import random

numero_da_indovinare = random.randint(1, 100)
tentativi = 0

while True:
    tentativo = int(input("Indovina il numero (1-100): "))
    tentativi += 1
    
    if tentativo == numero_da_indovinare:
        print("Bravo! hai indovinato il numero", numero_da_indovinare, "in", tentativi, "tentativi")
        break
    elif tentativo < numero_da_indovinare:
        print("il numero è più grande")
    elif tentativo > numero_da_indovinare:
        print("il numero è più piccolo")


# In[12]:


import random

mosse = ["carta", "forbici", "sasso"]

computer_mossa = random.choice(mosse)

print("Benvenuti al gioco del morra cinese!")
scelta_giocatore = input("scegli la tua mossa (carta, forbici, sasso): ")

if scelta_giocatore not in mosse:
    print("mossa non permessa")
else:
    print("il computer ha scelto:", computer_mossa) 
    if scelta_giocatore == computer_mossa:
        print("pareggio!")
    elif (scelta_giocatore == "carta" and computer_mossa == "sasso") or \
            (scelta_giocatore == "forbici" and computer_mossa == "carta") or \
            (scelta_giocatore == "sasso" and computer_mossa == "forbici"):
             print("Hai vinto! ")
    else:
        print("Hai perso! ")
     


# In[16]:


N = int(input("Inserisci un numero intero positivo N: "))

lista=[]

for numero in range(2, 2 * N + 1, 2):
    lista.append(numero)
    
print(lista)


# In[18]:


frase = input("Inserisci una frase o una parola: ").lower() #.lower() mette tutto in minuscolo

conteggio_vocali = 0

vocali= "aeiou"

for carattere in frase:
    if carattere in vocali:
        conteggio_vocali += 1
        
print(f"Nella frase inserita ci sono {conteggio_vocali} vocali.")


# In[26]:


import random

numero_dado = random.randint(1, 6)

indovina = int(input("Indovina il numero del dado (da 1 a 6)"))
    
if indovina <1 or indovina >6:
    print("numero non ammesso")
elif indovina == numero_dado:
    print(f"Complimenti! Il numero del dado era {numero_dado}. Hai indovinato!")
else:
    print(f"Il numero del dado era {numero_dado}. Meglio la prossima volta")


# In[1]:


popolazione = int(input("Inserire popolazione iniziale: "))
anni = int(input("Inserisci numero di anni da simulare: "))

tasso_di_natalità = float(input("Inserisci tasso natalità: "))
tasso_di_mortalità = float(input("Inserisci tasso mortalità: "))

for anno in range(anni):
    nascite = (popolazione * tasso_di_natalità) / 100 
    morti = (popolazione * tasso_di_mortalità) / 100 #percentuale
    popolazione += (nascite - morti)
    
    print(f"Anno {anno+1}: Popolazione = {int(popolazione)}")
    
print("Simulazione completata. ")


# In[18]:


import datetime

today = datetime.datetime.today()
print(f"oggi è il giorno: {today:%d %m %Y} ore: {today:%H %M %S}")


# In[4]:


print("Benvenuto nel convertitore di unità di misura!")
scelta = input("Cosa desideri convertire? (metri/piedi/chilogrammi/libbre): ").lower()

if scelta == "metri":
    valore = float(input("Inserisci il valore in metri: "))
    risultato = valore * 3.28084
    print(f"{valore} metri corrispondono a {risultato} piedi")
elif scelta == "piedi":
    valore = float(input("Inserisci il valore in metri: "))
    risultato = valore * 3.28084
    print(f"{valore} piedi corrispondono a {risultato} metri")
elif scelta == "chilogrammi":
    valore = float(input("Inserisci il valore in metri: "))
    risultato = valore * 2.20462
    print(f"{valore} chilogrammi corrispondono a {risultato} libbre")
elif scelta == "libbre":
    valore = float(input("Inserisci il valore in metri: "))
    risultato = valore * 2.20462
    print(f"{valore} libbre corrispondono a {risultato} chilogrammi")
else:
    print("Scelta non valida. Scegli tra 'metri', 'piedi', 'chilogrammi' o 'libbre'.")


# In[ ]:


def metri_a_piedi(metri):
    return metri * 3.28084
def piedi_a_metri(piedi):
    return piedi / 3.28084
def chilogrammi_a_libbre(chilogrammo):
    return chilogrammi * 2.20462
def libbre_a_chilogrammi(libbre):
    return libbre / 2.20462

def selezione(scelta):
    if scelta == "metri":
        valore = float(input("Inserisci il valore in metri: "))
        risultato = metri_a_piedi(valore)
        print(f"{valore: .3f} metri corrispondono a {risultato} piedi")
    elif scelta == "piedi":
        valore = float(input("Inserisci il valore in piedi: "))
        risultato = piedi_a_metri(valore)
        print(f"{valore: .3f} piedi corrispondono a {risultato} metri")
    elif scelta == "piedi":
        valore = float(input("Inserisci il valore in piedi: "))
        risultato = chilogrammi_a_libbre(valore)
        print(f"{valore: .3f} chilogrammi corrispondono a {risultato} libbre")
    elif scelta == "piedi":
        valore = float(input("Inserisci il valore in piedi: "))
        risultato = libbre_a_chilogrammi(valore)
        print(f"{valore: .3f} libbre corrispondono a {risultato} chilogrammi")
    else:
        print("Sveglia!! Scelta non valida, Scegli tra 'metri', 'piedi', 'chilogrammi' o 'libbre'.")
        
def main():
    print("Benvenuto nel Convertitore di Unità di Misura!")
    scelta = input("Cosa desideri convertire? (metri/piedi/chilogrammi/libbre): ").lower()
    selezione(scelta)
if __name__ == "__main__":
    main()


# In[7]:


n = int(input("Inserisci un numero n p'er calcolare l'n-esimo numero di Fibonacci: "))

a=0
b=1
c=1
#il terzo numero è la somma dei primi 2
if n <= 0:
    print("Il numero deve essere maggiore di zero.")
elif n == 1:
    risultato = a
else:
    for iterazione in range(n-3):
        a = b
        b = c
        c = a + b
        risultato = c
print("L'n-esimo numero di Fibonacci è:", risultato)


# In[4]:


def fibonacci(n):
    fib_series = [0, 1]
    
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    
    return fib_series


# In[5]:


fibonacci(10)


# In[19]:


import math

def calcola_area_cerchio(raggio):
    return math.pi * (raggio ** 2)

def calcola_area_rettangolo(base, altezza):
    return base * altezza
def calcola_area_triangolo(base, altezza):
    return (base * altezza) / 2


# In[20]:


print("Benvenuto nella Calcolatrice di Aree!")

scelta = input("Vuoi calcolare l'area di u cerchio (c), rettangolo (r) p triangolo (t)? ").lower()

if scelta == 'c':
    raggio = float(input("Inserisci il raggio del cerchio: "))
    area = calcola_area_cerchio(raggio)
    print(f"L'area del cerchio è {area: .2f}")
elif scelta == 'r':
    base = float(input("Inserisci la base del rettangolo: "))
    altezza = float(input("Inserisci l'altezza del rettangolo: "))
    area = calcola_area_rettangolo(base, altezza)
    print(f"L'area del rettangolo è {area: .2f}")
elif scelta == 't':
    base = float(input("Inserisci la base del triangolo: "))
    altezza = float(input("Inserisci l'altezza del triangolo: "))
    area = calcola_area_triangolo(base, altezza)
    print(f"L'area del tringolo è {area: .2f}")
else:
    print("scelta non valida.")


# In[7]:


def calcola_interessi(importo_inziale, tasso_interesse, periodi_investimento):
    importo_finale = importo_iniziale * (1 + tasso_interesse / 100) ** periodi_investimento
    return importo_finale


# In[5]:


print("Benvenuto nel calcolatore di interessi!")

importo_iniziale = float(input("Inserisci l'importo iniziale: "))
tasso_interesse = float(input("Inserisci il tasso di interesse annuale (%): "))
periodi_investimento = float(input("Inserisci il periodo di investimento (anni): "))

importo_finale = calcola_interessi(importo_iniziale, tasso_interesse, periodi_investimento)

print(f"L'importo finale dopo {periodi_investimento} anni è di {importo_finale:.2f} euro.")


# In[9]:


calcola_interessi(100000,4,10)


# In[10]:


def forza_gravitazionale(m1, m2, r):
    # Costante gravitazizonale
    G = 6.67430e-11 #N(m/kg)^2
    
    # Calcolo della forza gravitazionale
    F = (G * m1 * m2) / (r ** 2)
    
    return F


# In[11]:


massa_terra = 5.972e24 # kg
massa_luna = 7.342e22 # kg
distanza_terra_luna = 384400000 # metri

forza = forza_gravitazionale(massa_terra, massa_luna, distanza_terra_luna)
print(f"Forza gravitazionale tra la Terra la Luna: {forza} Newton")


# In[1]:


from itertools import permutations
k=0

def trova_anagrammi(parola):
    anagrammi =  [''.join(p) for p in permutations(parola)]
    return anagrammi
    
print("Benvenuto nel Risolutore di Anagrammi!")
parola_input = input("Inserisci una parola: ").strip().lower() # .strip() cancella gli spazi bianchi

if len(parola_input) < 2:
    print("Inserisci una parola con almeno 2 caratteri.")
else:
    anagrammi = trova_anagrammi(parola_input)
    
    for anagramma in anagrammi:
        if anagramma != parola_input: # != significa diverso
            k+=1
            print(anagramma)
    print(f"Gli anagrammi di '{parola_input}' sono:'{k}'")


# In[10]:


# definizione dei tassi di cambio
tassi_di_cambio = {
    "dollari": 1.0,
    "euro": 0.85,
    "yen": 110.41,
    # aggiungi altre valute e tassi di cambio se necessario
}

# Chiedi all'utente di inserire l'importo, la valuta di partenza e la valuta di destinazione
importo = float(input("Inserisci l'importo da convertire: "))
valuta_di_partenza = input("Inserisci la valuta di partenza: ")
valuta_destinazione = input("Inserisci la valuta di destinazione: ")

# Verifica se le valute sono nel dizionario dei tassi di cambio
if valuta_di_partenza in tassi_di_cambio and valuta_destinazione in tassi_di_cambio:
    # Calcola il tasso di cambio e l'importo convertito
    tasso_di_cambio = tassi_di_cambio[valuta_destinazione] / tassi_di_cambio[valuta_di_partenza]
    importo_convertito = importo * tasso_di_cambio
    
    print(f"{importo} {valuta_di_partenza} sono equivalenti a {importo_convertito:.2f} {valuta_destinazione}")
else:
    print("Valute non supportate. Assicurati di inserire valute valide")
    


# In[1]:


frase = input("inserisci una frase: ")

frase = frase.lower()

alfabeto = 'abcdefghijklmnopqrstuvwxyz'

conteggio_lettere = {} #dizionario

for lettera in alfabeto:
    conteggio = frase.count(lettera) 
    
    if conteggio > 0:
        conteggio_lettere[lettera] = conteggio  
        
#stampa il conteggio in un formato leggibile
for lettera, conteggio in conteggio_lettere.items():
    print(f"{lettera}: {conteggio}")


# In[14]:


conteggio_lettere.items()


# In[4]:


prodotti={}
prodotti["pan bauletto"]=2
prodotti["coca cola"]=3


# In[1]:


from datetime import datetime
import pytz

print("Benvenuto nell'Orologio Mondiale!")

#Definisci le città e i relativi fusi orari
citta_fusi_orari = {
    "New York": "America/New_York",
    "Londra": "Europe/London",
    "Tokyo": "Asia/Tokyo",
    "Sydney": "Australia/Sydney",
    "Rio de Janeiro": "America/Sao_Paulo",
}

while True:
    print("\nCittà disponibili:")
    for citta in citta_fusi_orari.keys():
        print(citta)

    scelta_citta = input("Inserisci il nome della città per visualizzare l'ora (o 'esci' per uscire): ").strip()
    if scelta_citta.lower() == 'esci':
        break

    if scelta_citta in citta_fusi_orari.keys():
        fuso_orario = pytz.timezone(citta_fusi_orari[scelta_citta])
        ora_corrente = datetime.now(fuso_orario)
        print(f"L'ora corrente a {scelta_citta} è: {ora_corrente.strftime('%H:%M:%S')}")
    else:
        print("Città non valida. Riprova.")


# In[2]:


def davide():
    print("mi chiamo davide")
    
if __name__== "__main__":
    
    davide ()


# In[7]:


def calcola_bmi(peso, altezza):
    return peso / (altezza ** 2)

def valuta_bmi(bmi):
    if bmi < 18.5:
        return "Sottopeso"
    elif 18.5 <= 24.9:
        return "Normopeso"
    elif 25 <= bmi < 24.9:
        return "sovrappeso"
    else:
        return "Obeso"
    
def main():
    print("Benvenuto nella calcolatrice BMI!")
    peso = float(input("Inserisci il tuo peso in chilogrammi: "))
    altezza = float(input("Inserisci la tua altezza in metri: "))
    
    bmi = calcola_bmi(peso,altezza)
    valutazione = valuta_bmi(bmi)
    
    print(f"Il tuo BMI è {bmi:.2f}, sei classificato come '{valutazione}'.")
    
if __name__ == "__main__":
    main()


# In[11]:


cibo_calorie = {
    "pizza": 285,
    "hamburger": 250,
    "insalata": 200,
    "pollo arrosto": 335,
    "yogurt": 150,
}

def calorie_consumate(cibo, quantità):
    if cibo not in cibo_calorie.keys():
        print("cibo non presente")
    elif cibo in cibo_calorie.keys():
        calorie_per_100g = cibo_calorie[cibo]
        calorie_totali = (calorie_per_100g / 100) * quantità 
        return calorie_totali
def main():
    cibo_consumato = []
    
    
    while True:
        print("Menu")
        print("\n 1. Aggiungi cibo consumato")
        print("\n 2. Calcola calorie totali")
        print("\n 3. Esci")
        
        scelta = input("Scegli un'opzione: ")
        
        if scelta == "1":
            print("\n")
            
            for key, value in cibo_calorie.items() :
                print (key, value)
                
            cibo = input("Inserisci il cibo consumato: ").lower()
            quantità = float(input("Inserisci la quantità (in grammi): "))
            cibo_consumato.append((cibo,quantità))
        elif scelta == "2":
            calorie_totali = sum(calorie_consumate(c, g) for c, g in cibo_consumato)
            print(f"\n Calorie totali consumate: {calorie_totali} calorie")
        elif scelta == "3":
            break
        else:
            print("\n Scelta non valida. Riprova.")
            
if __name__ == "__main__":
    main()


# In[5]:


acquisti={}
acquisti["pan bauletto"]=10
acquisti["nutella"]=10


# In[9]:


acquistidue={
    "pan bauletto":10,
    "nutella":10,
}


# In[10]:


acquistidue


# In[5]:


import random

speci = ["Elfo", "Umano", "Nano", "Orco", "Gnomo"]
classi = ["Guerriero", "Mago", "Ranger", "Ladro", "Chierico"]
armi = ["Spada", "Arco", "Bacchetta magica", "Ascia", "Daga"]
abilità = ["Furtività", "Magia dell'acqua", "Camuffamento", "Estrazione mineraria", "Incantesimi di guarigione"]

specie = random.choice(speci)
classe = random.choice(classi)
arma = random.choice(armi)
abilità_scelte = random.sample(abilità, random.randint(1, 3))

print(f"Personaggio Fantasy Generato:")
print(f"Specie: {specie}")
print(f"Classe: {classe}")
print(f"Arma: {arma}")
print(f"Abilità: {', '.join(abilità_scelte)}")


# In[13]:


import random

speci = ["Elfo", "Umano", "Nano", "Orco", "Gnomo"]
classi = ["Guerriero", "Mago", "Ranger", "Ladro", "Chierico"]
armi = ["Spada", "Arco", "Bacchetta magica", "Ascia", "Daga"]
abilità = ["Furtività", "Magia dell'acqua", "Camuffamento", "Estrazione mineraria", "Incantesimi di guarigione"]

def crea_personaggio():
    return {
        "Specie": random.choice(speci),
        "Classe": random.choice(classi),
        "Arma": random.choice(armi),
        "Abilità": random.sample(abilità, random.randint(1, 3))
    }

def main():
    personaggio_generato = crea_personaggio()

    print("Personaggio Fantasy Generato:")
    for chiave, valore in personaggio_generato.items():
        if chiave == "Abilità":
            valore = ', '.join(valore)
        print(f"{chiave}: {valore}")

if __name__ == "__main__":
    main()


# In[24]:


import random

speci = ["Elfo", "Umano", "Nano", "Orco", "Gnomo"]
classi = ["Guerriero", "Mago", "Ranger", "Ladro", "Chierico"]
armi = ["Spada", "Arco", "Bacchetta magica", "Ascia", "Daga"]
abilità = ["Furtività", "Magia dell'acqua", "Camuffamento", "Estrazione mineraria", "Incantesimi di guarigione"]

def crea_personaggio():
    return {
        "Specie": random.choice(speci),
        "Classe": random.choice(classi),
        "Arma": random.choice(armi),
        "Abilità": random.sample(abilità, random.randint(1, 3))
    }

def main():
    personaggio_generato = crea_personaggio()

    print("Personaggio Fantasy Generato:")
    for chiave, valore in personaggio_generato.items():
        if chiave == "Abilità":
            valore = ', '.join(valore)
        print(f"{chiave}: {valore}")

if __name__ == "__main__":
    main()


# In[1]:


import random

citazioni = [
    "La vita è ciò che succede mentre sei occupato a fare altri progetti. - John Lennon",
    "Il successo è camminare da un fallimento all'altro senza perdere l'entusiasmo. - Winston Churchill",
    "La felicità  è quando ciò che pensi, ciò che dici e ciò che fai sono in armonia. - Mahatma Gadhi",
    "La vota è davvero semplice, ma insistiamo. - Confucio",
    "La vota è ciò che succede mentre sei occupato a fare altri progetti. - Steve Jobs",
    "La vota è ciò che succede mentre sei occupato a fare altri progetti. - Charles R. Swindoll"
]

def genera_citazione():
    return random.choice(citazioni)

def main():
    print("Benvenuto nel Generatore di Citazioni")
    input("Premi Invio per ottenere una citazione casuale...")
    
    citazione = genera_citazione()
    print(f"Citazione del giorno: {citazione}")

if __name__ == "__main__":
    main()


# In[49]:


import random

citazioni = [
    "Non smettere mai di inseguire i tuoi sogni.",
    "I sogni sono le stelle che guidano la tua vita.",
    "La strada verso il successo è pavimentata con i sogni che inseguimo.",
    "I tuoi sogni sono la bussola della tua anima.",
    "I sogni sono le ali con cui voliamo verso il futuro.",
    "Ogni sogno è un passo avanti verso la realizzazione.",
    "I sogni sono la linfa vitale dell'ispirazione.",
    "Nessun sogno è troppo grande se hai il coraggio di inseguirlo.",
    "I sogni sono la forza che ci spinge ad andare avanti.",
    "Inseguire i tuoi sogni ti porta verso il miglioramento personale.",
    "I sogni sono la luce che illumina il cammino della vita.",
    "La determinazione è la chiave per inseguire i tuoi sogni.",
    "Ogni passo avanti è un passo verso i tuoi sogni.",
    "La perseveranza è la virtù di chi insegue i propri sogni.",
    "I tuoi sogni sono il tuo destino.",
    "I sogni sono il carburante della creatività.",
    "La vita è un viaggio, i sogni sono la destinazione.",
    "Nessun sogno è mai troppo lontano per essere raggiunto.",
    "I sogni sono i colori della tua vita.",
    "Inseguire i tuoi sogni è come danzare con il destino.",
    "I sogni sono le radici dei tuoi obiettivi.",
    "La passione è il motore che alimenta i tuoi sogni.",
    "Ogni giorno è un'opportunità per avvicinarti ai tuoi sogni.",
    "I tuoi sogni sono la musica della tua esistenza.",
    "Inseguire i tuoi sogni è il segreto della felicità.",
    "La determinazione trasforma i sogni in realtà.",
    "I sogni sono le perle della tua corona personale.",
    "Niente è impossibile quando inseguite i vostri sogni.",
    "I sogni sono la risposta alle domande della tua anima.",
    "Inseguire i tuoi sogni ti rende un costruttore di storie di successo.",
    "I sogni sono il ritmo della tua vita.",
    "Ogni giorno è un capitolo nel libro dei tuoi sogni.",
    "La vita è un regalo, i sogni sono il tuo dono al mondo.",
    "I tuoi sogni sono la radice della tua forza interiore.",
    "Inseguire i tuoi sogni è il segreto per vivere una vita significativa.",
    "I sogni sono le ali che ti sollevano al di sopra delle sfide.",
    "Niente è fuori portata quando segui i tuoi sogni con passione.",
    "Inseguire i tuoi sogni è il modo migliore per scoprire chi sei veramente.",
    "I sogni sono il tuo faro nella tempesta della vita.",
    "La determinazione è la spinta che ti fa progredire verso i tuoi sogni.",
    "I tuoi sogni sono il tesoro nascosto nel tuo cuore.",
    "Inseguire i tuoi sogni è la chiave per una vita appagante."
]

def crea_citazione():
    num_frammenti = random.randint(4, 7)
    citazione_rimescolata = random.sample(citazioni, num_frammenti)
    nuova_citazione = " ".join(citazione_rimescolata)
    return nuova_citazione

def main():
    nuova_citazione = crea_citazione()
    print("Nuova citazione generata:")
    print(nuova_citazione)

if __name__ == "__main__":
    main()


# In[7]:


aggettivi = ["dolce", "sereno", "profondo", "luminoso", "gentile"]
sostantivi = ["amore", "mare", "cielo", "vento", "sogno"]
verbi = ["danza", "splende", "abbraccia", "canta", "sorride"]

def genera_poesia():
    verso1 = f"Il {random.choice(aggettivi)} {random.choice(sostantivi)} {random.choice(verbi)}."
    verso2 = f"Il {random.choice(aggettivi)} {random.choice(sostantivi)} {random.choice(verbi)}."
    verso3 = f"Nel {random.choice(sostantivi)} {random.choice(verbi)} con {random.choice(aggettivi)} {random.choice(sostantivi)}."
    
    return f"{verso1}\n{verso2}\n{verso3}"

print(genera_poesia())


# # Esercitazione python

# In[1]:


pip install plotly


# In[2]:


pip install seaborn


# In[4]:


pip install nbmerge


# In[5]:


import pandas as pd

# Dataset con dati mancanti rappresentati da None o NaN
dataset = [
    {"età": 25, "punteggio": 90, "ammesso": 1},
    {"età": None, "punteggio": 85, "ammesso": 0},
    {"età": 28, "punteggio": None, "ammesso": 1},
    {"età": None, "punteggio": 75, "ammesso": 1},
    {"età": 23, "punteggio": None, "ammesso": None},
    {"età": 23, "punteggio": 77, "ammesso": None},
]
df = pd.DataFrame(dataset)
df


# In[6]:


import pandas as pd

# Dataset con dati mancanti rappresentati da None o NaN
dataset = [
    {"nome": "Alice", "età": 25, "punteggio": 90, "email": "alice@email.com"},
    {"nome": "Bob", "età": 22, "punteggio": None, "email": None},
    {"nome": "Charlie", "età": 28, "punteggio": 75, "email": "charlie@email.com"},
]

# Converti il dataset in un DataFrame
df = pd.DataFrame(dataset)
df


# In[7]:


import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Genera dati di esempio
data = {
    'Variable1': [1, 2, 3, 4, 5],
    'Variable2': [1, 2, np.nan, 4, np.nan],
    'Missing_Column': ['A', 'B', 'A', 'C', np.nan]
}
# Crea un DataFrame
df = pd.DataFrame(data)
df1=pd.DataFrame()


# In[8]:


import pandas as pd

# Dataset con dati mancanti rappresentati da None o NaN
dataset = [
    {"età": 25, "punteggio": 90, "ammesso": 1},
    {"età": None, "punteggio": 85, "ammesso": 0},
    {"età": 28, "punteggio": None, "ammesso": 1},
    {"età": None, "punteggio": 75, "ammesso": 1},
    {"età": 23, "punteggio": None, "ammesso": None},
    {"età": 23, "punteggio": 77, "ammesso": None},
]
df = pd.DataFrame(dataset)
df


# In[9]:


import pandas as pd

# Dataset con dati mancanti rappresentati da None o NaN
dataset = [
    {"nome": "Alice", "età": 25, "punteggio": 90, "email": "alice@email.com"},
    {"nome": "Bob", "età": 22, "punteggio": None, "email": None},
    {"nome": "Charlie", "età": 28, "punteggio": 75, "email": "charlie@email.com"},
]

# Converti il dataset in un DataFrame
df = pd.DataFrame(dataset)
df


# In[10]:


import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Genera dati di esempio
data = {
    'Variable1': [1, 2, 3, 4, 5],
    'Variable2': [1, 2, np.nan, 4, np.nan],
    'Missing_Column': ['A', 'B', 'A', 'C', np.nan]
}
# Crea un DataFrame
df = pd.DataFrame(data)
df1=pd.DataFrame()
df


# In[12]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Genera dati di esempio
data = {
    'Feature1': [1, 2, np.nan, 4, 5],
    'Feature2': [np.nan, 2, 3, 4, np.nan],
    'Feature3': [1, np.nan, 3, 4, 5]
}
# Crea un DataFrame
df = pd.DataFrame(data)
df


# In[ ]:





# In[13]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Genera dati casuali per l'esplorazione
np.random.seed(42)
data = {
    'Età': np.random.randint(18, 70, size=1000),
    'Genere': np.random.choice(['Maschio', 'Femmina'], size=1000),
    'Punteggio': np.random.uniform(0, 100, size=1000),
    'Reddito': np.random.normal(50000, 15000, size=1000)
}

df = pd.DataFrame(data)

# Visualizza le prime righe del dataset
print(df.head())


# In[15]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Genera dati di esempio
data = {
    'Feature1': [1, 2, np.nan, 4, 5],
    'Feature2': [np.nan, 2, 3, 4, np.nan],
    'Feature3': [1, np.nan, 3, 4, 5]
}

# Crea un DataFrame
df = pd.DataFrame(data)

# Calcola la matrice di missing values
missing_matrix = df.isnull()
missing_matrix


# In[27]:


plt.figure(figsize=(8, 6))
sns.heatmap(missing_matrix, cmap='viridis', cbar=False,alpha=0.8)
plt.title('Matrice di missing values')
plt.show()


# In[17]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Genera dati casuali per l'esplorazione
np.random.seed(2)
data = {
    'Età': np.random.randint(18, 70, size=1000),
    'Genere': np.random.choice(['Maschio', 'Femmina'], size=1000),
    'Punteggio': np.random.uniform(0, 100, size=1000),
    'Reddito': np.random.normal(50000, 15000, size=1000)
}

df = pd.DataFrame(data)

# Visualizza le prime righe del dataset
print(df.head())

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Genera dati di esempio
data = {
    'Feature1': [1, 2, np.nan, 4, 5],
    'Feature2': [np.nan, 2, 3, 4, np.nan],
    'Feature3': [1, np.nan, 3, 4, 5]
}

# Crea un DataFrame
df = pd.DataFrame(data)

# Calcola la matrice di missing values
missing_matrix = df.isnull()
missing_matrix


# In[30]:


numeric_features = df.select_dtypes(include=[np.number])
sns.pairplot(df[numeric_features.columns])
plt.title('Matrice di Scatter Plot tra variabili numeriche')
plt.show()


# In[18]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Genera dati di esempio
data = {
    'Numeric_Var': [1, 2, 3, 4, np.nan, 6],
    'Categorical_Var': ['A', 'B', 'A', 'B', 'A', 'B']
}

# Crea un DataFrame
df = pd.DataFrame(data)
print(df)


# In[19]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Genera dati casuali per l'esplorazione
np.random.seed(42)
data = {
    'Età': np.random.randint(18, 65, size=500),
    'Soddisfazione': 
    np.random.choice(['Molto Soddisfatto', 'Soddisfatto', 'Neutro', 'Insoddisfatto', 'Molto Insoddisfatto'], size=500)
}

df = pd.DataFrame(data)
print(df)
conditional_means = df.groupby('Soddisfazione')['Età'].transform('mean')

df['Numeric_Var'] = conditional_means
print(df)

# Crea un grafico a barre per mostrare la media condizionata per ogni categoria
plt.figure(figsize=(8, 6))
sns.barplot(data=df, x='Soddisfazione', y='Numeric_Var', ci=None)
plt.xlabel('Soddisfazione')
plt.ylabel('Media Condizionata di Numeric_Var')
plt.title('Media Condizionata delle Variabili Numeriche per Categoria')
plt.xticks(rotation=90)

plt.show()


# In[20]:


# Visualizza le prime righe del dataset
print(df.head())

# Visualizza una distribuzione dell'età
plt.figure(figsize=(10, 6))
sns.histplot(df['Età'], bins=50, kde=True)
plt.title('Distribuzione dell\'età dei partecipanti al sondaggio')
plt.xlabel('Età')
plt.ylabel('Conteggio')
plt.show()

# Visualizza un conteggio delle risposte sulla soddisfazione
plt.figure(figsize=(8, 6))
sns.countplot(x='Soddisfazione', data=df, order=['Molto Soddisfatto', 'Soddisfatto', 'Neutro', 'Insoddisfatto', 'Molto Insoddisfatto'])
plt.title('Conteggio delle risposte sulla soddisfazione')
plt.xlabel('Soddisfazione')
plt.ylabel('Conteggio')
plt.xticks(rotation=45)
plt.show()


# In[34]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Specifica il percorso del tuo file CSV
percorso_file_csv = "C:\\Users\\davide\\OneDrive\\Desktop\\robotica\\pokemons.csv"

# Leggi il file CSV in un DataFrame
df = pd.read_csv(percorso_file_csv)

# Mostra le prime righe del DataFrame (opzionale)
print(df.head())
df.shape


# In[38]:


import os
import pandas as pd

#Specifica il percorso della cartella contenente i file CSV
percorso_cartella = 'C:\Users\davide\OneDrive\Desktop\robotica\serieAnuovo'

#Lista per memorizzare tutti i DataFrame letti dai file CSV
lista_dataframes = []

#Scansiona la cartella e leggi i file CSV
for nome_file in os.listdir(percorso_cartella):
    if nome_file.endswith(".csv"):
        percorso_file_csv = os.path.join(percorso_cartella, nome_file)
        df = pd.read_csv(percorso_file_csv)
        lista_dataframes.append(df)

#Ora lista_dataframes contiene tutti i DataFrame letti dai file CSV nella cartella


# In[39]:


#importa xlsx con fogli 
import pandas as pd

# Specifica il percorso del tuo file Excel
percorso_file_excel = "C:\\Users\\davide\\OneDrive\\Desktop\\robotica\\serieA.xlsx"

# Leggi il file Excel in un DataFrame

df = pd.read_excel(percorso_file_excel, sheet_name='09-10')

# Ora puoi lavorare con il DataFrame df, che contiene i dati dal tuo file Excel

df


# In[40]:


import numpy as np
from sklearn.model_selection import train_test_split

# Creare dati casuali per altezze (variabile indipendente) e pesi (variabile dipendente)
np.random.seed(0)
altezze = np.random.normal(160, 10, 100)
pesi = 0.5 * altezze + np.random.normal(0, 5, 100)

# Suddividere il dataset in training set (70%) e test set (30%)
X_train, X_test, y_train, y_test = train_test_split(altezze, pesi, test_size=0.3, random_state=42)

# Stampare le dimensioni dei training set e test set
print("Dimensioni del Training Set (altezze e pesi):", X_train.shape, y_train.shape)
print("Dimensioni del Test Set (altezze e pesi):", X_test.shape, y_test.shape)


# In[41]:


import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Creazione di dati casuali per visite al sito web e importo delle vendite
np.random.seed(0)
visite_al_sito = np.random.randint(100, 1000, 1000)
importo_vendite = 50 + 0.2 * visite_al_sito + np.random.normal(0, 10, 1000)

# Suddivisione del dataset in training set (70%) e test set (30%)
X_train, X_test, y_train, y_test = train_test_split(visite_al_sito, importo_vendite, test_size=0.3, random_state=42)

# Creazione di un grafico a dispersione
plt.figure(figsize=(10, 6))
plt.scatter(X_train, y_train, label='Training Set', color='blue', alpha=0.7)
plt.scatter(X_test, y_test, label='Test Set', color='orange', alpha=0.7)
plt.xlabel('Numero di Visite al Sito')
plt.ylabel('Importo delle Vendite')
plt.title('Relazione tra Visite al Sito e Importo delle Vendite')
plt.legend()
plt.grid(True)
plt.show()

# Stampare le dimensioni dei training set e test set
print("Dimensioni del Training Set (visite al sito e importo delle vendite):", X_train.shape, y_train.shape)
print("Dimensioni del Test Set (visite al sito e importo delle vendite):", X_test.shape, y_test.shape)


# In[42]:


from sklearn.model_selection import train_test_split
import numpy as np

np.random.seed(1)
# Supponiamo di avere un dataset con feature X e target y
X = np.random.rand(100, 2)  # Dati del dataset (100 campioni, 2 feature)
y = np.random.choice(['A', 'B'], size=100)  # Etichette di classe casuali
# Calcola le proporzioni delle classi nel dataset originale
proporzione_classe_A = sum(y == 'A') / len(y)
proporzione_classe_B = 1 - proporzione_classe_A
# Eseguire uno split stratificato con una proporzione specificata
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
# Calcola le proporzioni delle classi nel training set e nel test set
proporzione_classe_A_train = sum(y_train == 'A') / len(y_train)
proporzione_classe_B_train = 1 - proporzione_classe_A_train

proporzione_classe_A_test = sum(y_test == 'A') / len(y_test)
proporzione_classe_B_test = 1 - proporzione_classe_A_test

# Stampa delle proporzioni
print("Proporzione Classe A nel data Set completo:", proporzione_classe_A)
print("Proporzione Classe B nel data Setcompleto:", proporzione_classe_B)
print("Proporzione Classe A nel Training Set:", proporzione_classe_A_train)
print("Proporzione Classe B nel Training Set:", proporzione_classe_B_train)
print("Proporzione Classe A nel Test Set:", proporzione_classe_A_test)
print("Proporzione Classe B nel Test Set:", proporzione_classe_B_test)


# In[43]:


# Etichette delle classi
labels = ['Classe A', 'Classe B']
# Colori delle fette del grafico
colors = ['gold', 'lightcoral']
# Crea un grafico a torta con etichette
plt.pie([proporzione_classe_A, proporzione_classe_B], labels=labels, colors=colors, autopct='%1.1f%%')
plt.title('Proporzione delle Classi nel Set')
plt.show()


# In[44]:


# Etichette delle classi
labels = ['Classe A', 'Classe B']
# Colori delle fette del grafico
colors = ['gold', 'lightcoral']
# Crea un grafico a torta con etichette
plt.pie([proporzione_classe_A_train, proporzione_classe_B_train], labels=labels, colors=colors, autopct='%1.1f%%')
plt.title('Proporzione delle Classi nel Training Set')
plt.show()


# In[45]:


# Etichette delle classi
labels = ['Classe A', 'Classe B']
# Colori delle fette del grafico
colors = ['gold', 'lightcoral']
# Crea un grafico a torta con etichette
plt.pie([proporzione_classe_A_test, proporzione_classe_B_test], labels=labels, colors=colors, autopct='%1.1f%%')
plt.title('Proporzione delle Classi nel Test Set')
plt.show()


# In[48]:


import random
import numpy as np

dataset=[]
# Creazione di un dataset di 1000 elementi (ad esempio, dati casuali)
popolazione =24000000
for i in range(popolazione):
    dataset.append(random.randint(0, 100000))
    
campione = int(round(0.3 * popolazione))# Estrazione di un campione casuale semplice dal dataset
campione_casuale = random.sample(dataset, campione)

# Calcolo della media e della deviazione standard del campione
media_campione = np.mean(campione_casuale)
deviazione_standard_campione = np.std(campione_casuale)

# Calcolo della media e della deviazione standard del dataset completo
media_dataset = np.mean(dataset)
deviazione_standard_dataset = np.std(dataset)

print(f"Media del campione casuale: {media_campione: .2f}")
print(f"Deviazione standard del campione casuale: {deviazione_standard_campione: .2f}")
print(f"Media del dataset completo: {media_dataset: .2f}")
print(f"Deviazione standard del dataset completo: {deviazione_standard_dataset: .2f}")


# In[47]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Impostare il seed per la riproducibilità
np.random.seed(42)
# Numero totale di elementi nel DataFrame
num_elementi = 10000
# Percentuale di "A"
percentuale_A = 0.7
# Generare la colonna con distribuzione desiderata
colonna = np.random.choice(['A', 'B'], size=num_elementi, p=[percentuale_A, 1 - percentuale_A])

# Creare il DataFrame
df = pd.DataFrame({'ColonnaAB': colonna})
df


# In[ ]:




