immutable_var = tuple([1, 'String', False])
print('Immutable tuple:', immutable_var)
immutable_var[0] = 3
print(immutable_var)
#Кортеж-неизменяемый объект, он не поддерживает обращение по элементам

mutable_list = [1, 2, True, 'String']
mutable_list[2] = 'Modified'
print(mutable_list)