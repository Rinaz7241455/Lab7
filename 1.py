# Лабораторная работа № 7. Вариант 8: «Employee»
# Класс Employee: ФИО, должность, оклад, стаж; расчёт премии и налога (13%)

class Employee:
    """Класс сотрудника с инкапсуляцией полей и расчётом выплат."""

    def __init__(self, full_name: str, position: str, salary: float, experience: int) -> None:
        self.__full_name: str = full_name
        self.__position: str = position
        self.salary = salary
        self.experience = experience

    @property
    def full_name(self) -> str: return self.__full_name

    @property
    def position(self) -> str: return self.__position

    @property
    def salary(self) -> float: return self.__salary

    @salary.setter
    def salary(self, value: float) -> None:
        if value <= 0: raise ValueError("Оклад должен быть положительным.")
        self.__salary = value

    @property
    def experience(self) -> int: return self.__experience

    @experience.setter
    def experience(self, value: int) -> None:
        if value < 0: raise ValueError("Стаж не может быть отрицательным.")
        self.__experience = value

    def calc_bonus(self) -> float:
        """Расчёт премии: 15% при стаже от 5 лет, 10% от 3 лет, иначе 5%."""
        rate: float = 0.15 if self.__experience >= 5 else (0.10 if self.__experience >= 3 else 0.05)
        return self.__salary * rate

    def calc_tax(self) -> float:
        """Расчёт НДФЛ (13%) от суммы оклада и премии."""
        return (self.__salary + self.calc_bonus()) * 0.13

    def print_info(self) -> None:
        """Вывод карточки сотрудника с пояснениями."""
        bonus: float = self.calc_bonus()
        tax: float = self.calc_tax()
        net: float = self.__salary + bonus - tax
        print(f"Сотрудник: {self.__full_name} | Должность: {self.__position}")
        print(f"Оклад: {self.__salary:.2f} руб. | Стаж: {self.__experience} лет")
        print(f"Премия: {bonus:.2f} руб. | Налог (13%): {tax:.2f} руб. | К выплате: {net:.2f} руб.\n")

if __name__ == "__main__":
    emp1 = Employee("Иванов Алексей Андреевич", "Разработчик", 80000.0, 6)
    emp2 = Employee("Смирнова Елена Сергеевна", "Тестировщик", 60000.0, 2)
    emp1.print_info()
    emp2.print_info()
