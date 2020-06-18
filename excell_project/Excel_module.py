import pandas as pd
from tkinter import *
from openpyxl import workbook

class MainProgr():

    def insert(self, file, value, col, cell, header_list, tex):
        print('File[-s] for inserting in: ' + file)
        print('Column position(entry): ' + col)
        print('Cell position(entry) : ' + cell)
        print('Value for insert in: ' + '123')

        col = header_list[int(col) - 1]
        cell = int(cell) - 1

        file = file.split(" ")
        print(file)
        print(type(file))

        try:
            for f in file:
                df = pd.read_excel(f, sheet_name='Sheet1')

                print(df.head())
                df.set_value(cell, col, value)  # cell_n, col_n, val
                # newer version, need todo tests
                # df.iat[1, 1] = '123'
                print("\n")
                print(df.head())

                df.to_excel(f, sheet_name='Sheet1', index=False)
        except PermissionError:
            tex.insert(END, "\n\nОШИБКА!\nЗакройте файлы и \nпопробуйте снова")
            return
        except FileNotFoundError:
            tex.insert(END, "\n\nОШИБКА!\nФайла[-ов] не существует в данной директории\n")

            # writer = pd.ExcelWriter("pandas_datetime_format.xlsx",
            #                         engine='xlsxwriter'
            #
            # df.to_excel(writer, sheet_name='Sheet1')
            #
            # workbook = writer.book
            # worksheet = writer.sheets['Sheet1']
            #
            # format_bc = workbook.add_format({
            #     'font_name': 'Arial',
            #     'font_size': 14,
            #     'font_color': 'white',
            #     'bold': 0,
            #     'border': 1,
            #     'align': 'left',
            #     'valign': 'vcenter',
            #     'text_wrap': 1,
            #     'fg_color': '#005581'})
            # worksheet.set_column('B:C', 20, format_bc)
            # writer.save()

    def read(self, tex, filename_entry, col_name_entry, cell_pos_entry, filename_insert_entry, col_name_insert_entry, cell_name_insert_entry):

        print ('Button clicked')
        print ('File name: ' + filename_entry)
        print('Cell position: ' + cell_pos_entry)
        print('Column position: ' + col_name_entry + "\n")
        tex.delete (0.0, END)

        if not filename_entry:
            df = pd.read_excel('MODULE_NAME.xlsx', sheet_name='Sheet1')
        else:
            try:
                df = pd.read_excel("{}".format(filename_entry), sheet_name='Sheet1')

            except FileNotFoundError:
                print("Файл отсутствует в рабочей папке!\n")
                return

        c_list = [] #for all columns
        c_list_contains = [] #for all values in all columns
        col_name_entry = int(col_name_entry) - 1  # str entered to int
        cell_pos_entry = int(cell_pos_entry) - 1

        print("Column headings:")
        print(df.columns)
        print("\n")

        # get all columns from file [pandas] -> list
        for d in df.columns:
            c_list.append(d)

        # заполнение массива содержимыми данными в виде массивов других колонок
        for v in c_list:
            c_list_contains.append(df[v].tolist())

        tex.insert (END, "Значение в ячейке [" + c_list_contains[col_name_entry][cell_pos_entry] + "]")
        value = c_list_contains[col_name_entry][cell_pos_entry]     # вытянутое из ячейки файла значение

        self.insert (filename_insert_entry, value, col_name_insert_entry, cell_name_insert_entry, c_list, tex)

def main():
    root = Tk()  # экземпляр главного окна
    root.title("Zmodule")  # title окна
    root.geometry("800x600")  # размер окна
    prObj = MainProgr()

    filename_text = StringVar()
    colname_text = StringVar()
    cellpos_text = StringVar()

    filename_insert_text = StringVar()
    colname_insert_text = StringVar()
    cellpos_insert_text = StringVar()

    filename = Label(text="Имя файла: ")
    col_name = Label(text="№ столбца: ")
    cell_pos = Label(text="№ ячейки: ")

    filename_insert = Label(text="Имя файла для вставки: ")
    col_name_insert = Label(text="№ столбца: ")
    cell_name_insert = Label(text="№ ячейки: ")
    separator = Label (text = "________________________")
    separator_col = Label(text="________________________")
    tex = Text(root, height=10, width=30)

    filename_entry = Entry (textvariable = filename_text)# поле для ввода имени ориг файла excell
    col_name_entry = Entry(textvariable = colname_text)  # поле для ввода колонки
    cell_pos_entry = Entry(textvariable = cellpos_text)  # поле для ввода ячейки

    filename_insert_entry = Entry(textvariable = filename_insert_text)  # поле для ввода имени файла в который вставка
    col_name_insert_entry = Entry(textvariable = colname_insert_text)  # поле для ввода имени колонки файла в который вставка
    cell_name_insert_entry = Entry(textvariable = cellpos_insert_text)  # поле для ввода имени ячейки файла в который вставка

    filename.grid(row = 0, column = 0, sticky = "w")
    filename_entry.grid(row = 0, column = 1, pady = 4, sticky = "w")
    col_name.grid(row=1, column=0, sticky="w")
    col_name_entry.grid(row=1, column=1, pady = 4, sticky="w")
    cell_pos.grid(row=2, column=0, sticky="w")
    cell_pos_entry.grid(row=2, column=1, pady=4, sticky="w")

    separator.grid(row=3, column=0, pady=10, sticky="w")
    separator_col.grid(row=3, column=1, pady=10, sticky="w")

    filename_insert.grid(row=4, column=0, pady=6, sticky="w")
    filename_insert_entry.grid(row=4, column=1, pady=6, sticky="w")
    col_name_insert.grid(row=5, column=0, pady=6, sticky="w")
    col_name_insert_entry.grid(row=5, column=1, pady=6, sticky="w")
    cell_name_insert.grid(row=6, column=0, pady=6, sticky="w")
    cell_name_insert_entry.grid(row=6, column=1, pady= 6, sticky="w")

    tex.grid(row = 7, column = 1, pady = 10, sticky = "w")

    message_button = Button(text="CHECK", command=lambda: prObj.read(tex, filename_entry.get(), col_name_entry.get(), cell_pos_entry.get(), filename_insert_entry.get(), col_name_insert_entry.get(), cell_name_insert_entry.get())) # button
    message_button.grid(row=9, column=1, sticky="w")

    root.mainloop()

if __name__ == '__main__':
    main()