from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
from pprint import pprint


#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

if __name__ == "__main__":
    # execute only if run as a script
  
    # ---------------------------- Retrieve Lowest prices stored in Sheets ------------------------------- #
    response = DataManager()
    #sheet_data = response.get_data()


    # ---------------------------- Add user info to the list ------------------------------- #
    #users = response.post_user_info("Dilraj","Bal","ds_dil@email.com")
    #print(users)


    # ---------------------------- Search for Flight data ------------------------------- #
    search_cities = FlightSearch()
    #search_cities.get_code("Paris")


    #for cities in range(0,len(sheet_data['sheet1'])):
    #    print(sheet_data['sheet1'][cities]['city'])
    #    sheet_data['sheet1'][cities]['iataCode'] = search_cities.get_code(sheet_data['sheet1'][cities]['city'] )
    #    response.update_iata(search_cities.get_code(sheet_data['sheet1'][cities]['city'] ), sheet_data['sheet1'][cities]['id'])
    #pprint(sheet_data)


    # ---------------------------- Search for Flight Prices per each destination ------------------------------- #

    price_info = FlightData()
    deals = price_info.get_flight_data('LHR')
    pprint(deals)
    #for cities in range(0,len(sheet_data['sheet1'])):
    #    price = price_info.get_flight_data(sheet_data['sheet1'][cities]['iataCode'])
    #    print(f"{sheet_data['sheet1'][cities]['city']}: {price}")


    # ---------------------------- Send notification deals to user------------------------------- #
    deals_notice = NotificationManager()
    message1 = f"Only £{deals['price']+deals['bags_price']} to fly from {deals['departure_city']}-{deals['departure_city_code']}"
    message2 = f" to {deals['arrive_city']}-{deals['arrive_city_code']}, from {deals['outbound_date']} to {deals['inbound_date']}."
    message = message1+message2
    #deals_notice.send_notification(message)


