"""Тесты для генератора паролей."""

from password_generator import (
    ambiguous_symbols,
    generate_password,
    prepare_symbols,
)


def test_prepare_symbols_removes_ambiguous_symbols() -> None:
    """
    Проверяет удаление неоднозначных символов
    из выбранных групп символов.
    """
    groups = {
        'digits': '0123456789',
        'letters': 'abciloO',
    }

    prepared_groups, char_pool = prepare_symbols(
        groups,
        remove_ambiguous=True,
    )

    for symbol in ambiguous_symbols:
        assert symbol not in char_pool

    assert prepared_groups == {
        'digits': '23456789',
        'letters': 'abc',
    }


def test_prepare_symbols_keeps_symbols_if_remove_ambiguous_is_false() -> None:
    """
    Проверяет, что символы не изменяются,
    если удаление неоднозначных символов отключено.
    """
    groups = {
        'digits': '0123456789',
        'letters': 'abciloO',
    }

    prepared_groups, char_pool = prepare_symbols(
        groups,
        remove_ambiguous=False,
    )

    assert prepared_groups == groups
    assert char_pool == '0123456789abciloO'


def test_generate_password_returns_password_with_required_length() -> None:
    """
    Проверяет, что длина сгенерированного пароля
    соответствует запрошенной длине.
    """
    groups = {
        'digits': '123',
        'letters': 'abc',
    }
    char_pool = '123abc'

    password = generate_password(
        groups=groups,
        length=10,
        char_pool=char_pool,
    )

    assert len(password) == 10


def test_generate_password_uses_only_allowed_symbols() -> None:
    """
    Проверяет, что пароль содержит только символы
    из разрешённого набора.
    """
    groups = {
        'digits': '123',
        'letters': 'abc',
    }
    char_pool = '123abc'

    password = generate_password(
        groups=groups,
        length=20,
        char_pool=char_pool,
    )

    assert set(password).issubset(set(char_pool))


def test_generate_password_contains_symbol_from_each_selected_group() -> None:
    """
    Проверяет, что пароль содержит хотя бы один символ
    из каждой выбранной группы.
    """
    groups = {
        'digits': '123',
        'letters': 'abc',
        'punctuation': '!?',
    }
    char_pool = '123abc!?'

    password = generate_password(
        groups=groups,
        length=12,
        char_pool=char_pool,
    )

    assert any(char in groups['digits'] for char in password)
    assert any(char in groups['letters'] for char in password)
    assert any(char in groups['punctuation'] for char in password)
