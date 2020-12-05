import re


def read_input_as_list(filename):
    return [line for line in open(filename, 'r')]


def find_row(code, rows):
    #print(f"Code: {code}\t{rows}")
    if len(rows) == 1:
        return rows[0]
    elif pow(2, len(code)) < len(rows):
        raise Exception(f"'{code}' gives not enough information to find a row between {len(rows)} rows")
    elif re.match('[^BF]', code):
        raise Exception("Code contains illegal characters")
    elif code[0] == "F":
        return int(find_row(code[1:], rows[:len(rows) // 2]))
    else:
        return int(find_row(code[1:], rows[len(rows) // 2:]))


def find_column(code, column):
    #print(f"Code: {code}\t{column}")
    if len(column) == 1:
        return column[0]
    elif pow(2, len(code)) < len(column):
        raise Exception(f"'{code}' gives not enough information to find a column between {len(columns)} columns")
    elif re.match('[^LR]', code):
        raise Exception("Code contains illegal characters")
    elif code[0] == "L":
        return int(find_column(code[1:], column[:len(column) // 2]))
    else:
        return int(find_column(code[1:], column[len(column) // 2:]))


def find_seat_id(row, column):
    return (8 * row) + column


if __name__ == '__main__':
    plane_rows = list(range(0, 128))
    plane_columns = list(range(0, 8))
    ids = []

    for code in read_input_as_list("5.txt"):
        row_code, column_code = re.match(r"([BF]+)([RL]+)", code).groups()
        row = find_row(row_code, plane_rows)
        column = find_column(column_code, plane_columns)
        seat_id = find_seat_id(row, column)
        ids.append(seat_id)

    ids.sort()
    print(f"The highest seat id is {ids[-1]}")
    for i, id in enumerate(ids):
        if ids[i+1] != id + 1:
            print(f"Your seat has the id: {id + 1}")
            break
