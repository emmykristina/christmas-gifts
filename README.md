-- Christmas Gifts CLI --

Ett enkelt CLI-program som ger julklappsförslag baserat på kategori och låter användaren spara förslag till en textfil.

Projektet är byggt som ett mini-projekt för att visa modulindelning, importer och felhantering i Python.


Funktioner:

- Välj kategori (man, kvinna, pojkvän, flickvän, alla)

- Slumpmässiga julklappsförslag

- Samma förslag visas bara en gång per kategori

- Möjlighet att spara förslag med datum och kategori till fil

- Felhantering vid ogiltiga menyval eller slut på förslag

- Logger som skriver programmets händerlser till en loggfil

Köra programmet:

- Aktivera virtuell miljö och kör:

christmas-gifts

- Alternativt:

python -m core.main


Projektstruktur:
## Projektstruktur

```text
christmas_gifts
│
├── core
│   ├── __init__.py
│   ├── config.py
│   ├── gifts_data.py
│   ├── gifts_logic.py
│   ├── main.py
│   └── ui.py
│
├── data
│   └── saved_gifts.txt
│
├── .gitignore
├── pyproject.toml
├── README.md
├── requirements.txt
└── structure.txt