def country_getter(lat: float, long: float) -> str:
    """
    Calculates address using
    longitude and latitude
    """
    location = geolocator.geocode([lat, long], language='en').address
    return location.split(', ')[-1]
