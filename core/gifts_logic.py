import random                # "random" genererar ett slumpmässigt förslag.
from core.gifts_data import GIFTS # Importerar dictionary'n "GIFTS" från filen "gifts_data".

# Skapar en funktion som tar emot en kategori, t.ex "man".
def get_random_gift(category: str, used_gifts: set[str]) -> str | None:
    all_gifts = GIFTS.get(category, [])

    # filtrera bort presenter som redan använts
    available_gifts = [gift for gift in all_gifts if gift not in used_gifts]

    if not available_gifts:
        return None
    
    return random.choice(available_gifts)

'''
en funktion som tar emot vilken kategori du valt och sedan skickar tillbaka en julklappsidé,
eller ingenting om kategorin skulle vara tom.
'''