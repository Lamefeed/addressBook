#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from Modules.data import DataFetch, DataAdd, DataEdit, DataExport
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
                  "5. export to txt\n",
                  "6. quit")
            choice = input("Enter the number of the action you want to do:\n\n")

            if choice == '1':
                self.update_data()
            elif choice == '2':
                df = DataFetch()
                print(df.print_content_all())
            elif choice == '3':
                print("Search by using the persons name:\n")
                name = input()
                df = DataFetch()
                df.search_data(name)
            elif choice == '4':
                self.edit_data()
            elif choice == '5':
                de = DataExport()
                de.export_to_txt()
            elif choice == '6':
                sys.exit()

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

    def edit_data(self):
        print("What do you want to edit(Enter the number of the",
              "part you want to change)?\n")
        print(" 1. All\n",
              "2. Name\n",
              "3. Phone numbern\n",
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


m = Main()
while running:
    m.start()
