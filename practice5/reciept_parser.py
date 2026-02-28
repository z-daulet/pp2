import re
import json

class Parser():
    def __init__(self, file):
        self.file = file
        with open(file, encoding='utf-8') as f:
            self.content = f.read()    
    def parse_price(self):
        pattern = re.compile(r"(?<=Стоимость\n)\d+,\d{2,}")
        matches = re.findall(pattern, self.content)
        return matches
    def parse_title(self):
        pattern = r"\d+\.\n(.+)"
        matches = re.findall(pattern, self.content)
        return matches
    def calculate_total_amount(self):
        pattern = r"\d+\.\n"
        matches = re.findall(pattern,self.content)
        return len(matches)
    def payment(self):
        pattern = r"([А-Яа-я\s]+)(?=:[\n\d+\s\d+\,\d+\n]+ИТОГО:)"
        matches = re.findall(pattern,self.content)
        return matches
    def parse_date(self):
        pattern = r"(?<=Время:\s)(.+)"
        matches = re.findall(pattern,self.content)
        return matches
    def export_to_json(self):
        data ={
            "date":self.parse_date()[0],
            "payment_method": self.payment()[0].strip(),
            "total_count": self.calculate_total_amount(),  
            "items": []          
        }
        titles = self.parse_title()
        prices = self.parse_price()
        for t, p in zip(titles, prices):
            data["items"].append({
                "name": t.strip(),
                "price": p
            })
        return json.dumps(data, ensure_ascii=False, indent=4)

parser = Parser('practice5/raw.txt')

res = parser.export_to_json()
print(res)