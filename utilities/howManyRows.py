import csv

def count_csv_rows(file_path):
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            row_count = sum(1 for row in reader)
        print(f"Il file CSV contiene {row_count} righe.")
    except FileNotFoundError:
        print("Errore: File non trovato.")
    except Exception as e:
        print(f"Si è verificato un errore: {e}")

# Sostituisci con il percorso del file CSV
file_path = 'input_file'
count_csv_rows(file_path)
