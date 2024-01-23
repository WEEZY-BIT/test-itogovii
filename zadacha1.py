import json
import datetime
import uuid

# Функция для создания заметки
def create_note():
    title = input("Введите заголовок заметки: ")
    text = input("Введите текст заметки: ")
    note_id = str(uuid.uuid4())  # Генерация уникального идентификатора
    created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {
        "id": note_id,
        "title": title,
        "text": text,
        "created_at": created_at
    }
    return note

# Функция для сохранения заметки в файл
def save_note(note):
    with open("notes.json", "a") as file:
        json.dump(note, file)
        file.write("\n")

# Функция для чтения списка заметок из файла
def read_notes():
    with open("notes.json", "r") as file:
        notes = [json.loads(line) for line in file]
    return notes

# Функция для редактирования заметки
def edit_note():
    note_id = input("Введите идентификатор заметки для редактирования: ")
    notes = read_notes()
    for note in notes:
        if note["id"] == note_id:
            note["title"] = input("Введите новый заголовок заметки: ")
            note["text"] = input("Введите новый текст заметки: ")
            note["updated_at"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            break
    else:
        print("Заметка с указанным идентификатором не найдена")

# Функция для удаления заметки
def delete_note():
    note_id = input("Введите идентификатор заметки для удаления: ")
    notes = read_notes()
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            break
    else:
        print("Заметка с указанным идентификатором не найдена")

# Главная функция для работы с заметками
def main():
    while True:
        print("Выберите действие:")
        print("1. Создать заметку")
        print("2. Просмотреть список заметок")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выйти")

        choice = input("Введите номер действия: ")

        if choice == "1":
            note = create_note()
            save_note(note)
            print("Заметка успешно создана")

        elif choice == "2":
            notes = read_notes()
            for note in notes:
                print(f"Идентификатор: {note['id']}")
                print(f"Заголовок: {note['title']}")
                print(f"Текст: {note['text']}")
                print(f"Дата создания: {note['created_at']}")
                print("")

        elif choice == "3":
            edit_note()

        elif choice == "4":
            delete_note()

        elif choice == "5":
            break

        else:
            print("Неверный выбор. Попробуйте еще раз.")

if __name__ == "__main__":
    main() 