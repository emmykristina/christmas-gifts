# importerar funktioner från andra filer.
from datetime import datetime
from core.config import APP_TITLE, DATA_DIR, OUTPUT_FILE, GIFTS_FILE, LOG_FILE
from core.ui import show_menu, ask_menu_choice, ask_continue
from core.gifts_logic import get_random_gift
from utility.logger import setup_logger


# dict. som kopplar menyvalet till en kategori - gör koden renare.
MENU_OPTIONS = {
    '1': 'man',
    '2': 'kvinna',
    '3': 'pojkvän',
    '4': 'flickvän',
    '5': 'alla',
    '6': 'avsluta'
}

def main():                         # huvudfunktionen som kör hela programmet.
    DATA_DIR.mkdir(exist_ok=True)   # skapa mappen om den inte finns, krascha inte om den redan finns.
    logger = setup_logger(LOG_FILE)
    logger.info("Application started")
    
    print(APP_TITLE)
    while True:                     # while-loop som körs till användaren väljer att avsluta.
        show_menu()                 # skriver ut menyvalen.
        choice = ask_menu_choice()  # hämtar giltigt val från användaren.

        if choice == '6':           # avsluta programmet om användaren väljer 6.
            print('God Jul! \U0001F384')
            break

        category = MENU_OPTIONS[choice]          # överstätter t.ex '1' till 'man'
        used_gifts = set()                       # 'set' säkerställer att samma förslag inte föreslås två gånger.

        while True:                              # while-loop till "vill du ha ett till förslag?"-inputen.
            gift = get_random_gift(category, used_gifts)  # hämtar ett slumpat förslag från "gifts_logic"-filen.

            if not gift:                         # säkerhetskontroll om kategorin skulle vara tom.
                print (f'Inga fler förslag för kategorin {category}.')
                break

            used_gifts.add(gift)
            print(f'Förslag: {gift} \U0001F381') # skriver ut det slumpade förslaget.
            
            from core.ui import ask_save         # importerar funktionen från ui.py
            if ask_save():
                date_str = datetime.now().strftime('%Y-%m-%d')        # tar nuvarande datum och tid och gör om till angivet text-format.
                with OUTPUT_FILE.open('a', encoding='utf-8') as file: # 'a' = append - lägger till, raderar ej gamla. encoding='utf-8' - gör att emojis fungerar.
                    file.write(f'{date_str} | {category} | {gift}\n') # skapar en tydlig rad.
                print('Förslaget sparades.')
            if not ask_continue():               # om användaren skriver n = går tillbaka till huvudmenyn.
                break

if __name__ == '__main__':          # gör att main() bara körs om filen startas direkt i terminalen.
    main()                          # (standard-Python-sätt att starta program.)