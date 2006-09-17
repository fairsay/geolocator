The functionality of this package can be divided into roughly three categories:

 1. Library of various GIS (Geographical Information Systems) algorithms
  - algorithms related to the longitude-latitude coordinate system
  - algorithms related to distance calculation (Haversine function)

 2. Common API to location data provided by different organizations
  - MaxMind:http://www.maxmind.com (some free data, mostly commercial)
  - GNS (Geonet Names Server):http://earth-info.nga.mil/gns/html (free data)

 3. Common API to GeoIP data sources provided by different organizations
  - MaxMind:http://www.maxmind.com (some free data, mostly commercial)

See INSTALL.txt on how to configure the data sources for 2 and 3.

The library can be useful for example to implement location-based features
in different www frameworks; for an example of that, see the GeoLocation Zope /
CMF / Plone package from which this library was spun off. Please note, however,
that there is nothing www-specific in the library, nor does it have any
external dependencies.

Notes:

 - there is a little bit of import-time magic: the name "ChosenLocatorId" is bound to
   id of the locator that the package thinks is the best available one on the system
 - support for accessing GNS data is not yet working in version 0.1
 - accessing MaxMind data only works on unix until someone compiles the MaxMind
   C library that used to access their data for win32. Anyone able to do that?
   The C library is open source; check MaxMind site or search sourceforge.
