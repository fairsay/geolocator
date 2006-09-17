import os

import gislib
from providers import *

"""

Provides a common api to various geoip/geolocation databases.

MaxMind country & city geoip databases are supported, with support planned for:

 * the GNS "city & country location database":http://earth-info.nga.mil/gns/html

 * the hostip.info "city IP database":http://www.hostip.info/index.html

 * others?

"""

__all__ = ["DummyLocator", "MaxMindCountryLocator", "MaxMindCityLocator"]


class GeoLocatorBase:

   def getDistance(self, origin, location):
      "get distance between origin and location"
      return gislib.getDistanceByHaversine(origin, location)

   def isWithinDistance(origin, location, distance):
      "return true if location is within the given distance from origin"
      return gislib.isWithinDistance(origin, location, distance)


# This is really just a dummy.
# See the DummyProvider for API.
# Subclass your own locator according to what data you have/need.
# Some example subclasses below.

class DummyLocator(GeoLocatorBase, DummyProvider):
   "generic proxy/api to various data sources"

class MaxMindCountryLocator(GeoLocatorBase, MaxMindCountryDataProvider):
   "for using the free country data"

class MaxMindCityLocator(GeoLocatorBase, MaxMindCityDataProvider):
   "for using the commercial city data"