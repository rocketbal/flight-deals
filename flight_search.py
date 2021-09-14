import requests
from pprint import pprint

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.data = []
        self.tequilia_endpoint = "https://tequila-api.kiwi.com/locations/query"
        self.api_key= "OXnZwqwfURHKpdWK05CGT6BWjnE9MoRy"

    def get_code(self, cities):
        headers = {
            "apikey": self.api_key
            }

        params ={
            "term": cities,
            "location_types":"airport",
            "limit":10,
            "active_only": "true",
            }
        response = requests.get(url = self.tequilia_endpoint,params=params, headers = headers)
        
        data = response.json()
        print(data['locations'][0]['city']['code'])
        return data['locations'][0]['city']['code']
   