import json


class ParseJsonObject:
    """Class converts json object to python dictionary."""

    def __init__(self, json_object):
        """Accepts json object and convert to dictionary."""
        self.parsed_obj = json.loads(json_object)


class ParseMainPageObject(ParseJsonObject):
    """Class converts json object to python dictionary and contains methods for return defined values.

    Works with main page https://yandex.ru/

    """
    def __init__(self, *args, **kwargs):
        super(ParseMainPageObject, self).__init__(*args, **kwargs)
    
    def get_geo_id(self) -> int:
        """Returns geo id requested city."""
        return int(self.parsed_obj['widgets']['geoid'])


class ParseGeoPageObject(ParseJsonObject):
    """Class converts json object to python dictionary and contains methods for return defined values.

    Works with geo page https://yandex.ru/

    """

    def __init__(self, *args, **kwargs):
        super(ParseGeoPageObject, self).__init__(*args, **kwargs)

    def get_geo_id(self) -> int:
        """Returns geo id requested city."""
        return self.parsed_obj['b-autocomplete-item']['geoid']

    def get_city_name(self) -> str:
        """Returns city name requested city."""
        return self.parsed_obj['b-autocomplete-item']['title']

    def get_region_name(self) -> str:
        """Returns region name requested city."""
        return self.parsed_obj['b-autocomplete-item']['subtitle']
