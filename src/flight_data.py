import requests
from datetime import datetime

from requests.api import head, request

class FlightData:
    #This class is responsible for structuring the flight data.
    def get_data(self,city_code):
        endpoint = "https://tequila-api.kiwi.com/v2/search"
        head = {
            'apikey':"mK81B_VNX1UvNHahO65n8hvGkfkbo6AU"
        }
        body = {
            'fly_from':'BD',
            'fly_to':city_code,
            'date_from':datetime.now().strftime("%d/%m/%Y"),
            'date_to':datetime.now().strftime("%d/%m/%Y"),
        }

        request = requests.get(url=endpoint,params=body,headers=head)
        return (request.json()['data'])