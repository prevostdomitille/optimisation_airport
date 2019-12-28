from glutton_by_pairs import number_of_passengers_by_plane
from glutton_simple_optim import create_sorted_dict, glutton_simple_optim_allocation

# We simply switch planes and doors as they have the same roles
def glutton_simple_from_plane(size, distances, junctions):
    list_planes = create_sorted_dict(number_of_passengers_by_plane(junctions, size), size)
    solution = glutton_simple_optim_allocation(list_planes, distances, junctions, size)
    return solution