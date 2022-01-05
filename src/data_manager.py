import requests
from requests.models import Response

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        # creating variable to use the url
        self.endpoint = 'https://api.sheety.co/e78e679bf4063c1cfa9e4f16869c45b0/flightDeals/prices'
    
    def post_data(self,city,iataCode,lowestPrice,id) -> list:
        # creating the body of the api
        body={
            'prices':{
                'city':city,
                'iataCode':iataCode,
                'lowestPrice':lowestPrice,
                'id':id,
            }
        }
        response = requests.post(url=self.endpoint,json=body)
        return response.json()['prices']


    def get_data(self) -> list:
        '''# creating the body of the api
        body={
            'prices':{
                'city':city,
                'iataCode':iataCode,
                'lowestPrice':lowestPrice,
                'id':id,
            }
        }'''
        # geting the data from the url
        response = requests.get(url=self.endpoint)
        data = response.json()['prices']
        return data

        