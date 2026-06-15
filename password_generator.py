import random
import string

symbol_groups: dict[str, str] = {
    'цифры': string.digits,
    'строчные буквы': string.ascii_lowercase,
    'прописные буквы': string.ascii_uppercase,
    'знаки пунктуации': string.punctuation
}

ambiguous_symbols = 'il1Lo0O'  # сомнительные символы


def get_int_input(
    prompt: str,
    min_value: int | None = None,
    max_value: int | None = None,
) -> int:
    """
    Запрашивает у пользователя целое число.

    При необходимости проверяет, что число входит в заданный диапазон.

    :param prompt: Текст приглашения для ввода.
    :param min_value: Минимально допустимое значение.
    :param max_value: Максимально допустимое значение.
    :return: Корректное целое число.
    """
    while True:
        try:
            value = int(input(prompt))

            if (min_value is not None and value < min_value):
                print(f'Число должно быть не меньше {min_value}.')
                continue

            if (max_value is not None and value > max_value):
                print(f'Число должно быть не больше {max_value}.')
                continue

            return value

        except ValueError:
            print('Ошибка! Пожалуйста, введите целое положительное число.')


def get_yes_no_input(prompt: str) -> bool:
    """
    Запрашивает у пользователя ответ "да" или "нет".

    Допускает несколько вариантов положительного и отрицательного ответа.

    :param prompt: Текст вопроса для пользователя.
    :return: True для положительного ответа, False для отрицательного.
    """
    while True:
        answer = input(prompt).strip().lower()

        if answer in ['да', 'lf', 'yes', '+']:
            return True

        if answer in ['нет', 'ytn', 'no', '-']:
            return False

        print('Некорректный ответ! Введите "да" или "нет".')


def get_user_settings() -> tuple[dict[str, str], bool]:
    """
    Запрашивает пользовательские настройки генерации пароля.

    Пользователь выбирает группы символов для пароля и решает,
    нужно ли исключать неоднозначные символы.

    :return: Кортеж из выбранных групп символов и флага исключения
        неоднозначных символов.
    """
    while True:
        selected_groups: dict[str, str] = {}

        for key, value in symbol_groups.items():
            include = get_yes_no_input(
                f'Включать ли в пароль {key}? '
            )

            if include:
                selected_groups[key] = value

        if selected_groups:
            break

        print(
            'Вы не выбрали ни одну группу символов. '
            'Пожалуйста, выберите хотя бы одну.'
        )

    exclude_ambiguous = get_yes_no_input(
        f'Исключить ли неоднозначные символы {ambiguous_symbols}?'
    )

    return selected_groups, exclude_ambiguous


def prepare_symbols(
    groups: dict[str, str],
    remove_ambiguous: bool,
) -> tuple[dict[str, str], str]:
    """
    Подготавливает символы для генерации пароля.

    Объединяет выбранные группы символов в общий набор. Если нужно,
    удаляет из выбранных групп неоднозначные символы.

    :param groups: Выбранные пользователем группы символов.
    :param remove_ambiguous: Нужно ли удалить неоднозначные символы.
    :return: Кортеж из обновлённых групп символов и общего набора символов.
    """
    if remove_ambiguous:
        groups = {
            key: ''.join(
                char for char in value if char not in ambiguous_symbols
            )
            for key, value in groups.items()
        }

    # строка со всеми символами, кроме сомнительных
    char_pool = ''.join(groups.values())

    return groups, char_pool


def generate_password(
    groups: dict[str, str],
    length: int,
    char_pool: str,
) -> str:
    """
    Генерирует пароль заданной длины.

    Пароль содержит хотя бы один символ из каждой выбранной группы.
    Остальные символы выбираются случайно из общего набора.

    :param groups: Группы символов для генерации пароля.
    :param length: Длина пароля.
    :param char_pool: Общий набор разрешённых символов.
    :return: Сгенерированный пароль.
    """
    password_chars = [
        random.choice(chars) for chars in groups.values()
    ]

    while len(password_chars) < length:
        password_chars.append(random.choice(char_pool))

    random.shuffle(password_chars)

    return ''.join(password_chars)


def main() -> None:
    """Функция запускает генератор паролей."""
    pwd_quantity = get_int_input(
        'Сколько паролей вам нужно сгенерировать? Введите число. ',
        min_value=1,
        max_value=100,
    )

    pwd_length = get_int_input(
        'Какой длины должен быть пароль? '
        'Введите число, пароль должен включать '
        'от 8 до 20 символов включительно. ',
        min_value=8,
        max_value=20,
    )

    selected_groups, exclude_ambiguous = get_user_settings()

    groups_of_symbols, char_pool = prepare_symbols(
        selected_groups,
        exclude_ambiguous
    )

    for _ in range(pwd_quantity):
        print(
            generate_password(
                groups_of_symbols,
                pwd_length,
                char_pool,
            )
        )


if __name__ == '__main__':
    main()
