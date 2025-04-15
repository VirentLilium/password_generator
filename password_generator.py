import random

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
punctuation = ['!', '#', '$', '%', '&', '*', '+', '-', '=', '?', '@', '^', '_', '.']

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
        answer = input(prompt).lower()
        if answer in ['да', 'lf', 'yes', 'нет', 'ytn', 'no']:
            return answer
        else:
            print("Некорректный ответ! Введите 'да' или 'нет'.")

# составляем список символов для генерации пароля
def password_chars():
    chars = []

    if get_yes_no_input('Включать ли в пароль цифры от 0 до 9? ') in ['да', 'lf', 'yes']:
        chars += digits

    if get_yes_no_input('Включать ли в пароль прописные буквы? ') in ['да', 'lf', 'yes']:
        chars += uppercase_letters

    if get_yes_no_input('Включать ли в пароль строчные буквы? ') in ['да', 'lf', 'yes']:
        chars += lowercase_letters

    if get_yes_no_input('Включать ли в пароль символы "!#$%&*+-=?@^_."? ') in ['да', 'lf', 'yes']:
        chars += punctuation

    if get_yes_no_input('Исключать ли неоднозначные символы "il1Lo0O"? ') in ['да', 'lf', 'yes']:
        chars = [ch for ch in chars if ch not in "il1Lo0O"]

    if not chars:
        print("Ошибка: Не выбраны символы для пароля. Пожалуйста, выберите хотя бы одну категорию символов.")
        return password_chars()

    return chars

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
        pwd_len = get_int_input(
            'Какой длины должен быть пароль? Введите число, пароль должен включать минимум 8 символов, максимум 20 символов. ')
        if 8 <= pwd_len <= 20:
            break
        else:
            print('Некорректный ввод - пароль должен включать минимум 8 символов, максимум 20 символов. Введите число. ')

    chars = password_chars()
    for i in range(pwd_quantity):
        print(generate_password(pwd_len, chars))


main()
