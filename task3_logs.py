# Скрипт повинен приймати шлях до файлу логів як аргумент командного рядка.
# Скрипт повинен приймати не обов'язковий аргумент командного рядка, після аргументу шляху до файлу логів. Він відповідає за виведення всіх записів певного рівня логування. І приймає значення відповідно до рівня логування файлу. Наприклад аргумент error виведе всі записи рівня ERROR з файлу логів.
# Скрипт має зчитувати і аналізувати лог-файл, підраховуючи кількість записів для кожного рівня логування (INFO, ERROR, DEBUG, WARNING).
# Реалізуйте функцію parse_log_line(line: str) -> dict для парсингу рядків логу.
# Реалізуйте функцію load_logs(file_path: str) -> list для завантаження логів з файлу.
# Реалізуйте функцію filter_logs_by_level(logs: list, level: str) -> list для фільтрації логів за рівнем.
# Реалізуйте функцію count_logs_by_level(logs: list) -> dict для підрахунку записів за рівнем логування.
# Результати мають бути представлені у вигляді таблиці з кількістю записів для кожного рівня. Для цього реалізуйте функцію display_log_counts(counts: dict), яка форматує та виводить результати. Вона приймає результати виконання функції count_logs_by_level.
import sys
import re


def parse_log_line(line: str) -> dict:
    log_pattern = r"^(?P<timestamp>[\d\:\s\-]+)\s+(?P<level>\w+)\s+(?P<message>.+)$"
    match = re.match(log_pattern, line)
    if match:
        return match.groupdict()
    return {}


def load_logs(file_path: str) -> list:
    logs = []
    with open(file_path, "r") as file:
        for line in file:
            parsed_line = parse_log_line(line.strip())
            if parsed_line:
                logs.append(parsed_line)
    return logs


def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log["level"].lower() == level.lower()]


def count_logs_by_level(logs: list) -> dict:
    counts = {}
    for log in logs:
        level = log["level"]
        counts[level] = counts.get(level, 0) + 1
    return counts


def display_log_counts(counts: dict):
    print(f"{'Log Level':<10} | {'Count':<5}")
    print("-" * 20)
    for level, count in counts.items():
        print(f"{level:<10} | {count:<5}")


def main():
    if len(sys.argv) < 1:
        print("Usage: python task3_logs.py [<log_level>]")
        return
    
    log_level = sys.argv[1] if len(sys.argv) > 1 else None
    logs = load_logs("logs.txt")
    if log_level:
        logs = filter_logs_by_level(logs, log_level.upper())
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

if __name__ == "__main__":
    main()
#TESTS:
# Run the script:
# python task3_logs.py 
# To filter by log level:   
# python task3_logs.py ERROR