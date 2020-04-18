#!/usr/bin/env python3

import extras
import asciiArt
import os
from os import path

"""
Notes: I have decided  not to implement text feature. It was being really annoying. 
"""
if __name__ == '__main__':
    # global variable
    global user_dict
    # service.py executed as script
    # do something
    extras.intro_func()
    defaultPath = os.path.abspath(".")
    # checking if the user.info exists
    if path.exists('user.info') != True:
        print('Hello, This is Gideon. AI created by Star Fleet.')
        print('Before we continue we need to create a setup for you.')
        extras.create_setup()
        user_dict = extras.load_setup()
    else:
        # making user dict global
        user_dict = extras.load_setup()
        print('Welcome back ' + user_dict['name'])

    while True:
        # input should figure out automatically the input type.
        command = input('How may I help you : ')

        # here the commands will be evaluated.
        if command == 'quit':
            break

        # prints all the commands and their info
        elif command == "help":
            extras.help()

        # Temporary setup
        # Creating a secret folder for stash
        # Part of the directory management feature
        elif command == 'setup':
            extras.createStashDir()

        # clears the directory tree made by setup command
        elif command == 'clear stash':
            extras.clearMess()

        # calculate stuff
        elif command == "calculate":
            extras.calculate()

        # Command shows the time
        elif command == "time":
            extras.showTime()

        # shows the weather.
        elif command == "weather":
            extras.showWeather()

        # sends an email through an outlook email address
        elif command == "email":
            sender_email = user_dict['email']
            sender_password = user_dict['password']
            try:
                subject = input("Enter the subject of E-mail : ")
                body = input("Enter the body of E-mail : ")
                receiver = input("Enter the E-mail of recipient : ")
                extras.sendEmail(sender_email, sender_password, subject, body, receiver)
            except:
                print('Something went wrong. Please make sure that sender email is correct.')
                print('If the problem keeps o persisting. PLease make sure your email address and password is correct.')

        # Download a youtube video.
        elif command == "download youtube":
            temp = 0
            link = input("Enter the link of the video to download : ")
            # link = 'https://www.youtube.com/watch?v=OPGtpO1g_jk'
            while temp != 1:
                choice = input("audio or video ? = ")
                if choice == "audio":
                    temp = 1
                    extras.youtubeDownload(link, 'audio')
                elif choice == "video":
                    temp = 1
                    extras.youtubeDownload(link, 'video')
                else:
                    print("Please only write audio or video")

        # Download everything in a youtube playlist
        # link = 'https://www.youtube.com/playlist?list=PLBf0hzazHTGM8V_3OEKhvCM9Xah3qDdIx'
        elif command == "playlist download":
            temp = 0
            link = input("Enter the link of the playlist to download : ")
            while temp != 1:
                choice = input("audio or video ? = ")
                if choice == "audio":
                    temp = 1
                    if extras.playlistDownload(link, "audio") == 1:
                        print('Downloading finished')
                elif choice == "video":
                    temp = 1
                    if extras.playlistDownload(link, "video") == 1:
                        print('Downloading finished')
                else:
                    print("Please only write 'audio' or 'video'")

        # Prints all the important news for today. Basically only headlines.
        # Uses my personal api key
        # If it doesn't work anymore get your own api key and replace with mine.
        elif command == "top news":
            extras.topNews()

        # Command to provide the detailed news
        elif command == "det news":
            extras.detNews()

        # playing rock paper scissor with computer.
        elif command == "rps":
            extras.playRps()

        # To show the current status of enterprise.
        elif command == "status":
            extras.status()

        # need to test
        # should zip any files or directories mentioned.
        elif command == "zip":
            name = input("name of the file to zip or directory path : ")
            extras.zipEmUp()

        # move dir tree to another location
        elif command == "move dir":
            path = input("path of the dir to move : ")
            dst = input("path to move the directory and subdirectories to  : ")
            print(extras.moveDir(path, dst))

        # copy dir tree to another location
        elif command == "copy dir":
            path = input("path of the dir to copy : ")
            dst = input("path/location to copy the directory and subdirectories to  : ")
            print(extras.copyDir(path, dst))

        # function to test speed using the speed-cli module.
        elif command == "test speed":
            extras.testSpeed()
        elif command == "ip location":
            ip = input("Enter the ip address to look for : ")
            extras.geoLocation(ip)

        # ///////////////////////////////////////////////////
        # all implemented delete commands below
        # ////////////////////////////////////////////////////

        # deletes the saved stash folder
        elif command == "delete stash":
            # type 5 is a special path. defaultPath + rest of stash directory path
            extras.clearMess(defaultPath, 5)

        # deletes any file or directory tree.
        elif command == "delete dir":
            print("WARNING: Everything in and the directory will be deleted")
            choice = input("Do you still wanna proceed (y/n) : ")
            if choice == 'y':
                path = input("What directory you want to delete : ")
                # adds nothing more to the path
                extras.clearMess(defaultPath, 1)
            else:
                print('alright')

        # delete a file
        elif command == "delete":
            try:
                path = input("File path to delete : ")
                os.remove(path)
                print("File removed!")
            except:
                print("Make sure the path leads to a file and not a directory")
                print("If you wanna delete a dir use command |delete dir| ")

        # todo in future
        # A simple python stock scrapper
        elif command == "stock info":
            print("stock info")

        # todo implement namp feature here
        # nmap will have to wait for now.
        elif command == "defense":
            address = input("ip address to scan : ")
            print("Starting Scan")
            # print("nmap time ")

        # The point of this command will be to send a text message to wife with some excuse.
        elif command == "emergency":
            print("emergency")

        else:
            print('I don not understand')
