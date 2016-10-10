""" Retrieves distance from Google API given origin, destination"""
import googlemaps.distance_matrix


def get_distance(origin, destination):
    """ Returns distance. Matrix is a nested dictionary"""
    my_client = googlemaps.Client(key='AIzaSyCXcOGwoNEWW3sDcOpIoyyQq98MvHUGbI4')
    # Returns a nexted dictionary with many values.
    data_dict = googlemaps.distance_matrix.distance_matrix(my_client,
                                                           origin, destination)

    # Refers to the distance in meters.
    # Data structure is a mixture of dicts and lists.
    distance_meters = data_dict['rows'][0]['elements'][0]['distance']['value']
    return distance_meters
