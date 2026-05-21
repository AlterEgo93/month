import csv
import json
import urllib.request
from io import StringIO

# URL вашої Google Таблиці у форматі CSV
SHEET_URL = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTMw6H2nTGjSr4xbZNjl67tncfknalcb-RT7fBLfmJna7qwEkwxh49XHC3AgDEpWHG7IdnuflyXXnWE/pub?gid=825422948&single=true&output=csv'

def update_data():
    try:
        # Завантажуємо дані з Google Sheets (додано User-Agent для уникнення блокувань)
        req = urllib.request.Request(SHEET_URL, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            csv_data = response.read().decode('utf-8')
        
        # Читаємо CSV
        reader = csv.reader(StringIO(csv_data))
        next(reader) # Пропускаємо перший рядок із заголовками
        
        data = {}
        for row in reader:
            if len(row) >= 2:
                key = row[0].strip()
                raw_value = row[1].strip()
                
                # Конвертуємо у число, якщо це можливо
                try:
                    value = float(raw_value) if '.' in raw_value else int(raw_value)
                except ValueError:
                    value = raw_value
                    
                data[key] = value
                
        # Зберігаємо у JSON файл у поточній директорії
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            
        print("Дані успішно оновлено та збережено у data.json")
        
    except Exception as e:
        print(f"Помилка під час оновлення даних: {e}")

if __name__ == '__main__':
    update_data()
  
