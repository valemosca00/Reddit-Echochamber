import pandas as pd
from transformers import pipeline


def classify_emotions(input_csv, output_csv):
    # Carica il file CSV
    df = pd.read_csv(input_csv)

    # Controlla che la colonna "body" esista
    if "body" not in df.columns:
        raise ValueError('Il file CSV deve contenere una colonna chiamata "body"')

    # Carica il modello di Hugging Face
    classifier = pipeline(
        "text-classification",
        model="SamLowe/roberta-base-go_emotions",
        top_k=None,  # Ottieni tutti i punteggi per ogni classe
        truncation=True,
        max_length=512,  # Impostazione per troncare il testo a 512 token
        device = 0  # Imposta la GPU come dispositivo (0 per la prima GPU)
    )

    # Funzione per classificare il testo e restituire un dizionario con i punteggi
    def get_emotion_scores(text):
        # Controlla se il testo non è una stringa e lo converte
        if not isinstance(text, str):
            print(f"Valore non stringa trovato e convertito: {text}")  # Stampa il dato originale
            text = str(text)  # Converte in stringa

        scores = classifier(text)[0]
        return {score['label']: score['score'] for score in scores}

    # Gestisci i valori NaN o non stringa nella colonna "body"
    df["body"] = df["body"].fillna("").astype(str)

    # Applica il classificatore ai testi nella colonna "body"
    emotion_scores = df["body"].apply(get_emotion_scores)

    # Crea un DataFrame con i punteggi per ogni emozione
    emotion_df = pd.DataFrame(emotion_scores.tolist())

    # Aggiungi una colonna numerica progressiva chiamata "row"
    emotion_df.insert(0, "row", range(1, len(emotion_df) + 1))

    # Salva il nuovo DataFrame in un file CSV
    emotion_df.to_csv(output_csv, index=False)
    print(f"File salvato con successo in {output_csv}")


# Esegui lo script
input_csv = "/Users/vale/Desktop/DataSet Progetto Reti/non_echo_data/reddit_data_shakespeare.csv"  # Sostituisci con il nome del file CSV di input
output_csv = "output.csv"  # Sostituisci con il nome del file CSV di output
classify_emotions(input_csv, output_csv)
