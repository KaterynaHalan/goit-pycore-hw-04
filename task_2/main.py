import pathlib

current_dir = pathlib.Path(__file__).parent

def get_cats_info(path: str) -> list[dict]:
    cats = []

    try:
        with open(f"{current_dir}/{path}", "r", encoding="utf-8") as file:
            for line in file:
                cat_id, name, age = line.strip().split(",")

                cat = {
                    "id": cat_id,
                    "name": name,
                    "age": age
                }

                cats.append(cat)

        return cats

    except FileNotFoundError:
        print("Error: File not found.")
        return []
    except ValueError:
        print("Error: File format is incorrect.")
        return []
