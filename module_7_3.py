import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    content = file.read().lower()  # Приводим к нижнему регистру
                    # Убираем пунктуацию и тире
                    content = content.translate(str.maketrans('', '', string.punctuation + '-'))
                    words = content.split()  # Разделяем строку на слова
                    all_words[file_name] = words  # Добавляем в словарь
            except FileNotFoundError:
                print(f"Файл {file_name} не найден.")
        return all_words

    def find(self, word):
        result = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            if word.lower() in words:
                result[file_name] = words.index(word.lower()) + 1  # Позиция слова (с 1)
        return result

    def count(self, word):
        result = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            count = words.count(word.lower())
            if count > 0:
                result[file_name] = count
        return result

# Пример использования
finder2 = WordsFinder('test_file.txt')

# Получение всех слов
print(finder2.get_all_words())  # Возвращает словарь со словами

# Поиск позиции слова
print(finder2.find('TEXT'))
# Подсчет количества слова
print(finder2.count('teXT'))
