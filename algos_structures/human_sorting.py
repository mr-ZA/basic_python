class hSort:
    def human_sorting(self, sValues_arr):
        def human_compare(sourceArr, searchArr):
            for c in range(len(searchArr)):
                if searchArr[c] == sourceArr:
                    founded.append(sourceArr)
                    sValues_arr.pop(c)
                    break

        
        search_values_arr = ["X3_COMMANDO", "X3_GINJEC", "X3_CHAVE", "X3_MODULO", "X3_TAMANHO", "X3_SAVANHO", "X3_HAVANA", "X3_FRACTALO", "X3_PICTURE", "X3_VELJECHO",\
             "X3_FARRANG", "X3_LOVAJA", "X3_NUMERO", "X3_CAVALHO", "X3_NAVARRO"]
        founded = []
        length_search_values = len(sValues_arr)

        for sv in range(len(search_values_arr)):
            if len(sValues_arr) == 0:
                break
            human_compare(search_values_arr[sv], sValues_arr)
        
        if len(founded) == length_search_values:
            print(f'\n[INFO] Successfully found columns in the table -> {founded}')
            return True
        else:
            return False

    def __init__(self):
        sought_values = "X3_TAMANHO, X3_PICTURE"
        sought_values_arr = list(map(str, sought_values.split(', ')))
        sought_values_arr_unlinked = list(sought_values_arr)     # change link of variable id, python assign values as LINK!!!!!

        values_founded = self.human_sorting(sought_values_arr_unlinked)

        if values_founded:
            print(f"[INFO] Operation succesfull, checked by task conditions: {sought_values}")
        else:
            print(f"[ERROR] Operation unsuccesfull, values not found / checked: {sought_values}")

hObj = hSort()