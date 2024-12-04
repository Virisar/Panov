def introspection_info(obj):
    # Создаем словарь для хранения информации об объекте
    info = {
        'type': type(obj).__name__,  # Получаем тип объекта
        'attributes': [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith('__')],
        # Получаем атрибуты объекта
        'methods': [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith('__')],
        # Получаем методы объекта
        'module': obj.__module__,  # Получаем модуль, к которому принадлежит объект
    }
    return info  # Возвращаем собранную информацию


# Пример использования функции интроспекции
class SampleClass:
    def __init__(self, value):
        self.value = value  # Инициализируем атрибут объекта

    def display(self):
        return self.value  # Метод для отображения значения


sample_obj = SampleClass(10)  # Создаем экземпляр класса SampleClass
info = introspection_info(sample_obj)  # Вызываем функцию интроспекции для объекта
print(info)  # Печатаем полученную информацию

