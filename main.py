import sys
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
                  "4. quit")
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


m = Main()
while running:
    m.start()
