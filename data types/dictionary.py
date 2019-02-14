# -*- coding: utf-8 -*-

dict = {1:'tuples', 2:False, 3:555, 4:[1, 'mass', 3], 5:{'one','two'}}						#Объявление словаря
print ("\n")
print(dict)
print ("\n")

print(dict[4])
print ("\n")

dict[1] = True										#замена значения первого элемента(перезапись)
print (dict)
print ("\n")

dict['k'] = 123
print (dict)

print (dict.keys())									#все ключи

print (dict.values())								#все значения ключей

print (dict.items())								#кортежирование словаря