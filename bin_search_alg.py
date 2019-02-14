def binary_search(list, item):      #принимаем на вход [список, число для поиска]
	low = 0							              #наименьшее
	high = len(list)-1 				        # элементов в списке как-бы [5], но в списке элементы начинаются с [0]
	
	
	while low <= high:				        #пока low <= high входим 
		index = (low + high)		        #среднее, [4+0, 3+0, 2+0, 1+0]
		guess = list[index]			        #берем элементы list[4]=9, list[3]=7, list[2]=5, list[1]=3
		
		
		if guess == item:			          #9!=3, 7!=3, 5!=3, 3==3
			return index			            #если нашли, то вернуть номер элемента в списке
		
		if guess > item:			          #9>3, 7>3, 5>3
			high = index - 1		          #high=3, 2, 1
		else:
			low = index + 1			          #заглушка в случе если попадется значение не в отсортированном виде, будет low > high

	return "встретилось неотсортированное значение.."
	
my_list = [1, 3, 5, 7, 9]
print (binary_search(my_list, 3))
