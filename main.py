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
