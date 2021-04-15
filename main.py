import json
import random

# Создаем список из букв, которые будет нажимать обезьяна
letters = 'aбвгдеёжзийклмнопрстуфхцчшщыьъэюя'

# Здесь гениальный код, вызывающий генерацию рандомного слова в цикле.
# Попыток всего миллиард, чтобы было интереснее
for x in range(100):
    n = 1000000000
    attempt_count = 0  # Счетчик попыток
    successful_attempts = 0  # Номер попытки, которая была успешной
    days_on_try = 0  # Количество дней, затраченных на попытку
    dead_monkey = ()  # Умерла ли обезьяна
    cup_is_full = ()  # Наполнилась ли пиала
    for j in range(n):
        attempt = 1
        random_word = ''.join(random.choice(letters) for i in range(5))  # Самая генерация слова
        attempt_count += attempt
        days = attempt_count / 1000  # Количество дней

        # Проверяем, была ли попытка успешной
        if random_word == 'банан':
            successful_attempts += attempt_count
            days_on_try += days
            break
        else:
            pass

        # Считаем, умерла ли обезьяна. Примем за возраст обезьяны 10000 дней (около 27 лет)
        if attempt_count / 1000 == 10000:
            dead_monkey = 'Да'
            days_on_try += days
            break
        else:
            dead_monkey = 'Нет'
            pass

        # Допустим, что одна капля = 1мл. Каждый день капает одна капля и испаряется 0,5мл.
        # Тогда пиала наполняется водой за 800 дней, проверяем это,
        # если прошло больше 800 дней - программа останавливается
        if days/800 >= 1:
            cup_is_full = 'Да'
            days_on_try += days
            break
        else:
            cup_is_full = 'Нет'
            pass

    # Генерируем словарь, в который записываем результат проверок
    data = {'Номер теста: ': str(x),
            'Количество затраченных дней: ': str(days_on_try),
            'Успешная попытка № ': str(successful_attempts),
            'Умерла ли обезьяна? ': str(dead_monkey),
            'Наполнилась ли пиала? :': str(cup_is_full)
            }
    print(data)

    with open(f'stat{x}.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
