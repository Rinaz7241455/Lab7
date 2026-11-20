# Контрольный пример (Фотография 2)
# Расчёт выплат для двух сотрудников

employees = [
    ("Иванов Алексей Андреевич", "Разработчик", 80000.0, 6),
    ("Смирнова Елена Сергеевна", "Тестировщик", 60000.0, 2),
]

for full_name, position, salary, exp in employees:
    rate = 0.15 if exp >= 5 else (0.10 if exp >= 3 else 0.05)
    bonus = salary * rate
    tax = (salary + bonus) * 0.13
    net = salary + bonus - tax
    print(f"Сотрудник: {full_name} | Должность: {position}")
    print(f"Оклад: {salary:.2f} руб. | Стаж: {exp} лет")
    print(f"Премия: {bonus:.2f} руб. | Налог (13%): {tax:.2f} руб. | К выплате: {net:.2f} руб.\n")
