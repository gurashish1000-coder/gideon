#!/usr/bin/env python3
from __future__ import unicode_literals
from bs4 import BeautifulSoup
import datetime
import requests
import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
from random import randint
import os
import shutil
import subprocess
import json
import youtube_dl
import asciiArt
import random
from zipfile import ZipFile

# Global variables will be declared here
stash_folder = ""
curr_path = ''


# intro function: executes the intro
def intro_func():
    print('Hello, This is Spock. AI created by Star Fleet.')
    # prints the star fleet logo
    asciiArt.starFleet()
    print("type help for help")
    print("How may I help you?")


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


# Downloads a youtube video
def videoDownload(link):
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])


# google news api key 065c7994498f4d8aaa01a0fa4c5106bd
def topNews():
    api_key = "065c7994498f4d8aaa01a0fa4c5106bd"
    base_url = "http://newsapi.org/v2/top-headlines?sources=google-news&apiKey="
    complete_url = base_url + api_key
    response = requests.get(complete_url)

    # Converting Json format data into python formatted data
    news_page = response.json()
    article = news_page['articles']
    # Empty list to contain all the important news.
    results = []
    for ar in article:
        results.append(ar["title"])

    for i in range(len(results)):
        # printing all trending news
        print(i + 1, results[i])


# google news api key 065c7994498f4d8aaa01a0fa4c5106bd
# The following function provides detailed stuff about the news like summary and stuff.
# det short for detailed
def detNews():
    api_key = "065c7994498f4d8aaa01a0fa4c5106bd"
    base_url = "http://newsapi.org/v2/top-headlines?sources=google-news&apiKey="
    complete_url = base_url + api_key
    response = requests.get(complete_url)
    counter = 1

    # Converting Json format data into python formatted data
    news_page = response.json()
    article = news_page['articles']
    for ar in article:
        print('==================================')
        print(str(counter) + '. ' + ar['title'])
        print(ar['description'])
        print(ar['content'])
        print('URL - ' + ar['url'])
        print('==================================')
        counter = counter + 1


# I don't watch porn, but if i did i would use this way to disguise all of it in the directories jungle
def createStashDir():
    path = os.path.abspath(".")
    curr_path = path
    if os.path.isdir(path + "/Videos"):
        print("Videos folder doesn't exist.")
        answer = input("Would you like to create the Videos folder (y or n) ? ; ")
        if answer == "y":
            os.mkdir(path + "/Videos")
            try:
                os.mkdir(path + "/Videos/education")
                os.mkdir(path + "/Videos/education/maths")
                os.mkdir(path + "/Videos/education/maths/tuts")
                os.mkdir(path + "/Videos/education/maths/tuts/assignments")
                os.mkdir(path + "/Videos/education/maths/tuts/assignments/ch1")
                os.mkdir(path + "/Videos/education/maths/tuts/assignments/ch2")
                os.mkdir(path + "/Videos/education/maths/tuts/assignments/ch3")
                os.mkdir(path + "/Videos/education/maths/tuts/assignments/ch4")
                os.mkdir(path + "/Videos/education/maths/tuts/assignments/ch5")
                os.mkdir(path + "/Videos/education/maths/tuts/assignments/ch2/ex1")
                os.mkdir(path + "/Videos/education/maths/tuts/assignments/ch2/ex2")
                os.mkdir(path + "/Videos/education/maths/tuts/assignments/ch2/ex3")
                os.mkdir(path + "/Videos/education/maths/tuts/assignments/ch2/ex4")
                os.mkdir(path + "/Videos/education/maths/tuts/assignments/ch2/ex5")
                os.mkdir(path + "/Videos/education/maths/tuts/assignments/ch1/ex1/q1.1")
                os.mkdir(path + "/Videos/education/maths/tuts/assignments/ch1/ex1/q1.2")
                os.mkdir(path + "/Videos/education/maths/tuts/assignments/ch1/ex1/q1.3")
                os.mkdir(path + "/Videos/education/maths/tuts/assignments/ch1/ex2/q1.4")
                os.mkdir(path + "/Videos/education/maths/tuts/assignments/ch1/ex1/q1.5")
                os.mkdir(path + "/Videos/education/maths/tuts/assignments/ch1/ex1/q1.6")

                stash_folder = path + "/Videos/education/maths/tuts/assignments/ch2/ex4/q1.4"
            except:
                print("Something went wrong while creating the stash directory")
        else:
            # I didn't know what to do here.
            print("Alright")


# Will clear all the stash mess
def clearMess(path, type):
    # /home/gurashish3/Videos
    if type == 5:
        shutil.rmtree(path + '/Videos/education')
        print('Mess cleared')
    elif type == 1:
        shutil.rmtree(path)
        print(path + " has been cleared")

def todo():
    print('todo')


# game
# function for playing rock paper scissor game.
def playRps():
    # variables declared
    choice_name, choice_name2 = '', ''
    choice2 = ''
    player_choice = 0

    while True:
        # player's turn
        choice = input("rock, paper or scissor (r,p,s) : ")

        # player_choice is the int representation of r,p,s
        if choice == 'r':
            player_choice = 1
            choice_name = 'rock'
        elif choice == 'p':
            player_choice = 2
            choice_name = 'paper'
        elif choice == 's':
            player_choice = 3
            choice_name = 'scissor'

        # computer's turn
        comp_turn = random.randint(1, 3)

        if comp_turn == 1:
            choice2 = 'r'
            choice_name2 = 'rock'
        elif comp_turn == 2:
            choice2 = 'p'
            choice_name2 = 'paper'
        elif comp_turn == 3:
            choice2 = 's'
            choice_name2 = 'scissor'

        print('Computer chose : ' + choice_name2)
        asciiArt.rpsArt(choice2)
        print("V/S")
        print('User chose : ' + choice_name)
        asciiArt.rpsArt(choice)

        # condition for winning
        if ((player_choice == 1 and comp_turn == 2) or
                (player_choice == 2 and comp_turn == 1)):
            print("paper wins")
            result = "paper"

        elif ((player_choice == 1 and comp_turn == 3) or
              (player_choice == 3 and comp_turn == 1)):
            print("Rock wins")
            result = "Rock"
        # if a draw
        elif player_choice == comp_turn:
            print("draw")
            result = "draw"
        else:
            print("scissor wins")
            result = "scissor"

        # Printing either user or computer wins
        if result == choice_name:
            print("<== User wins ==>")
        elif result == "draw":
            print("<== No One wins ==>")
        else:
            print("<== Computer wins ==>")

        print('')
        print("Do you want to play again? (Y/N)")
        ans = input()
        if ans == 'n' or ans == 'N':
            break

    print("\nThanks for playing")

    return None


# give the status of the enterprise
# fun function
def status():
    return None


# ----------shutil related function -------------------
# ----------high level directory and files management --------

# the point of the function is to zip a folder up
def zipEmUp(fil_name):
    output = input("Name of the output : ")
    shutil.make_archive(output, 'zip', fil_name)
    return None


# moves the directory tree to another location
def moveDir(src, dst):
    return shutil.move(src, dst)


# need to test
def copyDir(src, dst):
    return shutil.copytree(src, dst)

# can use shutil.diskUsage method to find the storage and stuff.
