my_string = input('Введите произвольную строку: ')
print ('В данной строке: ', len(my_string),'Символов')
print ('Строка верхнем регистре: ',my_string.upper())
print ('Строка в нижнем регистре: ',my_string.lower())
print ('Строка без пробелов: ',my_string.replace(' ', ''))
firstChar=my_string[0]
print ('Первый символ строки: ',firstChar)
lastChar=my_string[-1]
print ('Последний символ строки: ', lastChar)