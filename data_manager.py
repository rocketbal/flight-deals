import requests
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.data = 0
        self.prices = []
        self.sheety_endpoint = "https://api.sheety.co/ad39586c2d65ed38d2aadd69b0f5b9d1/flightTracker/sheet1"
        self.sheety_put_endpoint = "https://api.sheety.co/ad39586c2d65ed38d2aadd69b0f5b9d1/flightTracker/sheet1/"
        self.post_sheety_users = "https://api.sheety.co/ad39586c2d65ed38d2aadd69b0f5b9d1/flightTracker/users"
        
    def get_data(self):
        response = requests.get(url = self.sheety_endpoint)
        response.raise_for_status()
        self.data = response.json()
        
        #for prices in range(0,len(self.data['sheet1'])):
            #self.prices.append(self.data['sheet1'][prices]['lowestPrice'])
        return self.data

    def update_iata(self,iata_code,ids):
        sheety_put_endpoint_ids = self.sheety_put_endpoint + str(ids)
        print(sheety_put_endpoint_ids)
        body = {
                    "sheet1": {
                        'iataCode':iata_code,
                    "id": ids,
                   
                    }
                }
        #print(self.data)
        response = requests.put(url = sheety_put_endpoint_ids,json=body)

    def post_user_info(self,first,last,email):
        body = {
            "user":{
                "firstName":first,
                "lastName":last,
                "email":email,
                }
            }
        response = requests.post(url = self.post_sheety_users, json = body)
        return response.raise_for_status()

            