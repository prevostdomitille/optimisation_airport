from glutton_by_pairs import excentricity_door, number_of_passengers_by_plane

MAX = 200000000


def optimality_optim(junctions, door_number, plane_number, list_plane_by_door, distances, size):
    score = 0
    for door_iterator in range(size):
        if list_plane_by_door[door_iterator] != -1 and door_number != door_iterator:
            score = score + junctions[plane_number][list_plane_by_door[door_iterator]]\
                + junctions[list_plane_by_door[door_iterator]][plane_number]
            score = score * distances[door_number][door_iterator]
    return score


def create_sorted_dict(doors, size):
    newList = []
    for i in range(size):
        newList.append((doors[i], i))
        newList.sort(reverse=True)
    return newList


def glutton_simple_optim_allocation(doors, distances, junctions, size):
    list_plane_by_door = [-1] * size
    planes_allocated = [-1] * size
    list_plane_by_door[doors[0][1]] = 0
    planes_allocated[0] = 1

    total_score = 0
    for iterator in range(1, size):
        door_number = doors[iterator][1]
        print(globals())
        best_option = MAX
        plane_retained = 0
        for plane_number in range(1, size):
            if planes_allocated[plane_number] != 1:
                current_option = optimality_optim(junctions, door_number, plane_number, list_plane_by_door, distances, size)
                if current_option <= best_option:
                    best_option = current_option
                    plane_retained = plane_number
        list_plane_by_door[door_number] = plane_retained
        planes_allocated[plane_retained] = 1
        if best_option == MAX:
            print("ERROR")
        total_score = total_score + best_option
    print(total_score)
    return list_plane_by_door


def glutton_simple_optim(size, distances, junctions):
    list_doors = create_sorted_dict(excentricity_door(distances, size), size)
    list_planes = create_sorted_dict(number_of_passengers_by_plane(junctions, size), size)
    print(list_doors)
    solution = glutton_simple_optim_allocation(list_doors, distances, junctions, size)
    return solution