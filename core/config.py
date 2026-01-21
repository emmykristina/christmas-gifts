from pathlib import Path

APP_TITLE = 'Christmas Gifts'
DEFAULT_EMOJI = '\U0001F381'
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / 'data'
OUTPUT_FILE = DATA_DIR / 'saved_gifts.txt'
LOG_FILE = DATA_DIR / 'app.log'
