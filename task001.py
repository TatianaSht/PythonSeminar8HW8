from msvcrt import getch


def phonebook_menu(path):
    while True:
        phonebook_title()
        print("для выбора доступного режима - введите номер от 1 до 5 и нажмите Enter\nдля выхода из телефонной книги - введите 0 и нажмите Enter")
        user_selection = int(input())
        if user_selection == 1:
            read_phonebook(path)
        elif user_selection == 2:
            add_new_phone(path)
        elif user_selection == 3:
            find_phone(path)
        elif user_selection == 4:
            change_phone(path)
        elif user_selection == 5:
            delete_phone(path)
        elif user_selection == 0:
            print("----Сеанс работы с телефонной книгой завершен. До новых встреч!----")
            print()
            return


def phonebook_title():
    print()
    glob_title = "Главный экран телефонной книги"
    print(f"{glob_title:^42}")
    print("*" * 42)
    print("""Режимы работы в телефонной книге:
          1 - Просмотр всех контактов
          2 - Добавление нового контакта
          3 - Поиск контакта
          4 - Изменение контакта
          5 - Удаление контакта
          0 - Выход из телефонной книги
          """)


def print_phonebook(data):
    print()
    title = 'Список контактов телефонной книги:'
    print(f"{title:^65}")
    phone_book = []
    border_line = "-" * 65
    print(border_line)
    numb_titl = '№'
    suname_titl = 'Фамилия'
    name_titl = 'Имя'
    patronymic_titl = 'Отчество'
    phone_titl = 'Номер телефона'
    print(f"{numb_titl:>2}. {suname_titl:<12} {name_titl:<14} {patronymic_titl:<15}  {phone_titl:<15}")
    print(border_line)
    num_contact = 1
    for contact in data:
        suname, name, patronymic, phone = contact.rstrip().split(",")
        phone_book.append({"ID": num_contact, "name1": suname, "name2": name, "name3": patronymic, "phone": phone, })
        num_contact += 1
    for contact in phone_book:
        num_contact, suname, name, patronymic, phone = contact.values()
        print(f"{num_contact:>2}. {suname:<12} {name:<14} {patronymic:<15}  {phone:<15}")
    print(border_line)


def read_phonebook(path):
    with open(path, "r") as file:
        data = sorted(file.readlines())
        print("\n1. Активирован режим просмотра контактов")
        print_phonebook(data)
    print("\n нажмите любую клавишу для возврата на главный экран => ")
    getch()


def add_new_phone(path):
    print("\n2. Активирован режим добавления нового контакта\n")
    with open(path, "a") as file:
        res = ""
        res += input("Введите фамилию и нажмите Enter: ") + ","
        res += input("Введите имя и нажмите Enter: ") + ","
        res += input("Введите отчество и нажмите Enter: ") + ","
        res += input("Введите телефон и нажмите Enter: ")
        file.write(res + "\n")
    print("\n----Новый контакт добавлен!----")
    print("\n нажмите любую клавишу для возврата на главный экран => ")
    getch()


def find_phone(path):
    print("\n3. Активирован режим поиска котактов\n")
    search_elem = input("Введите поисковое значение и нажмите Enter: ").capitalize()
    search_list = []
    with open(path, "r") as file:
        data = file.readlines()
        for contact in data:
            if search_elem in contact:
                search_list.append(contact)
    if len(search_list) != 0:
        print()
        print(f"По запросу '{search_elem}' найдены записи: ")
        print_phonebook(search_list)
    else:
        print(f"Не найден контакт с введенным поисковым значением '{search_elem}'.")
    print("\n нажмите любую клавишу для возврата на главный экран => ")
    getch()


def change_phone(path):
    print("\n4. Активирован режим изменения контактов")
    with open(path, "r") as file:
        phone_book = sorted(file.readlines())
        print_phonebook(phone_book)
        print("для редактирования - введите № записи из списка контактов и нажмите Enter \nдля возврата на главный экран - введите 0 и нажмите Enter")
        num_contact = int(input())
        if num_contact != 0:
            print(f"Для редактирования записи: {phone_book[num_contact - 1].rstrip().split(',')}")
            new_suname = input("Ввведите фамилию и нажмите Enter: ")
            new_name = input("Введите имя и нажмите Enter: ")
            new_patronymic = input("Введите отчество и нажмите Enter: ")
            new_phone = input("Введите номер телефона и нажмите Enter: ")
            phone_book[num_contact - 1] = (new_suname + "," + new_name + "," + new_patronymic + "," + new_phone + "\n")
            with open(path, "w") as file:
                file.write("".join(phone_book))
                print("\nЗапись в книге успешно изменена!")
                print("\n нажмите любую клавишу для возврата на главный экран => ")
                getch()
        else:
            return


def delete_phone(path):
    print("\n5. Активирован режим удаления контактов!")
    with open(path, "r+") as file:
        phone_book = sorted(file.readlines())
        print_phonebook(phone_book)
        print("для удаления - введите № записи из списка контактов и нажмите Enter \nдля возврата на главный экран - введите 0 и нажмите Enter")
        num_contact = int(input())
        if num_contact != 0:
            print(f"Запись: {phone_book[num_contact - 1].rstrip().split(',')} успешно удалена!\n")
            phone_book.pop(num_contact - 1)
            with open(path, "w") as file:
                file.write("".join(phone_book))
        else:
            return
    print("\n нажмите любую клавишу для возврата на главный экран => ")
    getch()


path = 'phonesbook.txt'

phonebook_menu(path)
