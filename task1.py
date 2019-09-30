# Reading input data from file
with open('input_file', 'r') as i:
    field_size = list(map(int, i.readline().split()))
    start_position = list(map(int, i.readline().split()))
    moves = i.readline().strip()
    walls = i.read().splitlines()
walls = [list(map(int, wall.split())) for wall in walls]


# This function moves pac-man
def make_step(step):
    if step == 'E':
        start_position[0] += 1
    elif step == 'W':
        start_position[0] -= 1
    elif step == 'N':
        start_position[1] += 1
    elif step == 'S':
        start_position[1] -= 1
    return start_position


out_of_game = [-1, -1, 0]  # In case if start position out of playground or on a wall we will print this
collected_coins = 0  # Coins counter

# Checking if start position is acceptable
if start_position[0] > field_size[0] or start_position[1] > field_size[1]:
    print(out_of_game)
elif start_position in walls:
    print(out_of_game)
else:
    # If start position is OK, moving pac-man and passing steps if the walls get in the way
    for move in moves:
        if make_step(move) not in walls and 0 < start_position[0] <= field_size[0] \
                and 0 < start_position[1] <= field_size[1]:
            collected_coins += 1
            current_position = start_position.copy()
        else:
            start_position = current_position.copy()
            continue
    current_position.append(collected_coins)
    print(current_position)
