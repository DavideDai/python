#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install seaborn


# In[2]:


pip install plotly


# In[3]:


import pandas as ad


dataset = [
    {"età": 25,"punteggio": 90, "ammesso": 1},
    {"età": None,"punteggio": 85, "ammesso": 0},
    {"età": 28,"punteggio": None, "ammesso": 1},
    {"età": None,"punteggio": 75, "ammesso": 1},
    {"età": 23,"punteggio": None, "ammesso": None},
    {"età": 23,"punteggio": 77, "ammesso": None},
    
]
df = pd.DataFrame(dataset)
df


# In[ ]:


righe_con_dati_mancanti = df[df.isnull().any(axys=1)]
righe_con_dati_mancanti


# In[ ]:


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


# In[ ]:


missing_percent = (df.isnull(). len


# In[ ]:


numeric_cols = df.select_dtypes(include=['number'])
numeric_cols.colums


# In[ ]:


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


# In[5]:


df.isnull()


# In[ ]:


df.isnull().sum()


# In[ ]:


missing_percent = (df.isnull().sum() / len(df)) * 100
missing_percent


# In[ ]:


missing_percent = (df.isnull().sum() / len(df)) * 100

plt.figure(figsize=(10, 6))
missing_percent.plot(kind='bar', color='skyblue',alpha=0.8)
plt.xlabel('variabili')
plt.ylabel('analisi dei missing values per variabile')
plt.xticks(rotation=0)
plt.show()


# In[ ]:


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


# In[ ]:


plt.figure(figsize=(8, 6))
sns.heatmap(missing_matrix, cmap='viridis', cbar=False,alpha=0.8)
plt.title('Matrice di missing values')
plt.show


# In[ ]:


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


# In[ ]:


#informazione sul dataset
print(df.info())


#statistiche descrittive
print(df.describe())


# In[ ]:


plt.figure(figsize=(12,6))
sns.set_style("whitegrid")
sns.hitsplot(df["Reddito"], kde=False, bins=50, label="Reddito")
plt.legend()
plt.title('Distribuzione delle variabili numeriche')
plt.show()


# In[4]:


numeric_features = df.select_dtypes(include=[np.number])
sns.pairplot(df[numeric_features.columns])
plt.title('Matrice di Scatter Plot tra variabili numeriche')
plt.show()


# In[ ]:


plt.figure(figsize=(10, 6))
sns.boxplot(x='Genere', y='Punteggio')
plt.title('box plot genere maschile e femminile')
plt.show()


# In[ ]:


import plotly.express as px
fig = px.scatter(df, x='Età', y='Reddito', color='Genere', size='Punteggio')
fig.update_layout(title='Grafico a dispersione interattivo')
fig.show()


# In[ ]:


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


# In[ ]:


conditional_means = df['Numeric_Var'].fillna(df.groupby('Categorical_Var')['Numeric_Var'].transform('mean'))


# In[ ]:


df['Numeric_Var'] = conditional_means
print(df)
plt.figure(figsize=(8,6))
sns.barplot(data=df, x='Categorical_Var', y='Numeric_Var', 'ci'= False)
plt.xlabel('Categorical_Var')
plt.ylabel('Media Condizionata di Numeric_Var')
plt.title('Media Condizionata delle Variabili Numeriche per Categoria')
plt.show


# In[ ]:


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


# In[ ]:


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


# In[ ]:


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


# In[ ]:


import os
import pandas as pd

# Specifica il percorso della cartella contenente i file CSV
percorso_cartella = 'C:\\Users\\davide\\OneDrive\\Desktop\\robotica\\serieAnuovo'

# Lista per memorizzare tutti i DataFrame letti dai file CSV
lista_dataframes = []

# Scansiona la cartella e leggi i file CSV
for nome_file in os.listdir(percorso_cartella):
    if nome_file.endswith(".csv"):
        percorso_file_csv = os.path.join(percorso_cartella, nome_file)
        df = pd.read_csv(percorso_file_csv)
        lista_dataframes.append(df)

# Ora lista_dataframes contiene tutti i DataFrame letti dai file CSV nella cartella


# In[ ]:


#omporta xlsx con fogli 
import pandas as pd

# Specifica il percorso del tuo file Excel
percorso_file_excel = "C:\\Users\\davide\\OneDrive\\Desktop\\robotica\\serieA.xlsx"

# Leggi il file Excel in un DataFrame

df = pd.read_excel(percorso_file_excel, sheet_name='09-10')

# Ora puoi lavorare con il DataFrame df, che contiene i dati dal tuo file Excel

df


# In[ ]:


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


# In[ ]:


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


# In[ ]:


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


# In[ ]:


# Etichette delle classi
labels = ['Classe A', 'Classe B']
# Colori delle fette del grafico
colors = ['gold', 'lightcoral']
# Crea un grafico a torta con etichette
plt.pie([proporzione_classe_A, proporzione_classe_B], labels=labels, colors=colors, autopct='%1.1f%%')
plt.title('Proporzione delle Classi nel Set')
plt.show()


# In[ ]:


# Etichette delle classi
labels = ['Classe A', 'Classe B']
# Colori delle fette del grafico
colors = ['gold', 'lightcoral']
# Crea un grafico a torta con etichette
plt.pie([proporzione_classe_A_train, proporzione_classe_B_train], labels=labels, colors=colors, autopct='%1.1f%%')
plt.title('Proporzione delle Classi nel Training Set')
plt.show()


# In[ ]:


# Etichette delle classi
labels = ['Classe A', 'Classe B']
# Colori delle fette del grafico
colors = ['gold', 'lightcoral']
# Crea un grafico a torta con etichette
plt.pie([proporzione_classe_A_test, proporzione_classe_B_test], labels=labels, colors=colors, autopct='%1.1f%%')
plt.title('Proporzione delle Classi nel Test Set')
plt.show()


# In[ ]:


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


# In[ ]:


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


# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt

# Crea un DataFrame di esempio
data = {'Valori': [1, 2, 3, 4, 5, 10, 15, 20, 25, 300, 1000, 100000000, -50000000, -50]}
df = pd.DataFrame(data)
# Lista con outliers da entrambi i lati

# Calcola la media e la deviazione standard
mean_value = df['Valori'].mean()
std_dev = df['Valori'].std()
std_dev


# In[9]:


outliers = df[(df['Valori'] > mean_value + 3 * std_dev) | (df['Valori'] < mean_value - 3 * std_dev)]
outliers


# In[13]:


# Crea un grafico a dispersione
plt.scatter(df.index, df['Valori'], label='Valori')

# Evidenzia gli outliers nel grafico con un colore diverso
plt.scatter(outliers.index, outliers['Valori'], color='red', label='Outliers')

# Aggiungi la media e la deviazione standard al grafico
plt.axhline(y=mean_value, color='green', linestyle='--', label='Media')
plt.axhline(y=mean_value + 3 * std_dev, color='orange', linestyle='--', label='±3 Deviazioni Standard')
plt.axhline(y=mean_value - 3 * std_dev, color='orange', linestyle='--')

# Aggiungi etichette e legenda al grafico
plt.xlabel('Indice')
plt.ylabel('Valori')
plt.title('Grafico con Outliers Evidenziati')
plt.legend()

# Mostra il grafico
plt.show()


# In[16]:


import pandas as pd
import matplotlib.pyplot as plt

# Crea un DataFrame di esempio con 4 features
data = {'Feature1': [1, 200, 3, 4, 50000, 10, 15, 20, 2500000, 300000000, 100000000],
        'Feature2': [2, 4, 6, 8, 10, 20, 30, 40, 500, 60, 200],
        'Feature3': [5, 10, 15, 20000, 25, 50, 75, 100, 125, 150, 500000],
        'Feature4': [1, -200000, 3, 4000000000, 5, 10, 15, 20, 200, 30, 10000]}

df = pd.DataFrame(data)

# Definisci il numero minimo di features che devono superare la soglia per considerare un dato un outlier
min_features_threshold = 1
k=3 #intervallo di confidenza 

# Lista per salvare gli indici degli outliers
outlier_indices = []

# Itera su ogni feature
for feature in df.columns:
    mean_value = df[feature].mean()
    std_dev = df[feature].std()    
    # Identifica gli outliers per ciascuna feature
    df['Outlier_' + feature] = (df[feature] > mean_value + k * std_dev) | (df[feature] < mean_value - k * std_dev)
df


# In[19]:


df['Num_Outliers'] = df.filter(like = 'Outlier_').sum(axis=1)
df


# In[20]:


outliers = df[df['Num_Outliers'] >= min_features_threshold]
outliers


# In[21]:


# Aggiungi una colonna che indica se il record è un outlier o meno
df['Is_Outlier'] = df.index.isin(outliers.index)
# Rimuovi colonne ausiliarie
df.drop(df.filter(like='Outlier_').columns, axis=1, inplace=True)
df.drop('Num_Outliers', axis=1, inplace=True)
df


# In[1]:


import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
# Creiamo un DataFrame di esempio
data = {'Feature1': [100, 200, 300, 400],
        'Feature2': [0.1, 0.5, 0.2, 0.8],
        'Feature3': [1000, 800, 1200, 1500]}

df = pd.DataFrame(data)

# Visualizziamo il DataFrame prima dello scaling
print("DataFrame prima dello scaling:")
print(df)

# Iniziamo con il Min-Max scaling
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(df)

# Creiamo un nuovo DataFrame con le features scalate
scaled_df = pd.DataFrame(scaled_data, columns=df.columns)

# Visualizziamo il DataFrame dopo lo scaling
print("\nDataFrame dopo lo scaling:")
print(scaled_df)


# In[2]:


import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Creiamo un DataFrame di esempio
data = {'Feature1': [100, 200, 300, 400],
        'Feature2': [0.1, 0.5, 0.2, 0.8],
        'Feature3': [1000, 800, 1200, 1500]}

df = pd.DataFrame(data)

# Visualizziamo il DataFrame prima dello scaling
print("DataFrame prima dello scaling:")
print(df)

# Min-Max scaling
min_max_scaler = MinMaxScaler()
min_max_scaled_data = min_max_scaler.fit_transform(df)
min_max_scaled_df = pd.DataFrame(min_max_scaled_data, columns=df.columns)

# Z-score scaling
standard_scaler = StandardScaler()
standard_scaled_data = standard_scaler.fit_transform(df)
standard_scaled_df = pd.DataFrame(standard_scaled_data, columns=df.columns)

# Visualizziamo i DataFrame dopo lo scaling
print("\nDataFrame dopo Min-Max scaling:")
print(min_max_scaled_df)

print("\nDataFrame dopo Z-score scaling:")
print(standard_scaled_df)


# In[3]:


import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler

# Creiamo un DataFrame di esempio
data = {'Feature1': [100, 200, 300, 400],
        'Feature2': [0.1, 0.5, 0.2, 0.8],
        'Feature3': [1000, 800, 1200, 1500]}

df = pd.DataFrame(data)

# Visualizziamo il DataFrame prima dello scaling
print("DataFrame prima dello scaling:")
print(df)

# Min-Max scaling
min_max_scaler = MinMaxScaler()
min_max_scaled_data = min_max_scaler.fit_transform(df)
min_max_scaled_df = pd.DataFrame(min_max_scaled_data, columns=df.columns)

# Z-score scaling
standard_scaler = StandardScaler()
standard_scaled_data = standard_scaler.fit_transform(df)
standard_scaled_df = pd.DataFrame(standard_scaled_data, columns=df.columns)

# Robust scaling
robust_scaler = RobustScaler()
robust_scaled_data = robust_scaler.fit_transform(df)
robust_scaled_df = pd.DataFrame(robust_scaled_data, columns=df.columns)

# Visualizziamo i DataFrame dopo lo scaling
print("\nDataFrame dopo Min-Max scaling:")
print(min_max_scaled_df)

print("\nDataFrame dopo Z-score scaling:")
print(standard_scaled_df)

print("\nDataFrame dopo Robust scaling:")
print(robust_scaled_df)


# In[4]:


import pandas as pd

# Creiamo un DataFrame di esempio con una variabile categorica
data = {'Colore': ['Rosso', 'Blu', 'Verde', 'Rosso']}
df = pd.DataFrame(data)

# Applichiamo l'encoding One-Hot
df_encoded = pd.get_dummies(df, columns=['Colore'])

# Visualizziamo il DataFrame dopo l'encoding
print(df_encoded)


# In[5]:


import pandas as pd

# Creiamo un DataFrame di esempio con una variabile categorica ordinale
data = {'Livello_Istruzione': ['Scuola elementare', 'Scuola media', 'Diploma', 'Scuola elementare']}
df = pd.DataFrame(data)

# Definiamo l'ordine delle categorie
livelli_istruzione_ordine = {'Scuola elementare': 1, 'Scuola media': 2, 'Diploma': 3}

# Applichiamo l'encoding ordinale
df['Livello_Istruzione_Ordinale'] = df['Livello_Istruzione'].map(livelli_istruzione_ordine)

# Visualizziamo il DataFrame dopo l'encoding
print(df)


# In[ ]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OrdinalEncoder

# Creiamo un DataFrame di esempio
data = {'Livello_Istruzione': ['Scuola elementare', 'Scuola media', 'Diploma', 'Laurea'],
        'Colore_Preferito': ['Rosso', 'Blu', 'Verde', 'Rosso'],
        'Età': [25, 30, 22, 35],
        'Punteggio': [85, 92, 78, 96]}

df = pd.DataFrame(data)


