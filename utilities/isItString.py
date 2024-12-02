import pandas as pd


def check_string_column(input_csv):
    # Carica il file CSV in un DataFrame
    df = pd.read_csv(input_csv)

    # Controlla la colonna 'body' per assicurarti che ogni valore sia una stringa
    non_string_rows = []
    for index, text in enumerate(df["body"]):
        if not isinstance(text, str):  # Se il valore non è una stringa
            non_string_rows.append((index + 1, text, type(text)))  # Aggiungi la riga con l'indice, valore e tipo

    if non_string_rows:
        print("Le seguenti righe contengono valori non stringa nella colonna 'body':")
        for row in non_string_rows:
            print(f"Riga {row[0]}: valore = {row[1]} (Tipo: {row[2]})")
    else:
        print("Tutti i valori nella colonna 'body' sono stringhe.")


# Esegui la funzione con il tuo file CSV
input_csv = 'input_file'  # Sostituisci con il percorso del CSV di input
check_string_column(input_csv)
