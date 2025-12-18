import random                # "random" genererar ett slumpmässigt förslag.
from core.gifts_data import GIFTS # Importerar dictionary'n "GIFTS" från filen "gifts_data".

# Skapar en funktion som tar emot en kategori, t.ex "man".
def get_random_gift(category: str) -> str | None: # får in en variabel som heter "category", som ska vara text (str).
    gifts = GIFTS.get(category, []) # hämtar listan med juklappar för vald kategori.
    if not gifts:                   # om kategorin inte finns returneras en tom lista istället för att krascha.
        return None                 # om listan är tom finns inga förslag, returnerar då None.
    return random.choice(gifts)     # väljer ett slumpmässigt objekt i listan och skickar tilbaka det till main.

'''
en funktion som tar emot vilken kategori du valt och sedan skickar tillbaka en julklappsidé,
eller ingenting om kategorin skulle vara tom.
'''