import json

students_data = {
    "Коваленко": ["Олександр", "Петрович", 2005],
    "Шевченко": ["Тарас", "Григорович", 2004],
    "Франко": ["Іван", "Якович", 2005],
    "Українка": ["Леся", "Петрівна", 2006],
    "Бойко": ["Андрій", "Миколайович", 2004],
    "Мельник": ["Марія", "Іванівна", 2005],
    "Козаченко": ["Олег", "Степанович", 2005],
    "Ткаченко": ["Олена", "Василівна", 2006],
    "Кравченко": ["Віктор", "Павлович", 2004],
    "Бондаренко": ["Юлія", "Олександрівна", 2005]
}

json_filename = "students.json"

with open(json_filename, 'w', encoding='utf-8') as json_file:
    json.dump(students_data, json_file, ensure_ascii=False, indent=4)

print(f"Дані успішно записані у файл {json_filename}.")

with open(json_filename, 'r', encoding='utf-8') as json_file:
    loaded_data = json.load(json_file)

print("\n--- Прочитані дані з файлу ---")
for surname, details in loaded_data.items():
    print(f"Прізвище: {surname}, Ім'я: {details[0]}, По батькові: {details[1]}, Рік народження: {details[2]}")