# list of doors sorted by sum of distances to other doors
def excentricity_door(distances, size):
    doors = []
    for i in range(size):
        temp = 0
        for j in range(size):
            temp += distances[j][i]
        doors.insert(i, temp)
    return doors


# list of passengers sorted by sum of passengers transiting to other doors
def number_of_passengers_by_plane(junctions, size):
    number_passengers = []
    for i in range(size):
        temp = 0
        for j in range(size):
            temp += junctions[j][i]
            temp += junctions[i][j]
        number_passengers.insert(i, temp)
    return number_passengers


# list of junctions (two planes) by priority: number of passengers between the two planes, and then
# number of passengers in a plane
def order_junctions(junctions, size):
    list_junctions_load = []
    priority_between_planes = number_of_passengers_by_plane(junctions, size)
    for i in range(size):
        for j in range(i + 1, size):
            sum_transit = junctions[i][j] + junctions[j][i]
            list_junctions_load.append((i, j, sum_transit,  priority_between_planes[i], priority_between_planes[j]))
    list_junctions_load.sort(key=lambda val: val[4], reverse=True)
    list_junctions_load.sort(key=lambda val: val[3], reverse=True)
    list_junctions_load.sort(key=lambda val: val[2], reverse=True)
    return list_junctions_load


# list of door distances by length and excentricity of the doors
def order_doors(distances, size):
    list_doors = []
    excentricity = excentricity_door(distances, size)
    for i in range(size):
        for j in range(i + 1, size):
            list_doors.append((i, j, distances[i][j], excentricity[i] + excentricity[j]))
    list_doors.sort(key=lambda val: val[3])
    list_doors.sort(key=lambda val: val[2])
    return list_doors


def glutton_allocation(list_distances, list_junctions_load, size):
    mapping_plane_door = [-1] * size  # for each door, the number of the plane that uses it
    planes_allocated = [-1] * size  # for each plane, 1 if it is allocated, -1 elsewhere
    for junction in list_junctions_load:
        # none of the two planes is allocated
        if planes_allocated[junction[0]] == -1 and planes_allocated[junction[1]] == -1:
            i = 0
            while i < len(list_distances):
                if mapping_plane_door[list_distances[i][0]] != -1:
                    list_distances.pop(i)
                elif mapping_plane_door[list_distances[i][1]] != -1:
                    list_distances.pop(i)
                else:
                    mapping_plane_door[list_distances[i][0]] = junction[0]
                    mapping_plane_door[list_distances[i][1]] = junction[1]
                    planes_allocated[junction[0]] = 1
                    planes_allocated[junction[1]] = 1
                    break
                i = i + 1
    # allocate the last planes if some remain
    for i in range(len(planes_allocated)):
        if planes_allocated[i] == -1:
            for j in range(len(mapping_plane_door)):
                if mapping_plane_door[j] == -1:
                    mapping_plane_door[j] = i
                    planes_allocated[i] = 1
    return mapping_plane_door


def glutton_by_pairs(size, distances, junctions):
    list_junctions_load = order_junctions(junctions, size)
    list_distances = order_doors(distances, size)
    solution = glutton_allocation(list_distances, list_junctions_load, size)
    return solution