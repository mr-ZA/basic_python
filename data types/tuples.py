# -*- coding: utf-8 -*-
p = ('tuples', 'learning')

print (len(p))
print (p)

print (p[0] + " is fun to learn!")

#will be an  error, 'cause tuples can't be assigned!
#p[0] = "t"

#error too
#print ("метод POP: [" + p.pop(3) + "]") 				#Удаляет i-ый элемент и возвращает его.

print(p.index('learning'))								#Индекс слова в кортеже