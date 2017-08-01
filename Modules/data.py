import sqlite3
import json
import csv
import sys
conn = sqlite3.connect('addressBook.db')
c = conn.cursor()


class DataFetch():

    def database_conn(self):
        c.execute('''CREATE TABLE IF NOT EXISTS book
                  (name, phoneNumber, address, email)''')
        conn.commit()

    def search_data(self, name):
        t = ('%'+name+'%', )
        c.execute('SELECT * FROM book WHERE name LIKE ?', t)
        print(c.fetchone())

    def print_content_all(self, json_str=False):
        content = c.execute('SELECT * FROM book').fetchall()

        if json_str:
            return json.dumps([dict(ix) for ix in content])

        return(content)


class DataAdd():

    def save_data(self, name, phoneNumber, address, email):
        c.execute('''INSERT INTO book(name, phoneNumber, address, email)
                  VALUES(?, ?, ?, ?)''', (name, phoneNumber, address, email))
        conn.commit()


class DataEdit():

    def update_database_all(self, cname, name, phoneNumber, address, email):
        c.execute('''UPDATE book SET
                  name =?,
                  phoneNumber =?,
                  address =?,
                  email =?
                  WHERE name =?
                  ''', (name, phoneNumber, address, email, cname))
        conn.commit()

    def update_database_name(self, cname, name):
        c.execute('''UPDATE book SET
                  name =?
                  WHERE name =?''', (name, cname))
        conn.commit()

    def update_database_number(self, cname, phoneNumber):
        c.execute('''UPDATE book SET
                  phoneNumber =?
                  WHERE name =?''', (phoneNumber, cname))
        conn.commit()

    def update_database_address(self, cname, address):
        c.execute('''UPDATE book SET
                  address =?
                  WHERE name =?''', (address, cname))
        conn.commit()

    def update_database_email(self, cname, email):
        c.execute('''UPDATE book SET
                  email =?
                  WHERE name =?''', (email, cname))


class DataExport():

    def export_csv(self):

        c.execute("SELECT * FROM book")
        content = c.fetchall()
        with open('data.csv', 'a') as out:
            writer = csv.writer(out, lineterminator='\n')
            writer.writerows(content)
