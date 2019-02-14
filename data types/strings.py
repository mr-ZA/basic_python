# -*- coding: utf-8 -*-
str
s1 = 'строка'
s2 = "строка2"
s3 = '''многострочный
комментарий, используется так-же как
описание модуля, методов и тд (docstring)'''

print (s1, s2, "\n", s3)										#через запятую значит отступ
print ("\n")
																#однако в тройных кавыках переход учитывается как новая строка

name = 'Python'																
ver = 3.5

#s = 'Name is: ' + name + ', versoin: ' + ver					#будет ошибка тк строки можно складывать только со строками
s = 's1 Name is: ' + name + ', versoin: ' + str (ver)				#преобразование типа float -> string
print (s)
print ("\n")

str2 = "s2 Name is %s, version: %.1f" %(name, ver)			#явное подставление в строку переменной как в СИ и 1 знак после запятой
print (str2)
print ("\n")

str3 = "s3 Name is %s, version: %+10f" %(name, ver)			#подставление с 10 пробелами слева
print (str3)
print ("\n")

str4 = "s4 Name is %-10s, version: %f" %(name, ver)			#подставление с 10 пробелами справа
print (str4)
print ("\n")

str5 = "s5 Name is %s, version: %.*f" %(name, 2, ver)		#подставление с 2-умя знаками от float
print (str5)
print ("\n")

print ("s6 Name is %s, version: %d" %(name, ver))			#неявное преобразование float -> int
print ("\n")

print ("s7 Name is {0}, version: {1}" .format (name, ver))	#другой формат подставления в строку
#----------------------------------------------------------------------------------------------------------------------------------