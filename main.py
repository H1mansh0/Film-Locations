import folium
import argparse
from geopy.geocoders import Nominatim
import haversine


geolocator = Nominatim(user_agent="my_requests")


parser = argparse.ArgumentParser()

parser.add_argument('longitude', type=int, help='Longitude of place')
parser.add_argument('latitude', type=int, help='Latitude of place')
parser.add_argument('year', type=str, help='Year of film')


args = parser.parse_args()

ln = args.latitude
lg = args.longitude
year = args.year

def country_getter(lat: float, long: float) -> str:
    """
    Calculates address using
    longitude and latitude
    """
    location = geolocator.geocode([lat, long], language='en').address
    return location.split(', ')[-1]

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
