from glutton_by_pairs import number_of_passengers_by_plane
from glutton_simple_optim import create_sorted_dict


def optimality_optim(junctions, door_number, plane_number, list_plane_by_door, distances, size):
    score = 0
    for door_iterator in range(size):
        if list_plane_by_door[door_iterator] != -1 and door_number != door_iterator:
            score = score + junctions[plane_number][list_plane_by_door[door_iterator]]\
                + junctions[list_plane_by_door[door_iterator]][plane_number]
            score = score * distances[door_number][door_iterator]
    return score


def glutton_simple_optim_allocation(list_planes, junctions, distances, size):
    list_plane_by_door = [-1] * size
    planes_allocated = [-1] * size
    list_plane_by_door[list_planes[0][1]] = 0
    planes_allocated[0] = 1
    total_score = 0;
    for iterator in range(1, size):
        door_number = list_planes[iterator][1]
        best_option = 200000000
        plane_retained = 0
        for plane_number in range(1, size):
            if planes_allocated[plane_number] != 1:
                current_option = optimality_optim(junctions, door_number, plane_number, list_plane_by_door, distances, size)
                if current_option <= best_option:
                    best_option = current_option
                    plane_retained = plane_number
        list_plane_by_door[door_number] = plane_retained
        planes_allocated[plane_retained] = 1
        if best_option != 200000000:
            total_score = total_score + best_option
    print(total_score)
    return list_plane_by_door


def glutton_simple_from_plane(size, distances, junctions):
    list_planes = create_sorted_dict(number_of_passengers_by_plane(junctions, size), size)
    print(list_planes)
    solution = glutton_simple_optim_allocation(list_planes, distances, junctions, size)
    return solution