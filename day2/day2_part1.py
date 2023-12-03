cubes = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

with open('day2Input.txt') as topo_file:
    tot_sum = 0
    for line in topo_file:
        game, game_data = line.split(":")
        _, game_number = game.split(" ")

        game_ok = True
        game_data_occurrences = game_data.split(";")
        for occurrence in game_data_occurrences:
            blocks = occurrence.split(",")
            for block in blocks:
                number, block_key = block.strip().split(" ")
                if block_key not in cubes or cubes[block_key] < int(number):
                    game_ok = False
                    break

            if not game_ok:
                break
        if game_ok:
            tot_sum += int(game_number)
    print(tot_sum)
