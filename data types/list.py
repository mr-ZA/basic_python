# -*- coding: utf-8 -*-
print ("\n")
listt = ['s', 'p', ['isok'], 3]					#разные типы данных в списке
print (listt)
print ("\n")
listt.append([9, 8, 7])
print (listt)
print ("\n")
print ("вложенный элемент списка пятый и внутри первый: [" + str (listt[-1][0]) + "]")
print ("\n")
print ("элемент с конца: [" + str(listt[-1]) + "]")	#элемент с конца и преобразование тк конкатенация str + int НЕ РАБОТАЕТ
print ("\n")
listt.insert (0, 'a')							 	#поставить на первое место букву [a s p isok 3]
print (listt)
print ("\n")
listt.append("three")							 	#добавить в конец списка слово
print (listt)
print ("\n")
listt.remove ('a')								 	#убрать первую добавленную в список букву
print (listt)
print ("\n")
print ("метод POP: [" + str(listt.pop(3)) + "]") 	#Удаляет i-ый элемент и возвращает его.
print ("\n")
print("index of \'p\' is: ")
print(listt.index('p'))								#Индекс буквы 'p' в списке
print ("\n")
print (listt.reverse())								#разворачиваем список
print (listt)
print ("\n")

c = [c * 3 for c in 'list']							#генератор списков
print (c)
print ("\n")

# c + d, кроме [iii], кроме буквы [aaa] в spam
c = [c + d for c in 'list' if c != 'i' for d in 'spam' if d != 'a']
print (c)
print ("\n")