import json
import datetime

def track_lineage():
    print("Adateredet (Lineage) származási fa generálása...")
    
    lineage_data = {
        "dataset_name": "Kutatási minta adathalmaz",
        "version": "1.0",
        "processed_at": datetime.datetime.now().isoformat(),
        "pipeline_steps": [
            {
                "step": "1. Schema Extraction",
                "input_file": "data/minta_adat.csv",
                "output_file": "schema_output.json",
                "action": "CSV fejlécek automatikus kinyerése"
            },
            {
                "step": "2. Ontology Mapping",
                "input_file": "schema_output.json",
                "output_file": "metadata.jsonld",
                "action": "Fejlécek összekötése SNOMED és NCIT orvosi szótárakkal"
            }
        ],
        "status": "FAIR elveknek megfelelő adateredet rögzítve."
    }
    
    with open("lineage_log.json", "w", encoding="utf-8") as f:
        json.dump(lineage_data, f, indent=4)
        
    print("Sikeres lineage tracking! A származási fa lementve ide: lineage_log.json")

if __name__ == "__main__":
    track_lineage()