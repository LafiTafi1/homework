from online import get_actual_currencies

# 1. Приветствие
# 2. Мануал – как пользоваться программой и какие валюты доступны
# 3. Ввести исходную валюту
# 4. Ввести в какую валюту перевести
# 5. Количество валюты
# 6. Подсчёт
# 7. Вывод результата

CURRENCIES = get_actual_currencies()


def convert(amount1, from_currency, to_currency, currencies):
    from_value = currencies.get(from_currency)
    to_value = currencies.get(to_currency)

    coefficient = to_value / from_value
    return round(amount1 * coefficient, 2)


def is_there_a_currency(currency: str, dict_currencies: dict) -> bool:
    return bool(dict_currencies[currency])


# 1
print("Добро пожаловать в конвертатор валют!")
# 2
print("""
Инструкция:
1. Ввести исходную валюту
2. Ввести результирующую валюту
3. Ввести количество валюты
""")

print("Доступные валюты:")

for key in CURRENCIES['data']:
    print(f"* {key}")

# 3
while True:
    current_currency = (input("Введите исходную валюту: ")).upper()
    if current_currency not in CURRENCIES['data']:
        print('Такой валюты нет в списке. Повторите попытку.')
    else:
        break

# 4
while True:
    result_currency = (input("Введите результирующую валюту: ")).upper()
    if result_currency not in CURRENCIES['data']:
        print('Такой валюты нет в списке. Повторите попытку.')
    else:
        break
# 5
amount = input("Введите количество: ")

# 6
result = convert(float(amount), current_currency, result_currency, CURRENCIES['data'])

print(f'{amount} {current_currency} = {result} {result_currency}')
