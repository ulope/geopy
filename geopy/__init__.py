from geopy.point import Point
from geopy.location import Location
from geopy import geocoders

import logging

__all__ = ('Point', 'Location', 'geocoders', )

class NullHandler(logging.Handler):
    def emit(self, record):
        pass

logging.getLogger('geopy').addHandler(NullHandler())
