#!/usr/bin/env python3

import extras


def intro_func():
    print('Hello, This is Gideon. How may I help you?')
    print("type help for help")


"""
Notes: I have decided  not to implement text feature. It was being really annoying. 
"""
if __name__ == '__main__':
    # service.py executed as script
    # do something
    intro_func()
    while True:
        # input should figure out automatically the input type.
        command = input()
        # here the commands will be evaluated.
        if command == 'quit':
            break
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
            subject = input("Enter the subject of E-mail : ")
            body = input("Enter the body of E-mail : ")
            receiver = input("Enter the E-mail of recipient : ")
            extras.sendEmail(subject, body, receiver)

        # A simple python scrapper
        elif command == "stock info":
            print("stock info")
        # gotta implement namp feature here
        # nmap will have to wait for now.
        elif command == "defense":
            address = input("ip address to scan : ")
            print("Starting Scan")
            extras.nmapScan(address)
            # print("nmap time ")
        # gotta implement namp feature here
        elif command == "help":
            print("help time")
        # The point of this command will be to send a text message to wife with some excuse.
        elif command == "emergency":
            print("emergency")
