#C:\Users\YOUR\FILE\PATH
import openpyxl


def find_substring_in_columns(file_path, search_substring):
    wb = openpyxl.load_workbook(file_path)
    ws = wb.active

    found_columns = []

    for col in ws.iter_cols():
        column_name = col[0].value
        found_in_col = []
        for cell in col:
            if search_substring in str(cell.value):
                found_in_col.append(cell.row)

        if found_in_col:
            found_columns.append((column_name, found_in_col))

    return found_columns


def main(file_path, search_substring):
    found_columns = find_substring_in_columns(file_path, search_substring)

    if found_columns:
        print(f"{search_substring} найдена в следующих столбцах:")
        for column, rows in found_columns:
            print(f" {column}", end=' ')
    else:
        print('Подстрока не найдена.')


if __name__ == '__main__':
    pattern_list = ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']
    file_path = input('Путь до файла: ')
    for pattern in pattern_list:
        main(file_path, pattern)
        print()
