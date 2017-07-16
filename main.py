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


import sys, getopt
from Modules.data import DataFetch, DataAdd
running = True


class Main():

    def __init__(self):
        pass

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
                  # "4. export to txt\n",
                  "5. quit")
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
            # elif choice == '4':
            #     de = DataExport()
            #     de.export_to_txt()
            elif choice == '5':
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
        self.save_data(name, phoneNumber, address, email)


    def save_data(self, name, phone_number, address, email):
        da = DataAdd()
        da.save_data(name, phone_number, address, email)


# Help text to be printed if arguments are mismatching
    def help_text(self):
        return '''
            -h -help for help
            -add to add, need be followed by
                -n and a name
                -p and a phone number
                -e and an email
                -a and an address

            -pa to print all

            -s and an search phrase (name atm)

        '''


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
            opts, args = getopt.getopt(argv, "h:n:p:a:e:dd:g:s:", ["help=", "phone=", "name=", "address=", "email=", "printall=", "search="])
        except getopt.GetoptError:
            print (self.help_text())
            sys.exit(2)

        # looping through the arguments to find a matching one
        for opt, arg in opts:
            if opt == '-h':
                print (self.help_text())
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

        if not willAdd and not will_print and not will_search and len(opts) > 1: # if arguments are supplied, but without print or add, print help text
            print(self.help_text())


        if willAdd: # is true if the -dd argument was added
            if will_print: # if both the -dd and -pa was supplied - add and print, not allowed
                print(self.help_text())
                sys.exit()
            if name != "": # if the -dd was used, you need at least to supply a name.
                self.save_data(name, phone, address, email) # all of this data was fetched from the arguments
                sys.exit()
        elif will_print: # true if -pa was added.
            df = DataFetch()
            print(df.print_content_all())
            sys.exit()

        elif will_search:
            df = DataFetch()
            df.search_data(search_phrase)
            sys.exit()

        else: # no arguments - run the menu.
            m.start()




m = Main()
while running:
    m.main(sys.argv[1:])
    # m.start()
