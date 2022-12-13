import tkinter
import Weather
import Drone

class Gui():
    def __init__(self,window:tkinter,zip:str,speed:str) -> None:
        curWeather = Weather.Weather(zip)
        curDrone = Drone.Drone(speed)
        window.resizable(False, False)
        window.geometry("600x500")
        window.title("Drone-Cast")
        danger = False
        caution = False

        cityNameLabel = tkinter.Label(window, text=(curWeather.getCityName()+", "+curWeather.getCountryCode()), font=('Arial','40','underline','bold'))
        cityNameLabel.pack(pady=20)

        condition = curWeather.getCondition()
        conditionLabel = tkinter.Label(window, text=("Condition: "+((str)(condition))), font=('Arial',25))
        if(condition=="Snow"):
            conditionLabel.config(fg='#FF0000')
            danger = True
        if(condition=="Rain"):
            conditionLabel.config(fg='#FF0000')
            danger = True
        if(condition=="Mist"):
            conditionLabel.config(fg='#F6BE00')
            caution = True
        conditionLabel.pack(pady=10)
      
        temp:float = curWeather.getTemp()
        tempLabel = tkinter.Label(window, text=("Temp: "+((str)(temp))+" °F"), font=('Arial',25))
        if(curDrone.getMaxTemp()<=temp or temp<=curDrone.getLowTemp()):
            tempLabel.config(fg='#FF0000')
            danger = True
        tempLabel.pack(pady=10)
         
        windSpeed:float = curWeather.getWind()
        windSpeedLabel = tkinter.Label(window, text=("Wind Speed: "+((str)(windSpeed))+" MPH"), font=('Arial',25))
        if(curDrone.getMaxSpeed()<=windSpeed):
            windSpeedLabel.config(fg='#FF0000')
            danger = True
        windSpeedLabel.pack(pady=10)

        if(curWeather.hasGust()):
            gust:float = curWeather.getGust()
            gustLabel = tkinter.Label(window, text=("Gust : "+((str)(gust))+" MPH"), font=('Arial',25))
            if(curDrone.getMaxSpeed()<=gust):
                gustLabel.config(fg='#FF0000')
                danger = True
            else:
                gustLabel.config(fg='#F6BE00')
                caution = True
            gustLabel.pack(pady=10)

        humidity:float = curWeather.getHumidity()
        humidityLabel = tkinter.Label(window, text=("Humidity: "+((str)(humidity))+"%"), font=('Arial',25,))
        if(curDrone.getMaxHumidity()<=humidity):
            humidityLabel.config(fg='#FF0000')
            danger = True
        humidityLabel.pack(pady=10)

        statusLabel:tkinter.Label
        if(danger):
            statusLabel = tkinter.Label(window, text=("Not Safe to Fly!"), font=('Arial',25,'bold'))
            statusLabel.config(fg='#FF0000')
        elif(caution):
            statusLabel = tkinter.Label(window, text=("Have Caution When Flying"), font=('Arial',25,'bold'))
            statusLabel.config(fg='#F6BE00')
        else:
            statusLabel = tkinter.Label(window, text=("Safe to Fly!"), font=('Arial',25,'bold'))
            statusLabel.config(fg='#058711')
        statusLabel.pack(pady=30)

        window.eval('tk::PlaceWindow . center')  
        window.mainloop()