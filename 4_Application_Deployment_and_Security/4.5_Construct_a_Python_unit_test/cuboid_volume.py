def cuboid_volume(l):
    if type(l) not in [int, float]:
        raise TypeError("Length of cuboid can only be int or float.")
    return (l*l*l)