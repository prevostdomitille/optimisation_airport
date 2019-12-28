def optimality(junctions, door_number, plane_number, list_plane_by_door, distances, size):
    score = 0
    for door_iterator in range(door_number, size):
        score = score + junctions[plane_number][list_plane_by_door[door_iterator]]\
                + junctions[list_plane_by_door[door_iterator]][plane_number]
        score = score * distances[door_number][door_iterator]
    return score


def glutton_simple_allocation(distances, junctions, size):
    list_plane_by_door = [-1] * size
    planes_allocated = [-1] * size
    planes_allocated[0] = 1
    list_plane_by_door[0] = 0
    total_score = 0

    for door_number in range(1, size):
        best_option = 200000000
        plane_retained = 0
        for plane_number in range(1, size):
            if planes_allocated[plane_number] != 1:
                current_option = optimality(junctions, door_number, plane_number, list_plane_by_door, distances, size)
                if current_option <= best_option:
                    best_option = current_option
                    list_plane_by_door[door_number] = plane_number
                    plane_retained = plane_number
        planes_allocated[plane_retained] = 1
        total_score = total_score + best_option
    print(total_score)
    return list_plane_by_door


def glutton_simple_from_door(size, distances, junctions):
    solution = glutton_simple_allocation(distances, junctions, size)
    return solution