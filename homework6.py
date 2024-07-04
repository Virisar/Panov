#Работа со славорем:
my_dict = {'Сергей': 1991, 'Виктор': 1990}
print(my_dict)
print(my_dict['Сергей'])
my_dict.update({'Игорь':1995, 'Николай':1989})
print(my_dict)
a = my_dict.pop('Виктор')
print(a)
print(my_dict)

# Работа с множествами:
my_set = {1, 2, 3, 4, 5, 5, 4, 4, 3, 2, 1, 1, 56.25, 'String', (1, 2, 3, 4, 4), (1, 2, 3, 4, 4)}
print('Множества: ',my_set)
my_set.update([6,7])
print(my_set)
