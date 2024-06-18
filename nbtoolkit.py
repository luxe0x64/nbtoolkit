#!/usr/bin/env python3
import qrcode
import time
import os
import pyshorteners
from mimesis import Person
from mimesis import Datetime
pn = Person()
dt = Datetime()

# Toolkits tool: nbtoolkit. Like: nobody's toolkit
# This toolkit was made by: nobody3132 aka luxe0x64
# Version: 1.0
# Created in 18.06.2024
# Modified in 18.06.2024 at 23:24
# Thanks for using :)
# Enjoy this tool

class QRCoder:
    def __init__(self, URL):
        self.URL = URL
    pass

    def QRMake(self):
        os.system('clear')
        os.system('cat qr_maker_banner.txt')
        self.URL = input("URL: ")
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data('Some data')
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        try:
            img.save('qrcode.png')
            print("QRcode saved. ")
        except:
            print("QRcode is not Saved. ")
    pass

URL = None
QRMaker = QRCoder(URL=None)

class FakeID:
    def __init__(self, full_name, month, year, day, birth_date):
        self.full_name = full_name
        self.month = month
        self.year = year
        self.day = day
        self.birth_date = birth_date
    pass


    def fakeID(self):
        os.system('clear')
        print(f"{full_name}\n{birth_date} ")
        exit()
    pass


full_name = pn.full_name()
day = dt.day_of_month()
month = dt.month()
year = dt.year()
birth_date = day, month, year

fakeIdentity = FakeID(full_name=full_name, month=month, year=year, day=day, birth_date=None)


class URLshorter:
    def __init__(self, s, short_link, users_input, wanna_save_in_file ):
        self.users_input = users_input
        self.s = s
        self.short_link = short_link
        self.wanna_save_in_file = wanna_save_in_file
    pass

    def makeShortLink(self):
        os.system('clear')
        os.system('cat url_shorter_banner.txt')
        users_input = input("Enter URL: ")
        print("URL entered. ")
        print(short_link)
        wanna_save_in_file = input("Wanna save URL in file?\nY/n: ")
        if wanna_save_in_file == "Y" or wanna_save_in_file == "y":
            try:
                os.system(f'touch short_link.txt && echo "{short_link} > short_link.txt" ')
                print("URL saved in file. ")
            except:
                print("Something went wrong. ")
        else:
            print("Ok. ")
            exit()
        pass
    pass

users_input = None
wanna_save_in_file = None
s = pyshorteners.Shortener()
short_link = (s.tinyurl.short(f'{users_input}'))
ShortedLink = URLshorter(users_input=None, wanna_save_in_file=None, s=s, short_link=short_link)


class Toolkit:
    def __init__(self, choice):
        self.choice = choice
    pass

    def Choice(self):
        os.system('clear')
        os.system('cat toolkit_banner.txt')
        self.choice = input("1 For QRMaker\n2 For FakeID\n3 For URl Shorterner\n4 for Quit\n\nChoice: ")
        if self.choice == "1":
            QRCoder(URL=None)
            QRMaker.QRMake()
        elif self.choice == "2":
            FakeID(full_name=full_name, month=month, day=day, year=year, birth_date=None)
            fakeIdentity.fakeID()
        elif self.choice == "3":
            URLshorter(users_input=None, wanna_save_in_file=None, s=s, short_link=short_link)
            ShortedLink.makeShortLink()
        elif self.choice == "4":
            exit()
        else:
            print("Option not Found. ")
        print("Thanks for using. ")
    pass

choice = None
MyToolkit = Toolkit(choice=None)
MyToolkit.Choice()
