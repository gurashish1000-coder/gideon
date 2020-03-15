#!/usr/bin/env python3
import datetime
import requests
import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import subprocess
import json
import nmap


# Method to show the current time.
def showTime():
    now = datetime.datetime.now()
    print("Current date and time : ")
    print(now.strftime("%Y-%m-%d %H:%M:%S"))


"""
I could have made a calculator app from starting but that would have been a wastage of time. So i am 
going to be using the eval function. 
"""
def calculate():
    # Prints out the options
    while True:
        # either we get expression info or quit
        mode = input("\nPlease enter your expression:")
        if mode == "quit":
            break
        else:
            try:
                print(eval(mode))
            except:
                print("something's wrong with the expression")


# Method to show the current weather
def showWeather():
    api_key = "260f4b24510171dde25f05e78af6de07"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = "Toronto"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)

    # Converting Json format data into python formatted data
    x = response.json()
    if x["cod"] != "404":
        # store the value of "main" key in variable y
        y = x["main"]

        # store the value corresponding to the "temp" key of y in kelvin
        current_temperature = y["temp"]
        temp_celsius = int(current_temperature - 273.15)

        # store the value corresponding to the "pressure" key of y
        current_pressure = y["pressure"]

        # store the value corresponding to the "humidity" key of y
        current_humidity = y["humidity"]

        # store the value of "weather" key in variable z
        z = x["weather"]

        # store the value corresponding to the "description" key at the 0th index of z
        weather_description = z[0]["description"]

        # printing weather info
        print('==================================')
        print('|' "Weather = " + city_name + '|')
        print('==================================')
        print('|current condition    = ' + str(weather_description))
        print('|current temp         = ' + str(temp_celsius) + "c")
        print('|current pressure     = ' + str(current_pressure) + " pHa")
        print('|current humidity     = ' + str(current_humidity) + "%")
        print('==================================')
    else:
        print("Sorry, city not found")


'''
To implement something like this with gmail, gmail's new OAuth2 security measures and library needs to be used. 
Implementing something like that would be a  feature in it self.
so this works with office365 email accounts. 
would need  to implement further convenient changes, but will do that later.
'''


def sendEmail(subject, body, receiver):
    # Open the plain text file whose name is in textfile for reading.
    # Enter your email address and password below.
    email = 'gurashish2000@outlook.com'
    password = 'Gurashish@3'
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = receiver
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    # If not working change to port 587
    server = smtplib.SMTP('smtp.office365.com', 25)
    server.ehlo()
    server.starttls()
    server.login(email, password)
    text = msg.as_string()
    server.sendmail(email, receiver, text)
    server.quit()
    print('email sent')


# method to start a timer in terminal.
def setTimer():
    print('Timer set')


def nmapScaner(address):
    scanner = nmap.PortScanner()
    print(scanner.nmap_version)
    scanner.scan(address, "1-1024", "-v")
    print(scanner.scaninfo())
    print(scanner.csv())
    print("done")
