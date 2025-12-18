# importerar funktioner från de andra filerna.
from core.ui import show_menu, ask_menu_choice, ask_continue
from core.gifts_logic import get_random_gift

# dict. som kopplar menyvalet till en kategori - gör koden renare.
CHOICE_TO_CATEGORY = {
    '1': 'man',
    '2': 'kvinna',
    '3': 'pojkvän',
    '4': 'flickvän',
    '5': 'alla',
}

def main():                         # huvudfunktionen som kör hela programmet.
    while True:                     # while-loop som körs till användaren väljer att avsluta.
        show_menu()                 # skriver ut menyvalen.
        choice = ask_menu_choice() # hämtar giltigt val från användaren.

        if choice == '6':           # avsluta programmet om användaren väljer 6.
            print('God Jul! \U0001F384')
            break

        category = CHOICE_TO_CATEGORY[choice] # överstätter t.ex '1' till 'man'

        while True:                           # while-loop till "vill du ha ett till förslag?"-inputen.
            gift = get_random_gift(category)  # hämtar ett slumpat förslag från "gifts_logic"-filen.
            if gift is None:                  # säkerhetskontroll om kategorin skulle vara tom.
                print('Inga förslag för den här kategorin.')
                break

            print(f'Förslag: {gift} \U0001F381')         # skriver ut det slumpade förslaget.

            if not ask_continue():            # om användaren skriver n = går tillbaka till huvudmenyn.
                break

if __name__ == '__main__': # gör att main() bara körs om filen startas direkt i terminalen.
    main()                  # (standard-Python-sätt att starta program.)