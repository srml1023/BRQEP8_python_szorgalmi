import json
import os

# Ez itt a "Szótár-illesztés": összekötjük az oszlopainkat orvosi azonosítókkal (Ontológiákkal)
ONTOLOGY_MAP = {
    "patient_id": "http://purl.obolibrary.org/obo/NCIT_C83226",  # Nemzeti Rákintézet azonosító
    "heart_rate": "http://purl.bioontology.org/ontology/SNOMEDCT/364075005", # SNOMED klinikai kód
    "blood_pressure": "http://purl.bioontology.org/ontology/SNOMEDCT/75367002",
    "study_date": "http://purl.obolibrary.org/obo/NCIT_C25164"
}

def create_json_ld(schema_file, output_file):
    print(f"Séma beolvasása innen: {schema_file} ...")
    
    # 1. Beolvassuk az előző lépés eredményét
    with open(schema_file, "r", encoding="utf-8") as f:
        schema_data = json.load(f)
    
    columns = schema_data["extracted_columns"]
    
    # 2. JSON-LD alapstruktúra felépítése a FAIR elveknek megfelelően
    json_ld = {
        "@context": "https://schema.org",
        "@type": "Dataset",
        "name": "Kutatási minta adathalmaz",
        "description": "Automatikus pipeline által generált metaadatok",
        "sourceFile": schema_data["source_file"],
        "variablesMeasured": []
    }
    
    # 3. Oszlopok illesztése az ontológiákhoz
    for col in columns:
        # Kikeresi a szótárból a linket, ha nincs meg, kap egy "ismeretlen" címkét
        mapped_uri = ONTOLOGY_MAP.get(col, "http://example.com/unknown")
        
        variable = {
            "@type": "PropertyValue",
            "name": col,
            "propertyID": mapped_uri
        }
        json_ld["variablesMeasured"].append(variable)
    
    # 4. Mentés JSON-LD fájlként
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(json_ld, f, indent=4)
        
    print(f"Sikeres ontológia-illesztés! JSON-LD lementve ide: {output_file}")

if __name__ == "__main__":
    input_schema = "schema_output.json"
    output_jsonld = "metadata.jsonld"
    
    if os.path.exists(input_schema):
        create_json_ld(input_schema, output_jsonld)
    else:
        print("Hiba: Előbb futtasd az extractor.py-t, mert nincs meg a schema_output.json!")