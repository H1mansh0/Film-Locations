def distance_calc(ln: int, lg: int, places: list[tuple]) -> list[tuple]:
    """
    Calculates the nearest recording places
    to given coordinates
    """
    res = []
    for ele in places:
        res += [(ele[0], ele[-1], haversine.haversine((ln, lg), (ele[-1][0], ele[-1][0])))]
    return sorted(res, key = lambda x: x[-1])[:10]
