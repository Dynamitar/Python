
def direction(matrix, x , y):
    if matrix[x][y] == 'D' and x < row:
        if x == row - 1:
            return ['END', 0, 0]
        else:
            x += 1
    elif matrix[x][y] == 'U':
        if x == 0:
            return ['END', 0, 0]
        else:
            x -= 1

    elif matrix[x][y] == 'L':
        if y == 0:
            return ['END', 0, 0]
        else:
            y -= 1

    elif matrix[x][y] == 'R' and y < col:
        if y == col - 1:
            return ['END', 0, 0]
        else:
            y += 1

    new_position = matrix[x][y]
    return [new_position, x, y]


def valid_cell(current_direction,next_direction):
    if (current_direction == 'D' and next_direction == 'U') or \
            (current_direction == 'U' and next_direction == 'D') or \
            (current_direction == 'L' and next_direction == 'R') or \
            (current_direction == 'R' and next_direction == 'L'):
        return False
    elif next_direction == 'END':
        return False
    else:
        return True


def path(r, c):
    sum_cells = 1
    movement_history = []
    movement_history.append([r, c])
    while True:
        starting_position = matrix[r][c]
        next_step = direction(matrix, r, c)
        next_direction = next_step[0]
        r = next_step[1]
        c = next_step[2]
        if [r, c] in movement_history:
            break
        else:
            movement_history.append([r, c])
        if next_direction != 'END':
            sum_cells += 1
        if valid_cell(starting_position, next_direction):
            continue
        else:
            break
    return sum_cells


# -----------------------------------------------------------

def open_file(filename):
    with open(filename, mode='rt', encoding='utf-8') as f:
        result = [x[:-1] for x in list(f.readlines())]
        clean_new_lines(result)
    return result


def clean_new_lines(lst):
    for x in lst:
        if x == '':
            lst.remove(x)
    return lst

# --------------------------------------------------------------------
# ____________________STARTING POINT__________________________________

input_data_from_file = 'input.txt'
input_data_from_file = open_file(input_data_from_file)

input_data_from_file = clean_new_lines(input_data_from_file)
# print(input_data_from_file)

test_cases = 0
row = 0
col = 0
matrix = []

counter = 0
second_counter = 0

while counter < len(input_data_from_file):
    if input_data_from_file[counter].isdigit() and ' ' not in input_data_from_file[counter]:
        test_cases = int(input_data_from_file[counter])
        counter += 1

        # loop until all cases are handled
        while second_counter < test_cases:
            temp = input_data_from_file[counter].split(' ')
            row = int(temp[0])
            col = int(temp[1])
            counter += 1

            # iterate to get all rows with directions
            for i in range(row):
                matrix.append(input_data_from_file[counter])
                counter += 1

            # -------------------------------------------------------------
            starting_row = 0
            starting_col = 0

            r = 0
            c = 0
            longest_path = 0
            temp_path = 0
            answers = []

            while r < row:
                while c < col:
                    temp_path = path(r, c)
                    if temp_path > longest_path:
                        longest_path = temp_path
                        starting_row = r
                        starting_col = c
                        answers.clear()
                        answers.append((starting_row + 1, starting_col + 1, longest_path))
                    elif temp_path == longest_path:
                        starting_row = r
                        starting_col = c
                        answers.append((starting_row + 1, starting_col + 1, temp_path))
                    c += 1
                c = 0
                r += 1

            # construct the result
            result = ''
            for answer in answers:
                for letter in answer:
                    result += str(letter) + ' '
                result = result[:-1]
                result += ';'

            print(result[:-1])

            # -------------------------------------------------------------
            matrix.clear()
            second_counter += 1
        second_counter = 0

