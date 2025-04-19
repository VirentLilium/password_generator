# 🔐 Генератор надёжных паролей

Консольная программа на Python для генерации надёжных паролей с гибкой пользовательской настройкой.  

---

## Возможности

- Генерация одного или нескольких паролей
- Выбор, какие группы символов включать:
  - Цифры (`0-9`)
  - Строчные буквы (`a-z`)
  - Прописные буквы (`A-Z`)
  - Знаки пунктуации (`!@#$%...`)
- Исключение неоднозначных символов (`il1Lo0O`)
- Указание длины пароля (от 8 до 20 символов включительно)

---

## Особенности

- Пользователь сам выбирает, какие символы будут использоваться: цифры, строчные и прописные буквы, знаки пунктуации.
- Можно исключить неоднозначные символы (например, il1Lo0O), чтобы избежать путаницы.
- Умная генерация паролей: скрипт гарантирует, что в каждом пароле будет как минимум по одному символу из каждой выбранной группы. Оставшиеся символы добираются случайным образом из общего пула, после чего пароль перемешивается.
- Генерация сразу нескольких паролей по заданным параметрам.

## Как использовать
```
git clone https://github.com/VirentLilium/password_generator.git
cd password_generator
python password_generator.py
```

## Пример использования
Сколько паролей вам нужно сгенерировать? Введите число. 3

Какой длины должен быть пароль? Введите число, пароль должен включать от 8 до 20 символов включительно. 12

Включать ли в пароль цифры? да

Включать ли в пароль строчные буквы? да

Включать ли в пароль прописные буквы? нет

Включать ли в пароль знаки пунктуации? да

Исключить ли неоднозначные символы il1Lo0O? да

Результат:

g7#n3*z@rpqe

8%m!b9h&yqru

9@d^j5$cwzse
