from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import normalize
import pandas as pd

# 1. Carica i vettori dai file
file1 = "/Users/vale/Desktop/DataSet Progetto Reti/outputs Emotions/meanVector_non_echo.csv"  # Percorso del file delle echo chamber
file2 = "/Users/vale/Desktop/DataSet Progetto Reti/outputs Emotions/meanVector_non_echo.csv"  # Stesso file per ora

# Lettura dei file
echo_data = pd.read_csv(file1)
non_echo_data = pd.read_csv(file2)

# Estrarre i nomi dei file
echo_names = echo_data['file_name']
non_echo_names = non_echo_data['file_name']

# Estrarre solo i vettori emozionali (escludendo 'file_name')
echo_vectors = echo_data.drop(columns=['file_name']).values
non_echo_vectors = non_echo_data.drop(columns=['file_name']).values

# Normalizzare i vettori
echo_vectors = normalize(echo_vectors, axis=1)  # Normalizzazione per ogni vettore (asse 1 = righe)
non_echo_vectors = normalize(non_echo_vectors, axis=1)

# Calcolare la matrice di cosine similarity
similarity_matrix = cosine_similarity(echo_vectors, non_echo_vectors)

# Creare un DataFrame per aggiungere i nomi dei file
similarity_df = pd.DataFrame(similarity_matrix, index=echo_names, columns=non_echo_names)

# Salvataggio del risultato
output_with_names = 'similarity_matrix_nonXnon.csv'
similarity_df.to_csv(output_with_names)

# Mostrare il risultato
print("Matrice di cosine similarity calcolata:")
print(similarity_df)
print(f"La matrice è stata salvata in: {output_with_names}")
