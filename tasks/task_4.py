# Очистка "грязных" данных ⭐⭐

raw_data = [
    "Иван;25;Москва;разработчик",
    "Мария-23-Санкт-Петербург-аналитик",
    "Алексей,30,Казань,менеджер",
    "Анна|28|Новосибирск|дизайнер"
]

def clean_data(data):
    cleaned = []

    for item in data:
        if ";" in item:
            parts = item.split(";")
        elif "," in item:
            parts = item.split(",")
        elif "-" in item:
            parts = item.split("-")
        elif "|" in item:
            parts = item.split("|")
        else:
            continue

        record = {
            "name": parts[0].strip(),
            "age": int(parts[1].strip()),
            "city": parts[2].strip(),
            "position": parts[3].strip(),
        }
        cleaned.append(record)
    return cleaned


result = clean_data(raw_data)
print(result)