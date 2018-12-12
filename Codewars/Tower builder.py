def tower_builder(n_floors):
    tower = []
    whitespaces_count = n_floors - 1
    floor_multiplier = 1
    for floors in range(n_floors):
        floor = '*' * floor_multiplier
        floor = (' ' * whitespaces_count) + floor + (' ' * whitespaces_count)
        tower.append(floor)
        floor_multiplier += 2
        whitespaces_count -= 1
    print tower


tower_builder(5)
