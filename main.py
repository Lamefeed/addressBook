import sqlite3
import sys
import json
running = True
conn = sqlite3.connect('addressBook.db')
conn.row_factory = sqlite3.Row
c = conn.cursor()


class Main():

    def __init__(self):
        pass

    def start(self):
        print(
            "Welcome to this easy to use address-book",
            "written to be used in the\n",
            "CLI. This will hopefully give you the ability",
            "to store and search\n",
            "All of your contact using their name.")
        self.database_conn()
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
                print(self.print_content_all(json_str=True))
            elif choice == '3':
                print("Search by using the persons name:\n")
                name = input()
                self.search_data(name)
            elif choice == '4':
                sys.exit()

    def database_conn(self):
        c.execute('''CREATE TABLE IF NOT EXISTS book
                  (name, phoneNumber, address, email)''')

    def update_data(self):
        print("Enter a name:\n")
        name = input()
        print("Enter a phone number:\n")
        number = input()
        print("Enter a address:\n")
        address = input()
        print("Enter a email:\n")
        email = input()
        c.execute('''INSERT INTO book(name, phoneNumber, address, email)
                  VALUES(?, ?, ?, ?)''', (name, number, address, email))
        conn.commit()

    def print_content_all(self, json_str=False):
        content = c.execute('SELECT * FROM book').fetchall()

        if json_str:
            return json.dumps([dict(ix) for ix in content])

        return content

    def search_data(self, name):
        t = (name, )
        c.execute('SELECT * FROM book WHERE name=?', t)
        print(c.fetchone())

m = Main()
while running:
    m.start()
