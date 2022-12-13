# Drone-Cast
A Python app that will let the user know if it's safe to fly their drone.
The front end is built using the python tkinter toolkit.
Asks the user to enter their zip code and the max speed of their drone. 
The IP-API can also get users' current location if they do not know their zip code.
Then uses the Open Weather API to get weather conditions, temperature, wind speed, wind gust, and humidity.
Uses the two-thirds rule to determine if the wind speed/gust is too high for the drone.
It also follows other best practice conditions to give a final recommendation on whether flying is safe.
