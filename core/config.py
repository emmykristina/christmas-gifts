from pathlib import Path

APP_TITLE = 'Christmas Gifts'
DEFAULT_EMOJI = '<df81>'
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / 'data'
OUTPUT_FILE = DATA_DIR / 'saved_gifts.txt'

MENU_OPTIONS = {
'1': 'man',
'2': 'kvinna',
'3': 'pojkvän',
'4': 'flickvän',
'5': 'alla',
'6': 'avsluta'
}
