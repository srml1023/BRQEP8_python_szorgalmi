import pandas as pd
import json
import os

def extract_schema(file_path):
    print(f"Adatok beolvasása innen: {file_path} ...")
    
    # Beolvassuk a CSV-t (csak az oszlopneveket)
    df = pd.read_csv(file_path, nrows=0)
    columns = df.columns.tolist()
    
    return columns

if __name__ == "__main__":
    input_file = "data/minta_adat.csv"
    output_file = "schema_output.json"
    
    if os.path.exists(input_file):
        # 1. Automatikus Schema Extraction
        extracted_headers = extract_schema(input_file)
        print(f"Sikeresen kinyert oszlopok: {extracted_headers}")
        
        # 2. Eredmény mentése egy ideiglenes JSON fájlba
        schema_data = {
            "source_file": input_file,
            "extracted_columns": extracted_headers
        }
        
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(schema_data, f, indent=4)
            
        print(f"A kinyert séma lementve ide: {output_file}")
    else:
        print(f"Hiba: A {input_file} nem található!")