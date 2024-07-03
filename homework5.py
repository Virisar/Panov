immutable_var = 1, True, 'string'
print('Картеж: ',immutable_var)

# immutable_var[0]=5
# print(immutable_var)
# Картеж нельзя редактировать или как-либо изменять, они служат для хранения информации

mutable_list = [1, True, 'string']
print('Список: ', mutable_list)
mutable_list[0]=5
print('Измененный Список: ',mutable_list)