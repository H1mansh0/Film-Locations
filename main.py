import folium


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
