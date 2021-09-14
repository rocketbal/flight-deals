import requests
import datetime

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        self.deals_packet = {
            "price":0,
            "bags_price":0,
            "departure_city":"SEATTLE",
            "departure_city_code":"SEA",
            "arrive_city":"",
            "arrive_city_code":"",
            "outbound_date":"",
            "inbound_date":"",
            "stop_over":0,
            "via_city":"",
            }
        self.search_endpoint = "https://tequila-api.kiwi.com/v2/search"
        self.departure_airport_code = "SEA"
        self.departure_city = "SEATTLE"
        self.tomorrow = datetime.date.today()+datetime.timedelta(days=1)
        self.six_months = datetime.date.today()+datetime.timedelta(days=60)
        self.headers = {
            "apikey": "fZfdCxeB9rpwjP6wngUckah4NjlSvh-V"
            }
        self.stop_overs=1
        self.via_city=""

    def return_data(self,data:dict):
        self.deals_packet["price"] = data["data"][0]['price']
        self.deals_packet["bags_price"] = data["data"][0]['bags_price']['1']
        self.deals_packet["arrive_city"] = data["data"][0]['cityTo']
        self.deals_packet["arrive_city_code"] = data["data"][0]['cityCodeTo']
        self.deals_packet["outbound_date"] =  data["data"][0]['route'][0]['local_arrival'].split('T')[0]
        self.deals_packet["inbound_date"] =  data["data"][0]['route'][1]['local_arrival'].split('T')[0]
        self.deals_packet["stop_over"] = self.stop_overs
        self.deals_packet["via_city"] = self.via_city
        


    def get_flight_data(self,fly_to:str)->dict:
        try:
            params = {
                "fly_from":self.departure_airport_code,
                "fly_to":fly_to,
                "date_from":self.tomorrow.strftime("%d/%m/%Y"),
                "date_to":self.six_months.strftime("%d/%m/%Y"),
                "nights_in_dst_from":7,
                "nights_in_dst_to":28,
                "flight_type":"round",
                "curr":"USD",
                "max_stopovers":self.stop_overs,
                "limit":10,
                }
            response = requests.get(url = self.search_endpoint,params=params,headers=self.headers)
            data = response.json()
            print(data)
            flag = data["data"][0]['price']
            self.return_data(data)
            return self.deals_packet

        except:
            self.stop_overs = 2
            response = requests.get(url = self.search_endpoint,params=params,headers=self.headers)
            data = response.json()
            print(data)
            self.return_data(data)
            return self.deals_packet

        
            


