my_dict = {'Сергей': 1975, 'Татьянаэ': 1982, 'Оксана': 1985}
print(my_dict)
print(my_dict['Сергей'])
my_dict['Василий'] = 1977
print(my_dict)
del my_dict['Сергей']
print(my_dict)


my_set  =  {1,2,3,4,1,4,2,3, 'Сергей', True, (1,2,3,4,5)}
print(my_set)
print(my_set.discard(1))
print(my_set)
