from geolocator import DummyLocator, MaxMindCityLocator, MaxMindCountryLocator, ChosenLocatorId, GeoLocatorBase

locators = {
   "dummy_locator": DummyLocator,
   "maxmind_city_locator": MaxMindCityLocator,
   "maxmind_country_locator": MaxMindCountryLocator
}

__all__ = ("GeoLocatorBase", "DummyLocator", "MaxMindCityLocator", "MaxMindCountryLocator", "ChosenLocatorId", "locators")
