#!/usr/bin/env python3
import qrcode
import os
import pyshorteners
from mimesis import Person, Datetime
from mimesis.locales import Locale
from mimesis.enums import Gender
from colorama import init, Fore, Style
init()

# Created by: nobody3132 aka luxe0x64
# previos version was debugged by ChatGPT
# Version: 1.5
# Thanks for using :-)
# Date: 23.08.2024 Update: Added update function


# Clear screen function

def clear_screen():
    os.system('clear')
pass

# QRCoder class
class QRCoder:
    def __init__(self):
        self.url = None
    pass

    def generate_qr_code(self):
        clear_screen()
        print(Fore.CYAN)
        os.system('cat qr_maker_banner.txt')
        print(Fore.WHITE)
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
        os.system('clear')
        print(Fore.YELLOW)
        os.system('cat fakeID_banner.txt')
        print(Fore.WHITE)
        try:
            self.gender = input("Select the gender: ")
            if self.gender == "Male" or self.gender == "male" or self.gender == "Man" or self.gender == "man":
                print(f"Selected gender is: {self.gender} ")
                self.full_name = pn.full_name(gender=Gender.MALE)
                os.system('clear')
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
                        os.system(f'touch output.txt && echo "{self.personal_data}" > output.txt')
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
                os.system('clear')
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
                        os.system(f'touch output.txt && echo "{self.personal_data}" > output.txt ')
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
        print(Fore.RED)
        os.system('cat url_shorter_banner.txt')
        print(Fore.WHITE)
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

class SystemUpdate: # For Debian-based linux only
    def __init__(self):
        self.command_update = "apt update"
    pass

    def check_for_root(self):
        os.system('clear')
        try:
            print("Updating... ")
            os.system('sudo apt update')
            print("Updated. ")
        except KeyboardInterrupt:
            print("Cancelled by user. " + Fore.RED)
        try:
            print("Updating... ")
            os.system('sudo apt update ')
            print("Updated. ")
        except:
            print("Something went wrong. " + Fore.RED)
    pass


class FULLSystemUpdate: # Debian-based linux only
    def __init__(self):
        self.command = "sudo apt upgrade"
    pass

    def FullUpdate(self):
        self.full_system_update = input("Do you wanna do FULL system update?\nY/n: ")
        if self.full_system_update == "Y" or self.full_system_update == "y":
            try:
                print("Updating... ")
                os.system(f"{self.full_system_update}")
                print("Updated. ")
            except KeyboardInterrupt:
                print("Cancelled by user.  " + Fore.RED)
            try:
                os.system(f"{self.full_system_update}")
                print("Updated. ")
            except:
                print("Something went wrong. " + Fore.RED)
        else:
            print("Clossing... ")
            exit()
        print("Thanks for using. ")
    pass


class SystemUpdateArch: # Only for Arch
    def __init__(self):
        self.command_arch = "pacman -Syu"
    pass

    def UpdateArch(self):
        self.update = input("Do you wanna update your system?\nY/n: ")
        if self.update == "Y" or self.update == "y":
            print("Updating... ")
            try:
                os.system(self.command_arch)
                print("Updated. ")
            except KeyboardInterrupt:
                print("Cancelled by user. " + Fore.RED)
            try:
                os.system(self.command_arch)
                print("Updated. ")
            except:
                print("Something went wrong. " + Fore.RED)
        else:
            print("Clossing.... ")
            exit()
        print("Thanks for using ")
    pass

class ProgramUpdate:
    def __init__(self):
        self.current_version = "1.5"
        self.github_link = "https://github.com/luxe0x64/nbtoolkit.git"
        self.script_name = "update.sh"
    pass

    def Updating(self):
        check_for_file = os.system('ls')
        if check_for_file == ".no_updates_required.txt":
            print("No updates required. ")
            time.sleep(3)
            print("No updates required. ")
            os.system('python3 ./nbtoolkit.py')
        else:
            try:
                os.system(f"chmod +x update.sh")
                os.system('./' + self.script_name)
            except:
                print("Something went wrong. " + Fore.RED)
            try:
                os.system(f'chmod +x update.sh')
                os.system('./' + self.script_name)
            except KeyboardInterrupt:
                print("Cancelled by user. " + Fore.RED)
        print("Thanks for using. ")

# Toolkit class to provide menu and handle user choices
class Toolkit:
    def __init__(self):
        self.qr_coder = QRCoder()
        self.fake_id = FakeIdentity()
        self.url_shortener = URLShortener()
        self.update_system = SystemUpdate()
        self.FULL_system_update = FULLSystemUpdate()
        self.Arch_system_update = SystemUpdateArch()
        self.program_update = ProgramUpdate()

    def display_menu(self):
        print(Fore.GREEN)
        os.system('cat toolkit_banner.txt')
        print(Fore.WHITE)
        print("1. QR Code Maker")
        print("2. Fake ID Generator")
        print("3. URL Shortener")
        print("4. Update your system (Debian-based linux only)")
        print("5. FULL update your system (Debian-based linux only)")
        print("6. Update your system (Arch Linux only)")
        print("7. Program Update")
        print("8. Quit")

    def check_for_updates(self):
        try:
            self.program_update.Updating()
        except KeyboardInterrupt:
            print("Cancelled by user. " + Fore.RED)
        try:
            self.program_update.Updating()    
        except:
            print("Something went wrong. " + Fore.RED)
            exit()
    pass

    def run(self):
        self.check_for_updates()
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
                self.update_system.check_for_root()
            elif choice == "5":
                self.FULL_system_update.FullUpdate()
            elif choice == "6":
                self.Arch_system_update.UpdateArch()
            elif choice == "7":
                self.program_update.Updating()
            elif choice == "8":
                os.system('clear')
                print("Closed. ")
                exit()
            else:
                print("Invalid choice. Please try again." + Fore.RED)
            print("Thanks for using.")
        except KeyboardInterrupt:
            print("Cancelled by user. " + Fore.RED)
    pass

if __name__ == "__main__":
    gender = None
    pn = Person()
    dt = Datetime()
    toolkit = Toolkit()
    toolkit.run()