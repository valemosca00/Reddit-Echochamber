import pandas as pd
import os

# Specifica il percorso del file CSV originale
file_path = "file_path.csv"

# Specifica il percorso del file di destinazione
output_file_path = "meanVector_echo.csv"

# Estrai il nome del file senza il percorso
file_name = os.path.basename(file_path)

# Leggi il file CSV
data = pd.read_csv(file_path)

# Calcola le medie per ciascuna colonna numerica
mean_values = data.mean(numeric_only=True)

# Crea un nuovo DataFrame con una sola riga
mean_row = mean_values.to_frame().T

# Rinomina la colonna `row` in `file_name` se esiste, altrimenti aggiungi la colonna
if 'row' in data.columns:
    mean_row = mean_row.rename(columns={'row': 'file_name'})

# Se la colonnna `file_name` non esiste già, aggiungila al DataFrame
if 'file_name' not in mean_row.columns:
    mean_row.insert(0, 'file_name', file_name)
else:
    mean_row['file_name'] = file_name

# Verifica se il file di output esiste
if not os.path.exists(output_file_path):
    # Se il file non esiste, crea un nuovo file CSV con l'header
    mean_row.to_csv(output_file_path, index=False)
else:
    # aggiunge i dati in modalità append senza duplicare l'header
    mean_row.to_csv(output_file_path, mode='a', index=False, header=False)

print(f"Il vettore medio è stato aggiunto a '{output_file_path}'.")
