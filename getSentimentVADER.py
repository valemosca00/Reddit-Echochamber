import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
from tqdm import tqdm
import nltk

# Scarica il lessico di VADER
#nltk.download('vader_lexicon')

# Inizializza VADER
sia = SentimentIntensityAnalyzer()

# Carica il dataset CSV
input_file = "input_file"  # Nome del file CSV in ingresso
output_file = "output_file"  # Nome del file CSV in uscita

# Leggi il file CSV
df = pd.read_csv(input_file)

# Controlla se il dataset ha una colonna chiamata 'body'
if 'body' not in df.columns:
    raise ValueError("Il file CSV deve contenere una colonna chiamata 'body'.")

# Calcola il sentiment per ogni riga con la barra di caricamento
sentiments = []
for text in tqdm(df['body'], desc="Analizzando il sentiment"):
    if pd.isna(text):  # Gestione valori mancanti
        sentiments.append({'neg': 0, 'neu': 0, 'pos': 0, 'compound': 0})
    else:
        sentiment = sia.polarity_scores(text)
        sentiments.append(sentiment)

# Converti i risultati in un DataFrame
sentiment_df = pd.DataFrame(sentiments)

# Aggiunge un indice incrementale
df['index'] = range(1, len(df) + 1)

result_df = pd.concat([df['index'], sentiment_df], axis=1)

# Salva i risultati in un nuovo file CSV
result_df.to_csv(output_file, index=False)

print(f"Analisi del sentiment completata. File salvato come {output_file}")
