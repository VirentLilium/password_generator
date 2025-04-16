import random
import string


symbol_groups = {
    'цифры': string.digits,
    'строчные буквы': string.ascii_lowercase,
    'прописные буквы': string.ascii_uppercase,
    'знаки пунктуации': string.punctuation
}
ambiguous = 'il1Lo0O'  # сомнительные символы

# проверяем, что пользователь вводит целое число (количество и длина паролей)
def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка! Пожалуйста, введите число.")


# проверка ответов пользователя "да" и "нет"
def get_yes_no_input(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ['да', 'lf', 'yes', '+']:
            return True
        elif answer in ['нет', 'ytn', 'no', '-']:
            return False
        else:
            print("Некорректный ответ! Введите 'да' или 'нет'.")


# собираем настройки от пользователя для символов в пароле
def get_user_settings():
    selected_groups = dict()

    for key, value in symbol_groups.items():
        include = get_yes_no_input(f"Включать ли в пароль {key}?")
        if include:
            selected_groups[key] = value

    if not selected_groups:
        print("Вы не выбрали ни одну группу символов. Пожалуйста, выберите хотя бы одну.")
        return get_user_settings()

    exclude_ambiguous = get_yes_no_input(f"Исключить ли неоднозначные символы {ambiguous}?")

    return selected_groups, exclude_ambiguous


# генерируем пароль (из каждой группы берем минимум 1 символ, оставшиеся символы дополняем случайными из набора, перемешиваем)
def generate_password(length, chars):
    password = []

    if '1' in chars:
        password.append(random.choice(digits))

    if 'z' in chars:
        password.append(random.choice(lowercase_letters))

    if 'Z' in chars:
        password.append(random.choice(uppercase_letters))

    if '#' in chars:
        password.append(random.choice(punctuation))

    while len(password) < length:
        password.append(random.choice(chars))

    random.shuffle(password)
    return ''.join(password)


# запускаем программу
def main():
    pwd_quantity = get_int_input('Сколько паролей вам нужно сгенерировать? Введите число. ')

    while True:
        pwd_length = get_int_input(
            'Какой длины должен быть пароль? Введите число, пароль должен включать минимум 8 символов, максимум 20 символов. ')
        if 8 <= pwd_length <= 20:
            break
        else:
            print('Некорректный ввод - пароль должен включать минимум 8 символов, максимум 20 символов. Введите число. ')

    selected_groups, exclude_ambiguous = get_user_settings()
    char_pool = prepare_character_pool(selected_groups, exclude_ambiguous)

    for _ in range(pwd_quantity):
        print(generate_password(pwd_length, char_pool))


main()
