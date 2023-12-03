with open('day2Input.txt') as topo_file:
    tot_sum = 0
    for line in topo_file:
        _, game_data = line.split(":")

        game_data_occurrences = game_data.split(";")
        fewest_cubes = {}
        for occurrence in game_data_occurrences:
            blocks = occurrence.split(",")
            for block in blocks:
                number, block_key = block.strip().split(" ")
                number = int(number)
                if block_key not in fewest_cubes:
                    fewest_cubes[block_key] = number
                elif fewest_cubes[block_key] < number:
                    fewest_cubes[block_key] = number

        product = 1
        for value in fewest_cubes.values():
            product = product * value

        tot_sum += product

    print(tot_sum)
