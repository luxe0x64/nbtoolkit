#!/usr/bin/env python3
import qrcode
from os import system
import pyshorteners
from mimesis import Person, Datetime
from mimesis.locales import Locale
from mimesis.enums import Gender
from colorama import init, Fore
init()

# Created by: nobody3132 aka luxe0x64
# previos version was debugged by ChatGPT
# Version: 1.5
# Thanks for using :-)


# Clear screen function

def clear_screen():
    system('clear')
pass

# QRCoder class
class QRCoder:
    def __init__(self):
        self.url = None
    pass

    def generate_qr_code(self):
        clear_screen()
        system('cat qr_maker_banner.txt')
        self.url = input("URL: ")
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(self.url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        try:
            img.save('qrcode.png')
            print("QR code saved.")
        except Exception as e:
            print(f"QR code not saved. Error: {e}")
    pass

# FakeID class
class FakeIdentity:
    def __init__(self):
        self.gender = None
    pass

    def Users_input(self):
        system('clear')
        system('cat fakeID_banner.txt')
        try:
            self.gender = input("Select the gender: ")
            if self.gender == "Male" or self.gender == "male" or self.gender == "Man" or self.gender == "man":
                print(f"Selected gender is: {self.gender} ")
                self.full_name = pn.full_name(gender=Gender.MALE)
                system('clear')
                print(self.full_name)
                print("Generating birth date.... ")
                self.year = dt.year(minimum=1990, maximum=2001)
                self.month = dt.month()
                self.day = dt.day_of_month()
                self.birth_date = self.day, self.month, self.year
                print(self.birth_date)
                self.personal_data = self.full_name, self.birth_date
                self.save_in_file = input("Do you wanna save in file?\nY/n: ")
                if self.save_in_file == "Y" or self.save_in_file == "y":
                    print("saving...")
                    try:
                        system(f'touch output.txt && echo "{self.personal_data}" > output.txt')
                        print(Fore.GREEN)
                        print("saved. ")
                        print(Fore.WHITE)
                        exit()
                    except:
                        exit()
                else:
                    print("OK")
                pass
            elif self.gender == "Female" or self.gender == "female" or self.gender == "Woman" or self.gender == "woman":
                print(f"Sleected gender is : {self.gender} ")
                self.full_name = pn.full_name(gender=Gender.FEMALE)
                system('clear')
                print(self.full_name)
                print("Generating birth date.... ")
                self.year = dt.year(minimum=1990, maximum=2001)
                self.month = dt.month()
                self.day = dt.day_of_month()
                self.birth_date = self.day, self.month, self.year
                print(f"Birth date: {self.birth_date} ")
                self.personal_data = self.full_name, self.birth_date
                self.save_in_file = input("Do you wanna save in file?\nY/n: ")
                if self.save_in_file == "Y" or self.save_in_file == "y":
                    print("saving....")
                    try:
                        system(f'touch output.txt && echo "{self.personal_data}" > output.txt ')
                        print(Fore.GREEN)
                        print("saved. ")
                        print(Fore.WHITE)
                        exit()
                    except:
                        exit()
                else:
                    print("OK.")
                    exit()
            else:
                print(Fore.RED)
                print("Invalid gender. ")
                print(Fore.WHITE)
                exit()
        except KeyboardInterrupt:
            print(Fore.RED)
            print("Cancelled by user. ")
            print(Fore.WHITE)
    pass




# URLShortener class
class URLShortener:
    def __init__(self):
        self.shortener = pyshorteners.Shortener()
        self.url = None
        self.short_link = None

    def shorten_url(self):
        clear_screen()
        system('cat url_shorter_banner.txt')
        self.url = input("Enter URL: ")
        self.short_link = self.shortener.tinyurl.short(self.url)
        print(f"Shortened URL: {self.short_link}")
        try:
            save = input("Do you want to save the short URL to a file? (Y/n): ").lower()
            if save == 'y':
                self.save_to_file(self.short_link)
        except KeyboardInterrupt:
            print(Fore.RED)
            print("Cancelled by user. ")
            print(Fore.WHITE)
    def save_to_file(self, data, filename='short_link.txt'):
        try:
            with open(filename, 'w') as file:
                file.write(data)
            print("URL saved to file.")
        except Exception as e:
            print(f"Failed to save URL to file. Error: {e}")

# Toolkit class to provide menu and handle user choices
class Toolkit:
    def __init__(self):
        self.qr_coder = QRCoder()
        self.fake_id = FakeIdentity()
        self.url_shortener = URLShortener()

    def display_menu(self):
        clear_screen
        system('cat toolkit_banner.txt')
        print("1. QR Code Maker")
        print("2. Fake ID Generator")
        print("3. URL Shortener")
        print("4. Quit")

    def run(self):
        clear_screen()
        self.display_menu()
        try:
            choice = input("Choice: ")
            if choice == "1":
                self.qr_coder.generate_qr_code()
            elif choice == "2":
                self.fake_id.Users_input()
            elif choice == "3":
                self.url_shortener.shorten_url()
            elif choice == "4":
                exit()
            else:
                print("Invalid choice. Please try again.")
            print("Thanks for using.")
        except KeyboardInterrupt:
            print(Fore.RED)
            print("Cancelled by user. ")
            print(Fore.WHITE)
    pass

if __name__ == "__main__":
    gender = None
    pn = Person()
    dt = Datetime()
    toolkit = Toolkit()
    toolkit.run()
