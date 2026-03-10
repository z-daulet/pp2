from pathlib import Path
import shutil

workspace =  Path(__file__).parent/"workspace"
raw_dir = workspace/"raw_dir"
processed = workspace/"processed"

raw_dir.mkdir(parents=True, exist_ok=True)
processed.mkdir(parents=True, exist_ok=True)

# listing all folder and folders in current directory
folder  = Path(".")

for item in folder.iterdir():
    if item.is_dir():
        print(f"Folder: {item}")
    else:
        print(f"File: {item}")

# finding files by its extension

for file in Path(".").rglob("*.md"):
    print(f"Readme file: {file}")