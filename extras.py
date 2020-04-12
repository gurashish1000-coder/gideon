#!/usr/bin/env python3
from __future__ import unicode_literals
import datetime
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import shutil
import asciiArt
import random
import speedtest
from pytube import YouTube
from pytube import Playlist

# Global variables will be declared here
stash_folder = ""
curr_path = ''


# intro function: executes the intro
def intro_func():
    print('Hello, This is Gideon. AI created by Star Fleet.')
    # prints the star fleet logo
    asciiArt.starFleet()
    print("type help for help")


# Method to show the current date and time.
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
        mode = input("Please enter your expression:")
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
        current_temperature = y["temp"]
        temp_celsius = int(current_temperature - 273.15)
        current_pressure = y["pressure"]
        current_humidity = y["humidity"]
        z = x["weather"]
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
    password = ''
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
# todo need to implemement this function
def setTimer():
    print('Timer set')


# Downloads a youtube video
def youtubeDownload(link, type):
    try:
        yt = YouTube(link)

        # printing all the necessary information about the media.
        print('==================================')
        print('|Title           = ' + yt.title)
        print('==================================')
        print('|Description     = ' + yt.description)
        print('==================================')
        print('|Views           = ' + str(yt.views))
        print('|Length          = ' + str(yt.length) + ' seconds')
        print('|Rating          = ' + str(yt.rating))
        print('|Thumbnail       = ' + yt.thumbnail_url)
        print('==================================')

        if type == 'video':
            result_video = yt.streams.get_highest_resolution()
            try:
                # downloading the video
                result_video.download()
            except:
                print("Some Error!")
            print('Video downloading finished')

        # for only downloading the audio
        elif type == 'audio':
            result_video = yt.streams.get_audio_only()
            try:
                # downloading the video
                result_video.download()
            except:
                print("Some Error!")
            print('Audio downloading finished')
    except:
        print("Connection Error")


# Downloads all the videos from a youtube playlist
def playlistDownload(link, type):
    try:
        playlist = Playlist(link)
        print('Number of videos in playlist: %s' % len(playlist.video_urls))
        # downloading everything as a video
        if type == 'video':
            for i in playlist.video_urls:
                try:
                    yt = YouTube(i)
                    print("Video downloading : " + yt.title)
                    result_video = yt.streams.get_highest_resolution()
                    result_video.download()
                    # print(i)
                except:
                    print("Some Error!")
                    return 0
            return 1

        # downloading everything as a audio.
        if type == 'audio':
            for i in playlist.video_urls:
                try:
                    yt = YouTube(i)
                    print("Video downloading : " + yt.title)
                    result_video = yt.streams.get_audio_only()
                    result_video.download()
                    # print(i)
                except:
                    print("Some Error!")
                    return 0
            return 1
    except:
        print('Connection Error')
        return 0


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
    return None


'''
google news api key 065c7994498f4d8aaa01a0fa4c5106bd
The following function provides detailed stuff about the news like summary and stuff.
det short for detailed
'''
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
    return None


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


# Will clear all the stash dir mess
def clearMess(path, type):
    # /home/gurashish3/Videos
    if type == 5:
        shutil.rmtree(path + '/Videos/education')
        print('Mess cleared')
    elif type == 1:
        try:
            shutil.rmtree(path)
            print(path + " has been cleared")
        except:
            print('Something went wrong. Folder might not be there. ')

# todo implement this feature
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
# todo need to do this function
def status():
    return None


# can use shutil.diskUsage method to find the storage and stuff.
# install pip install speedtest-cli
def testSpeed():
    st = speedtest.Speedtest()
    option = int(input('''What speed do you want to test:   
    1) Download Speed   
    2) Upload Speed   
    3) Ping  
    Your Choice: '''))

    if option == 1:
        result = st.download()
        print("Your download speed is : " + str(int(result / 1000000)) + "mb/s")

    elif option == 2:
        result = st.upload()
        print("Your upload speed is : " + str(int(result / 1000000)) + "mb/s")
    elif option == 3:
        servernames = []
        st.get_servers(servernames)
        print("Your ping is : " + st.results.ping)
    else:
        print("Please enter the correct choice !")
    return None


'''
Gets the geolocation of a ipaddress and other useful info using a ip address
uses the api service from ipstack.com
the below api_key is valid for 10000 requests/month.
'''
def geoLocation(ip_address):
    api_key = 'de115059d356f8d603f3eede0058c5b1'
    complete_url = 'http://api.ipstack.com/' + ip_address + '?access_key=' + api_key
    response = requests.get(complete_url)
    result = response.json()
    country = result["country_name"]
    region = result["region_name"]
    city = result["city"]
    zip = result["zip"]
    type = result["type"]
    call_code = result["location"]["calling_code"]
    # printing values
    print('==================================')
    print('|Location        = ' + (country + ', ' + region + ', ' + city) + '|')
    print('==================================')
    print('|zip code        = ' + zip)
    print('|calling code    = ' + call_code)
    print('|type            = ' + type)
    print('==================================')
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

