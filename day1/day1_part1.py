def find_first_number(string):
    for c in string:
        if c.isnumeric():
            return c


with open('day1Input.txt') as topo_file:
    tot_sum = 0
    for line in topo_file:
        number = find_first_number(line) + find_first_number(line[::-1])
        tot_sum += int(number)
    print(tot_sum)
