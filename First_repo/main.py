def total_salary(path):
    try:
        total = 0
        count = 0
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    name, salary = line.strip().split(',')
                    total += int(salary)
                    count += 1
                except ValueError:
                    print(f"Неправильний формат рядка: {line.strip()}")
                    continue

        if count == 0:
            return 0, 0  
        average = total // count
        return total, average

    except FileNotFoundError:
        print(f"Файл за шляхом '{path}' не знайдено.")
        return 0, 0
    except Exception as e:
        print(f"Сталася помилка при обробці файлу: {e}")
        return 0, 0
    


    def get_cats_info(path):
    cats_list = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    cat_id, name, age = parts
                    cat_dict = {"id": cat_id, "name": name, "age": age}
                    cats_list.append(cat_dict)
                else:
                    print(f"Пропущено рядок з некоректним форматом: {line.strip()}")
        return cats_list
    except FileNotFoundError:
        print(f"Файл за шляхом '{path}' не знайдено.")
        return []
    except Exception as e:
        print(f"Виникла помилка при читанні файлу: {e}")
        return []


                