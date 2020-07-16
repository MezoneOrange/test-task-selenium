import json


class ParseJsonObject:
    """Class converts json object to python dictionary and contains methods for return defined values."""

    def __init__(self, json_object):
        """Accepts json object and convert to dictionary."""
        self.__parsed_obj = json.loads(json_object)

    def get_geo_id(self):
        return self.__parsed_obj['widgets']['geoid']

