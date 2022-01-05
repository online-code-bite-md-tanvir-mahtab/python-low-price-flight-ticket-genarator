import json
import requests
from requests.models import Response




class FlightSearch:
    def get_country_code(self,country):
        endpoint = "https://api.printful.com/countries"

        response = requests.get(url=endpoint)
        code = response.json()['result']

        for name in code:
            if name['name'] == country:
                return name['code']
