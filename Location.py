import requests

class Location():
    url = "http://ip-api.com/json/?fields=61439"
    response=""

    def __init__(self) -> None:
         self.response = requests.get(self.url).json()

    def getCountry(self):
        country = self.response['countryCode'] 
        return country    

    def getCity(self):
        country = self.response['city'] 
        return country  

    def getZip(self):
        zip = self.response['zip']
        return zip