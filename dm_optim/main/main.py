from random import shuffle

from glutton_by_pairs import glutton_by_pairs
from glutton_simple_from_door import glutton_simple_from_door
from glutton_simple_optim import glutton_simple_optim
from glutton_simple_from_plane import glutton_simple_from_plane


def make_matrices(size, f):
    distances = []
    for i in range(size):
        newline = f.readline()
        data = newline.split(",")
        if len(data) != size:
            raise ImportError
        line = []
        for case in data:
            line.append(int(case))
        distances.append(line)
    return distances


def parsing():
    f = open("input_10.txt", "r")
    if f.mode != "r":
        raise FileNotFoundError
    size = int(f.readline())
    distances = make_matrices(size, f)
    junctions = make_matrices(size, f)
    return size, distances, junctions


def calculate_cost(junctions, map_planes_to_gate, size):
    cost = 0
    graph = dict.fromkeys(range(size))
    for key in graph:
        graph[key] = {}
    for i in range(size):
        for j in range(size):
            if junctions[i][j] != 0:
                graph[i][j] = junctions[i][j]
    for avion in graph:
        porte1 = map_planes_to_gate[avion]
        for voisin in graph[avion]:
            porte2 = map_planes_to_gate[voisin]
            distance = distances[porte1][porte2]
            cost += graph[avion][voisin]*distance
    print(map_planes_to_gate)
    print(cost)
    return(cost)


if __name__ == "__main__":
    distances = [[0, 100, 6, 5, 100], [60, 0, 9, 10, 30], [4, 1, 0, 8, 12], [4, 1, 9, 0, 1], [6, 10, 11, 70, 0]]
    junctions = [[0, 10, 3, 12, 8], [10, 0, 6, 5, 99], [12, 5, 0, 10, 2], [12, 5, 100, 0, 16], [10, 70, 0, 7, 3, 0]]
    size = 5
    try:
        # size, distances, junctions = parsing()
        print("score glouton simple en partant des portes")
        solution_0 = glutton_simple_from_door(size, distances, junctions)
        calculate_cost(junctions, solution_0, size)
        print("score glouton un peu optimise en partant des portes")
        solution_1 = glutton_simple_optim(size, distances, junctions)
        calculate_cost(junctions, solution_1, size)
        print("score glouton optimise en partant des avions")
        solution_2 = glutton_simple_from_plane(size, distances, junctions)
        calculate_cost(junctions, solution_2, size)
        print("score glouton par paires")
        solution_3 = glutton_by_pairs(size, distances, junctions)
        calculate_cost(junctions, solution_3, size)
        print('score random')
        sequence = [i for i in range(5)]
        print(sequence)
        shuffle(sequence)
        calculate_cost(junctions, sequence, size)

    except FileNotFoundError:
        print("File not found")
    except ImportError:
        print('Input format not correct')

