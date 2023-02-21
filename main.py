import folium
import argparse
from geopy.geocoders import Nominatim
import haversine


geolocator = Nominatim(user_agent="my_requests")


parser = argparse.ArgumentParser()

parser.add_argument('year', type=str, help='Year of film')
parser.add_argument('longitude', type=float, help='Longitude of place')
parser.add_argument('latitude', type=float, help='Latitude of place')
parser.add_argument('filename', type=str, help='Path to file')



args = parser.parse_args()

ln = args.latitude
lg = args.longitude
year = args.year
filename = args.filename

def file_reader(filename: str) -> list:
    """
    Read file
    """
    res = []
    with open(filename, 'r') as file:
        data = file.readlines()[14:-1]
        for line in data:
            res += [(line[:-2].split(' (')[0] ,line[:-2].split(' (')[1][:4],
                                [ele for ele in line.replace('\n', '').split('\t')[1:] if ele][0])]
    return res

def map_maker(coords: list, rad: int):
    """
    Creates map with 10 markers 
    which shows the nearest films and
    grey circle which shows the area of
    the nearest film
    """
    map = folium.Map()
    fg = folium.FeatureGroup(name="Films")
    for ele in coords:
        fg.add_child(folium.Marker(location=[ele[1][0], ele[1][-1]], popup=ele[0], icon=folium.Icon(), color = 'black'))
    fg.add_child(folium.Circle(location = [ln, lg], radius=rad*1000, color='grey', fill=True, fill_color='grey', popup='Area of films'))
    map.add_child(fg)
    return map

def country_getter(lat: float, long: float) -> str:
    """
    Calculates address using
    longitude and latitude
    """
    location = geolocator.geocode([lat, long], language='en').address
    return location.split(', ')[-1]

def places(country: str, year: str, filename: str) -> list:
    """
    Gets list of films, years of publication and addresses of films
    then function calculate coordinates of recording places of films
    """
    res = []
    film_list = list(set([ele for ele in file_reader(filename) if ((country in ele[-1]) and (year in ele))]))
    for ele in film_list[:10]:
        try:
            location = geolocator.geocode(ele[-1])
            res += [(ele[0],[location.latitude, location.longitude])]
        except AttributeError:
            continue
    return res

def distance_calc(ln: int, lg: int, places: list[tuple]) -> list[tuple]:
    """
    Calculates the nearest recording places
    to given coordinates
    """
    res = []
    for ele in places:
        res += [(ele[0], ele[-1], haversine.haversine((ln, lg), (ele[-1][0], ele[-1][0])))]
    return sorted(res, key = lambda x: x[-1])[:10]

def main():
    """
    The main function
    """
    list_of_dist = distance_calc(ln, lg, places(country_getter(ln, lg), year, filename))
    print(list_of_dist)
    rad = round(list_of_dist[-1][-1])
    return map_maker(list_of_dist, rad)

if __name__ == '__main__':
    main()
