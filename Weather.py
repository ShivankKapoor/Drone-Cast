import requests

class Weather():
    response=""
    def __init__(self,zip:str) -> None:
        APIKEY:str="6376b9a415e766eaef5d5d53d30b7e1e"
        url:str = "https://api.openweathermap.org/data/2.5/weather?zip="+zip+",US&units=imperial&appid="+APIKEY
        self.response = requests.get(url).json()
        print(url)
        #print(self.response)

    def getCondition(self):
        condition=self.response['weather'][0]['main']
        return condition

    def getWind(self):
        windSpeed=self.response['wind']['speed']
        return windSpeed

    def getTemp(self):
        temp:str=self.response['main']['temp']
        return temp

    def getCityName(self):
        name=self.response['name']
        return name

    def hasGust(self):
        gust = 0
        try:
            gust=self.response['wind']['gust']
        except KeyError:
            return False
        return True

    def getGust(self):
        gust=self.response['wind']['gust']
        return gust
    
    def getCountryCode(self):
        CountryCode=self.response['sys']['country']
        return CountryCode

    def getHumidity(self):
        humidity=self.response['main']['humidity']
        return humidity
