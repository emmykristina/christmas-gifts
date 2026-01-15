# funktion som endast skriver ut huvudmenyn.
def show_menu():
    print('\nJulklappar till:')
    print('1) Man')
    print('2) Kvinna')
    print('3) Pojkvän')
    print('4) Flickvän')
    print('5) Funkar för alla')
    print('6) Avsluta')

# funktion som hämtar ett val från användaren (1-6).
def ask_menu_choice() -> str:
    while True:                                      # felhantering - while-loop som fortsätter tills användaren skriver något korrekt.
        choice = input('Välj (1-6): ').strip()       # tar in input
        if choice in ['1', '2', '3', '4', '5', '6']: # kontrollerar att användaren skrev ett tillåtet nummer.
            return choice                            # returnerar svaret om det är ok.
        print('Ogiltigt val, försök igen.')          # felmeddelande om valet inte är godkänt.

# funktion som frågar användaren om de vill se fler förslag.
def ask_continue() -> bool:
    while True:                   # felhantering - loop som hanterar felaktiga svar.
        answer = input('Vill du ha ett till förslag? (j/n): ')\
        .strip().lower()          # tar input, tar bort mellanslag, gör svaret till små bokstäver.
        if answer in ['j', 'n']:  # om svaret är j = retunera True, om n = False
            return answer == 'j'
        print('Skriv j eller n.') # felmeddelande

# funktion som frågar användaren om de vill spara förslagen i en textfil.
def ask_save() -> bool:
    while True:
        answer = input('Vill du spara förslaget i en textfil? (j/n): ').strip().lower()
        if answer in ['j', 'n']:
            return answer == 'j'
        print('Skriv j eller n.')