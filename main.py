#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  main.py
#  Adressbook
#
# This file contains the main logic of the address book.
# It is the starting point for running etc.
#
# Author Secretlamefeederino
# edits: Xenchrarr
#

import time
import getopt
import sys
from Modules.data import DataFetch, DataAdd, DataEdit, DataExport, DataImport
running = True


class Main():

    def start(self):
        print(
            "\n\n\nWelcome to this easy to use address-book",
            "written to be used in the\n" +
            "CLI. This will hopefully give you the ability",
            "to store and search\n" +
            "All of your contact using their name.\n\n\n")
        df = DataFetch()
        df.database_conn()
        while running:
            print("What do you want to do?\n",
                  "1. add a person\n",
                  "2. view address-book\n",
                  "3. search\n",
                  "4. edit\n",
                  "5. Import or export data\n",
                  "6. quit")
            choice = input("Enter the number of the action " +
                           "you want to do:\n\n")

            if choice == '1':
                self.update_data()
            elif choice == '2':
                df = DataFetch()
                print(df.print_content_all())
            elif choice == '3':
                print("Search for a person in the database using their full",
                      " name(if you can't remember parts of the name will",
                      "also work):\n")
                name = input()
                df = DataFetch()
                df.search_data(name)
            elif choice == '4':
                self.edit_data()
            elif choice == '5':
                print("What do you want to do?\n",
                      "1. Export data?\n",
                      "2. Import data?\n")
                answ = input()
                if answ == "1":
                    self.export_data()
                elif answ == "2":
                    self.import_data()
            elif choice == '6':
                sys.exit()
            else:
                print("You need to pick a valid option")

    def update_data(self):
        print("Enter a name:\n")
        name = input()
        print("Enter a phone number:\n")
        phoneNumber = input()
        print("Enter a address:\n")
        address = input()
        print("Enter a email:\n")
        email = input()
        da = DataAdd()
        da.save_data(name, phoneNumber, address, email)

    def export_data(self):
        de = DataExport()
        print("Welcome to the section used to export data!\n",
              "What format would you like to export your table into?\n",
              "Valid formats are: CSV, txt, xlxs")
        answ = input()
        if answ in {"CSV", "csv"}:
            startTime = time.time()
            de.export_csv()
            print("The export was succseful and it took:",
                  (time.time() - startTime), "s")
        elif answ in {"TXT", "txt"}:
            de.export_txt()
            print("Success!")
        else:
            print("Not a valid format")

    def import_data(self):
        di = DataImport()
        file_name = input("What is the filename?\n\t")
        di.import_csv(file_name)
        print("Success!")

    def edit_data(self):
        print("What do you want to edit(Enter the number of the",
              "part you want to change)?\n")
        print(" 1. All\n",
              "2. Name\n",
              "3. Phone number\n",
              "4. Address\n",
              "5. Email\n")
        choice = input()
        if choice == '1':
            print("Enter the name of the contact you want to modify:\n\n")
            cname = input()
            print("Thanks.\nEnter the new name:\n")
            name = input()
            print("Enter the new Phone number:\n")
            phoneNumber = input()
            print("Enter the new Address:\n")
            address = input()
            print("Enter the new email:\n")
            email = input()
            da = DataEdit()
            da.update_database(cname, name, phoneNumber, address, email)
        elif choice == '2':
            print("Enter the name of the contact you want to modify:\n\n")
            cname = input()
            print("Thanks!\nEnter the new name:\n")
            name = input()
            da = DataEdit()
            da.update_database_name(cname, name)
        elif choice == '3':
            print("Enter the name of the contact you want to modify:\n\n")
            cname = input()
            print("Thanks!\nEnter the new phone number:\n")
            phoneNumber = input()
            da = DataEdit()
            da.update_database_number(cname, phoneNumber)
        elif choice == '4':
            print("Enter the name of the contact you want to modify:\n\n")
            cname = input()
            print("Thanks!\nEnter the new address:\n")
            address = input()
            da = DataEdit()
            da.update_database_address(cname, address)
        elif choice == '5':
            print("Enter the name of the contact you want to modify:\n\n")
            cname = input()
            print("Thanks!\nEnter the new email-address:")
            email = input()
            da = DataEdit()
            da.update_database_email(cname, email)
        else:
            print("You need to enter an actual value")

    # Help text to be printed if arguments are mismatching
    def help_text(self):
        return """  -h -help for help
                    -add to add, need be followed by
                        -n and a name
                        -p and a phone number
                        -e and an email
                        -a and an address
                    -pa to print all
                    -s and an search phrase (name atm)"""

    # Main function. It loops through the arguments and see if they match
    # If they match - the data is saved, and some action is taken.
    def main(self, argv):
        df = DataFetch()
        df.database_conn()
        willAdd = False
        phone = ""
        name = ""
        address = ""
        email = ""
        will_print = False
        will_search = False
        search_phrase = ""

        try:
            opts, args = getopt.getopt(
                argv, "h:n:p:a:e:dd:g:s:", [
                    "help=", "phone=", "name=",
                    "address=", "email=", "printall=", "search="])
        except getopt.GetoptError:
            print(self.help_text())
            sys.exit(2)

        # looping through the arguments to find a matching one
        for opt, arg in opts:
            if opt == '-h':
                print(self.help_text())
                sys.exit()

            elif opt in ("-dd"):
                willAdd = True

            elif opt in ("-p", "--phone"):
                phone = arg

            elif opt in ("-a", "--address"):
                address = arg
                print("test")

            elif opt in ("-n", "--name"):
                name = arg

            elif opt in ("-e", "--email"):
                email = arg

            elif opt in ("-g", "--printall"):
                will_print = True

            elif opt in ("-s", "--search"):
                will_search = True
                search_phrase = arg
        # if arguments are supplied, but without print or add, print help text
        if not willAdd and not will_print and not will_search and len(
                opts) > 1:
            print(self.help_text())
        # is true if the -dd arguemnt was added
        if willAdd:
            # if both the -dd and -pa was supplied -
            # add and print, not allowed
            if will_print:
                print(self.help_text())
                sys.exit()
            # if the -dd was used, you need at least to supply a name.
            if name != "":
                # all of this data was fetched from the arguments
                self.save_data(name, phone, address, email)
                sys.exit()
        elif will_print:  # true if -pa was added.
            df = DataFetch()
            print(df.print_content_all())
            sys.exit()

        elif will_search:
            df = DataFetch()
            df.search_data(search_phrase)
            sys.exit()

        else:  # no arguments - run the menu.
            m.start()


m = Main()
while running:
    m.main(sys.argv[1:])
