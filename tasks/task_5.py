import re

# ⃣ Номер телефона

def check_number_pattern(numbers):
    clean_number = numbers.replace(" ", "")

    pattern = r"^(\+996)(\d{3})(\d{3})(\d{3})$"

    match = re.fullmatch(pattern, clean_number)

    if not match:
        return "Неверный формат номера"

    return f"{match.group(1)} {match.group(2)} {match.group(3)} {match.group(4)}"

print(check_number_pattern("+996774814583"))
print(check_number_pattern("+996 774 814 583"))
print(check_number_pattern("+996 774814583"))