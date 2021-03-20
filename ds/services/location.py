import geocoder
from yandex_geocoder import Client

_api_key = '40d1649f-0493-4b70-98ba-98533de7710b'
_client = Client(_api_key)


def _current_lat_lng():
    g = geocoder.ip('me')
    lat, lng = g.latlng
    return lat, lng


def current_location():
    lat, lng = _current_lat_lng()
    return _client.address(lng, lat)
