import math

def haversine(origin, destination):
    """
    Calculates the haversine distance in km between two points

    Parameters:
    -----------
    origin: set or list of (latitude, longitude)
    destination: set or list of (latitude, longitude)

    Returns:
    --------
    haversine distance in km (assumes a straight line, no account for elevation changes)

    """ 
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371 # km

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c

    return d

def east_north_distance(origin, destination):
    """
    Calculates the distance between two coordinates expresses 
    in eastings/northings 

    Parameters:
    -----------
    origin: set or list of (easting, northing)
    destination: set or list of (easting, northing)

    Returns:
    --------
    straight line distance sqrt((E1-E2)^2+(N1-N2)^2)

    """ 
    E1, N1 = origin
    E2, N2 = destination

    d = math.sqrt((E1-E2)**2 +(N1-N2)**2)
    return d
