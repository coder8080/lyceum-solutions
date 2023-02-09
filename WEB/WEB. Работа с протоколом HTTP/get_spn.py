def get_spn(toponym) -> tuple[float, float]:
    toponym_boundedby = toponym['boundedBy']['Envelope']
    lower_corner = list(
        map(float, toponym_boundedby['lowerCorner'].split(' ')))
    upper_corner = list(
        map(float, toponym_boundedby['upperCorner'].split(' ')))
    lon_delta = str(
        abs(lower_corner[0] - upper_corner[0]))
    lat_delta = str(
        abs(lower_corner[1] - upper_corner[1]))
    return lon_delta, lat_delta
