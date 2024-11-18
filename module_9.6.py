def all_variants(text):
    length = len(text)

    # Генерируем все подпоследовательности
    for i in range(length):
        for j in range(i + 1, length + 1):
            yield text[i:j]


# Пример использования
a = all_variants("abc")
for i in a:
    print(i)