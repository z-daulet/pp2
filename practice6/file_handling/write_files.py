from pathlib import Path

path = Path(__file__).parent/"text.txt"

with open(path, 'a') as f:
    f.write('\nID: 009 | Name: Riven | Age: 21 | City: Kelmar | Score: 76 | Active: True\n')
    f.write('ID: 010 | Name: Alina | Age: 28 | City: Borin | Score: 64 | Active: False\n')
    f.write('ID: 011 | Name: Cedric | Age: 24 | City: Valen | Score: 92 | Active: True\n')

with open(path,'r') as f:
    print(f.read())