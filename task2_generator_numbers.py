# Використовуйте регулярні вирази для ідентифікації дійсних чисел у тексті,
#   з урахуванням, що числа чітко відокремлені пробілами.
# Застосуйте конструкцію yield у функції generator_numbers для створення генератора.
# Переконайтеся, що sum_profit коректно обробляє дані від generator_numbers і підсумовує всі числа.

import re
from decimal import Decimal

DECIMAL_PATTERN = r"(?<!\w)[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?(?!\w)"


def generator_numbers(text: str):
    for match in re.finditer(DECIMAL_PATTERN, text):
        yield match.group()


def sum_profit(text: str, generator_func) -> Decimal:
    total = Decimal(0.0)
    for number in generator_func(text):
        total += Decimal(number)

    return total


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
assert total_income == Decimal("1351.46")


# TESTS:

result = re.findall(DECIMAL_PATTERN, "vals: +3, -2., .5, 10.0, 6e-3, +.7E2")
assert result == ["+3", "-2.", ".5", "10.0", "6e-3", "+.7E2"]

assert generator_numbers("100.5 200.75 300.25") is not None
assert generator_numbers("50.0 25.5 24.5") is not None
assert generator_numbers("1 2 -3") is not None
assert generator_numbers("10.0 20.0 30.0 40.0   50.0") is not None


total_income = sum_profit("wer 100 qwerty 200 qwerty 300.25", generator_numbers)
assert total_income == Decimal("600.25")

total_income = sum_profit("qwerty 50.0 qwerty 25.5 qwerty 24.5", generator_numbers)
assert total_income == Decimal("100")

total_income = sum_profit("0.1 0.2 0.3 0.4", generator_numbers)
assert total_income == Decimal("1")

total_income = sum_profit("100 3000 50.5", generator_numbers)
assert total_income == Decimal("3150.5")

total_income = sum_profit("-100 3000 50.5", generator_numbers)
assert total_income == Decimal("2950.5")
