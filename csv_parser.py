import csv
import re

def main():
    with open("full.csv", mode='r', encoding="utf-8") as c_file:
        # list from every element, delimiter = " "
        c_file_output = list(csv.reader(c_file))
        steps = []
        tables = []

        regex_steps = re.compile("step\s.+")
        regex_tables = re.compile("table\s.+")
        regex_values = re.compile("102032.+")

        # for every array one to another from .csv
        for mass in c_file_output:
            print(mass)
            if len(mass) == 0:
                continue

            # steps
            if re.search(regex_steps, mass[0]):
                steps.append(mass[0])


        print("\n")
        print(steps)
        print(tables)
        print(len(c_file_output))   # quantity of arrays
        print("\n")

        columns_DB = []
        values_DB = []
        dict = {}
        flag = True
        i = 3

        for mass in range(len(c_file_output)):

            if len(c_file_output[mass]) == 0:
                continue

            # c_file_output[0][0] = 'table sn4'
            # table -> get -> columnsDB
            if re.search(regex_tables, c_file_output[mass][0]):
                columns_DB.append([c_file_output[mass + 1][0]])

            # get values
            if re.search(regex_values, c_file_output[mass][0]):
                values_DB.append([c_file_output[mass][0]])

        # [[column] = [value]]
        print(columns_DB)
        print(values_DB)

if __name__ == '__main__':
    main()