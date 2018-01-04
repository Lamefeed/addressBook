import sqlite3
import json
import csv
# import sys
conn = sqlite3.connect('addressBook.db')
c = conn.cursor()


class DataFetch():

    def database_conn(self):
        c.execute('''CREATE TABLE IF NOT EXISTS book
                  (name, phoneNumber, address, email)''')
        conn.commit()

    def search_data(self, name):
        t = ('%'+name+'%', )
        content = c.execute('SELECT * FROM book WHERE name LIKE ?',
                            t).fetchall()
        print(json.dumps(content, sort_keys=True, indent=4))

    def print_content_all(self, json_str=False):
        content = c.execute('SELECT * FROM book').fetchall()

        if json_str:
            return json.dumps([dict(ix) for ix in content])

        return(json.dumps(content, sort_keys=True, indent=4))


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
                  email =?,
                  WHERE name =?''',
                  (name, phoneNumber, address, email, cname))
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
    # This class will contain multiple functions for exporting data
    def export_csv(self):
        c.execute("SELECT * FROM book")
        content = c.fetchall()
        with open('data.csv', 'a') as out:
            writer = csv.writer(out, lineterminator='\n')
            writer.writerows(content)

    def export_txt(self):
        c.execute("SELECT * FROM book")
        content = c.fetchall()
        with open('data.txt', 'a') as out:
            writer = out.writer(out, lineterminator='\n')
            writer.writerows(content)


class DataImport():
    # This call will ontain multiple function for importing data for different,
    # file formats and into the SQLite3 database
    def import_csv(self, file_name):
        with open(file_name, 'r+') as f:
            dr = csv.DictReader(f)  # comma is default delimiter
            to_db = [(i['Name'],
                      i['Number'],
                      i['Address'],
                      i['Email']) for i in dr]

        c.executemany("""INSERT INTO book (name, phoneNumber, address, email)
                      VALUES (?, ?, ?, ?);""", to_db)
        conn.commit()
