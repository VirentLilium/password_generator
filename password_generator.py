import random
import string

symbol_groups = {
    'цифры': string.digits,
    'строчные буквы': string.ascii_lowercase,
    'прописные буквы': string.ascii_uppercase,
    'знаки пунктуации': string.punctuation
}
ambiguous_symbols = 'il1Lo0O'  # сомнительные символы


def get_int_input(prompt, min_value=None, max_value=None):
    """
       Запрашивает у пользователя целое число с возможной проверкой диапазона

       Prompts the user for an integer with optional range validation
       """
    while True:
        try:
            value = int(input(prompt))
            if (min_value is not None and value < min_value):
                print(f"Число должно быть не меньше {min_value}.")
                continue
            if (max_value is not None and value > max_value):
                print(f"Число должно быть не больше {max_value}.")
                continue
            return value

        except ValueError:
            print("Ошибка! Пожалуйста, введите целое положительное число.")


def get_yes_no_input(prompt):
    """
       Запрашивает у пользователя ответ 'да' или 'нет' в разных формах

       Prompts the user for a yes/no answer
       """
    while True:
        answer = input(prompt).strip().lower()
        if answer in ['да', 'lf', 'yes', '+']:
            return True
        elif answer in ['нет', 'ytn', 'no', '-']:
            return False
        else:
            print("Некорректный ответ! Введите 'да' или 'нет'.")


def get_user_settings():
    """
        Запрашивает у пользователя, какие группы символов включать в пароль,
        и следует ли исключать неоднозначные символы.

        Asks the user which character groups to include in the password,
        and whether to exclude ambiguous characters.
        """
    selected_groups = dict()

    for key, value in symbol_groups.items():
        include = get_yes_no_input(f"Включать ли в пароль {key}?")
        if include:
            selected_groups[key] = value

    if not selected_groups:
        print("Вы не выбрали ни одну группу символов. Пожалуйста, выберите хотя бы одну.")
        return get_user_settings()

    exclude_ambiguous = get_yes_no_input(f"Исключить ли неоднозначные символы {ambiguous_symbols}?")

    return selected_groups, exclude_ambiguous


def prepare_symbols(groups, remove_ambiguous):
    """
       Подготавливает символы для генерации пароля:
       объединяет выбранные группы, и при необходимости удаляет неоднозначные символы.

       Prepares characters for password generation:
       merges selected groups and removes ambiguous symbols if needed.
       """
    if remove_ambiguous:
        groups_without_ambiguous = {k: ''.join([ch for ch in v if ch not in ambiguous_symbols]) for k, v in
                                    groups.items()}
        s = ''.join(
            value for key, value in groups_without_ambiguous.items())  # строка со всеми символами, кроме сомнительных
        return groups_without_ambiguous, s
    else:
        s = ''.join(value for key, value in groups.items())  # строка со всеми символами

    return groups, s


def generate_password(groups, length, char_pool):
    """
       Генерирует один пароль заданной длины:
       включает хотя бы по одному символу из каждой выбранной группы,
       и заполняет оставшиеся символы случайными из общего набора.

       Generates a password of given length:
       includes at least one character from each selected group,
       and fills the rest with random characters from the full pool.
       """
    password = []
    for key, value in groups.items():
        password.append(random.choice(value))

    while len(password) < length:
        password.append(random.choice(char_pool))

    random.shuffle(password)
    password = ''.join(password)
    return password


def main():
    """
       Основная функция: управляет вводом пользователя,
       собирает настройки и генерирует указанные пароли.

       Main function: handles user input,
       collects settings and generates the requested number of passwords.
       """
    pwd_quantity = get_int_input('Сколько паролей вам нужно сгенерировать? Введите число. ', min_value=1, max_value=100)

    pwd_length = get_int_input(
        'Какой длины должен быть пароль? Введите число, пароль должен включать от 8 до 20 символов включительно. ',
        min_value=8, max_value=20)

    selected_groups, exclude_ambiguous = get_user_settings()
    groups_of_symbols, char_pool = prepare_symbols(selected_groups, exclude_ambiguous)

    for _ in range(pwd_quantity):
        print(generate_password(groups_of_symbols, pwd_length, char_pool))


main()
