numbers = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}


def find_first_number(string, reverse):
    buffer = ""
    for c in string:
        if c.isnumeric():
            return c
        else:
            if reverse:
                buffer = c + buffer
            else:
                buffer = buffer + c
            for key in numbers:
                if key in buffer:
                    return str(numbers[key])


with open('day1Input.txt') as topo_file:
    tot_sum = 0
    for line in topo_file:
        number = find_first_number(line, False) + find_first_number(line[::-1], True)
        tot_sum += int(number)
    print(tot_sum)
