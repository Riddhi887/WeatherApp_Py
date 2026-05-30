#we used free api from web created an api key of weather api

import requests     #you can access things from network
import json
import pyttsx3
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
API_KEY = os.getenv("API_KEY")

# text to speech
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

while True:
    city =  input("Enter the name of City: ")
    if city.lower() in ["exit", "quit", "bye"]:
        print("Goodbye!")
        speak("Goodbye!")
        break

    url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"

    #get url
    r = requests.get(url)
    #print(r.text)   #prints the data
    #print(type(r.text))  #know the type of the data

    #data is str to parse it as dictionary use json
    if r.status_code == 200:
        weatherDict = json.loads(r.text)
        #print(weatherDict)
        cityName = weatherDict["location"]["name"]
        countryName = weatherDict["location"]["country"]
        localtime = weatherDict["location"]["localtime"]
        temp = weatherDict["current"]["temp_c"]
        condition = weatherDict["current"]["condition"]["text"]
        region = weatherDict["location"]["region"]
        latitude = weatherDict["location"]["lat"]
        longitude = weatherDict["location"]["lon"]

        # Extra weather details
        windDegree = weatherDict["current"]["wind_degree"]
        windDir = weatherDict["current"]["wind_dir"]
        windKph = weatherDict["current"]["wind_kph"]
        humidity = weatherDict["current"]["humidity"]
        clouds = weatherDict["current"]["cloud"]
        dewpoint = weatherDict["current"]["dewpoint_c"]
        willItRain = weatherDict["current"]["will_it_rain"]
        chanceOfRain = weatherDict["current"]["chance_of_rain"]
        willItSnow = weatherDict["current"]["will_it_snow"]
        chanceOfSnow = weatherDict["current"]["chance_of_snow"]

        #print on console
        print("Name:", cityName)
        print("Country:", countryName)
        print("Local Time:", localtime)
        print("Temperature (°C):",temp)
        print("Condition:", condition)


        #speak it
        report = f"{cityName},located in {countryName} at {localtime}, the temperature is {temp} degrees Celsius with {condition} condition."
        speak(report)

        s = (f"Do you want me to provide detailed information?\n 1. Yes\n 2. No")
        print(s)
        speak(s)

        choice = input("Enter your choice: ")
        # Convert numeric rain/snow flags into Yes/No


        if choice == "1":
            rainAnswer = "Yes" if willItRain >= 1 else "No"
            snowAnswer = "Yes" if willItSnow >= 1 else "No"
            reportDetailed = (
                f"{cityName}, located in {countryName} at {localtime}, \n"
                f"the temperature is {temp}°C with {condition} condition.\n"
                f"Wind is blowing at {windKph} kph from {windDir} ({windDegree}°).\n"
                f"Humidity is {humidity}%, cloud cover is {clouds}%. \n"
                f"Dewpoint is {dewpoint}°C.\n"
                f"Rain forecast: Will it rain? {rainAnswer}\n with Chance of rain: {chanceOfRain}%.\n"
                f"Snow forecast: Will it snow? {snowAnswer}\n with Chance of snow: {chanceOfSnow}%.\n"
                f"Enter the different city"
            )
            print(reportDetailed)
            speak(reportDetailed)
        else:
            s1 = (f"No Worries! Enter Different City")
            print(s1)
            speak(s1)



    else:
        error_msg = f"Error fetching weather data: {r.status_code}"
        print(error_msg)
        speak(error_msg)




