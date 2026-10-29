\# FAIR Data Ingestion \& Metadata Pipeline



\## A projekt leírása

A tudományos kutatásokban kulcsfontosságú, hogy a nyers adatok megtalálhatók, hozzáférhetők, átjárhatók és újrahasznosíthatók legyenek (FAIR elvek). Ez a projekt egy automatizált adatingestion és metaadat-kezelő pipeline-t valósít meg Python nyelven.



\## Főbb funkciók és elvárások teljesítése

1\. \*\*Automatikus Schema Extraction (`extractor.py`)\*\*: 

&#x20;  A rendszer képes a nyers adatfájlok (pl. CSV) automatikus beolvasására és a fejlécek kinyerésére anélkül, hogy a teljes adathalmazt a memóriába töltené.

2\. \*\*Ontológia- és Szótár-illesztés (`mapper.py`)\*\*: 

&#x20;  A kinyert metaadatok automatikus összekötése orvosi és tudományos ontológiákkal (pl. SNOMED CT, NCIT), és ezek exportálása szabványos \*\*JSON-LD\*\* formátumba.

3\. \*\*Version Control \& Lineage Tracking (`lineage.py`)\*\*: 

&#x20;  Az adathalmazok származási fájának (adateredet) követése, a pipeline lépéseinek naplózása, biztosítva a teljes transzparenciát.



\## Telepítés és Futtatás

A projekt futtatásához Python környezet szükséges.



1\. Függőségek telepítése:

&#x20;  `pip install -r requirements.txt`

2\. Schema kinyerése:

&#x20;  `python extractor.py`

3\. JSON-LD és Ontológia generálása:

&#x20;  `python mapper.py`

4\. Származási fa (Lineage) rögzítése:

&#x20;  `python lineage.py`



Készült a 2026.11.01-i projektfeladat határidejére.

