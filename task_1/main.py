import pathlib

current_dir = pathlib.Path(__file__).parent

def total_salary(path: str) -> tuple[int, float]:
    total = 0
    count = 0

    try:
        with open(f"{current_dir}/{path}", "r", encoding="utf-8") as fh:
            for line in fh:
                _, salary = line.strip().split(",")
                total += int(salary)
                count += 1

        average = int(total / count) if count > 0 else 0
        return total, average

    except FileNotFoundError:
        print("Error: File not found.")
        return 0, 0
    except ValueError:
        print("Error: File format is incorrect.")
        return 0, 0
