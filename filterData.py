import pandas as pd
import re

# Percorso del file originale e del file filtrato
input_file = "/Users/vale/Desktop/DataSet Progetto Reti/non_Filtered_Data/non_echo_data/reddit_data_sports.csv"
output_file = "/Users/vale/Desktop/DataSet Progetto Reti/Filtered_Data/non_echo_filtered_data/reddit_filteredData_sports.csv"

# Caricare il file CSV
df = pd.read_csv(input_file)

# Funzione per verificare se la riga deve essere rimossa
def is_removable(text):
    # Rimuove spazi e punteggiatura per il controllo
    clean_text = re.sub(r'[^\w\s]', '', str(text)).strip()
    # Verifica criteri di esclusione
    return (clean_text in ["removed", "deleted"] or
            len(clean_text.split()) <= 2)

# Filtrare il dataframe
filtered_df = df[~df['body'].apply(is_removable)]

# Salvare il file filtrato
filtered_df.to_csv(output_file, index=False)

print(f"File filtrato salvato in: {output_file}")