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


if __name__ == "__main__":
    distances = [[0, 100, 6, 5], [60, 0, 9, 10], [4, 1, 0, 8], [4, 1, 9, 0]]
    junctions = [[0, 10, 3, 12], [10, 0, 6, 5], [12, 5, 0, 10], [12, 5, 100, 0]]
    size = 4
    try:
        size, distances, junctions = parsing()
        print(glutton_simple_from_door(size, distances, junctions))
        print(glutton_simple_optim(size, distances, junctions))
        print(glutton_simple_from_plane(size, distances, junctions))
    except FileNotFoundError:
        print("File not found")
    except ImportError:
        print('Input format not correct')

