from pathlib import Path
path = Path(__file__).parent / "text.txt"

with open(path) as f:
    print(f.read())
