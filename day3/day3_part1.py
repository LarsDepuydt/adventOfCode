def is_special(test_char):
    if not test_char.isnumeric() and test_char != '.':
        return True
    else:
        return False


def add_number(l, c_i, current_i, ls, l_i):
    first_line_number = c_i - len(current_i) - 1
    last_line_number = c_i

    if first_line_number < 0:
        first_line_number = 0
    if last_line_number >= len(l):
        last_line_number = c_i - 1

    if is_special(l[first_line_number]) or is_special(l[last_line_number]):
        return True

    if l_i - 1 >= 0:
        previous_line = ls[l_i - 1]
    else:
        previous_line = ls[l_i + 1]

    if l_i + 1 <= len(ls) - 1:
        next_line = ls[l_i + 1]
    else:
        next_line = ls[l_i - 1]

    for i in range(first_line_number, last_line_number+1):
        if is_special(previous_line[i]) or is_special(next_line[i]):
            return True

    return False


lines = []
with open('day3Input.txt') as topo_file:
    for line in topo_file:
        lines.append(line.strip())

tot_sum = 0
for line_index in range(0, len(lines)):
    line = lines[line_index]
    current_number = ''
    for char_index in range(0, len(line)):
        char = line[char_index]

        if char.isnumeric():
            current_number += char

        elif current_number != '':
            if add_number(line, char_index, current_number, lines, line_index):
                tot_sum += int(current_number)

            current_number = ''

    if current_number != '':
        if add_number(line, len(line), current_number, lines, line_index):
            tot_sum += int(current_number)


print('sum:', tot_sum)
