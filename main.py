def places(country: str, year: str) -> list:
    """
    Gets list of films, years of publication and addresses of films
    then function calculate coordinates of recording places of films
    """
    res = []
    film_list = list(set([ele for ele in file_reader('locations.list') if ((country in ele[-1]) and (year in ele))]))
    for ele in film_list[:10]:
        try:
            location = geolocator.geocode(ele[-1])
            res += [(ele[0],[location.latitude, location.longitude])]
        except AttributeError:
            continue
    return res
