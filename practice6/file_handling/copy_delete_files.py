import os
import shutil
from pathlib import Path

path = Path(__file__).parent/"text.txt"
try:
    os.remove(path)
except FileExistsError:
    print("File does not exist")

try:
    os.rmdir("practice0")
except FileNotFoundError:
    print("Folder does not exist")


shutil.copy(path, "text_backup.txt")