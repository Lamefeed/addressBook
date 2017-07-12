import sqlite3
import json
conn = sqlite3.connect('addressBook.db')
c = conn.cursor()


class DataFetch():

    def database_conn(self):
        c.execute('''CREATE TABLE IF NOT EXISTS book
                  (name, phoneNumber, address, email)''')
        conn.commit()

    def search_data(self, name):
        t = (name, )
        c.execute('SELECT * FROM book WHERE name=?', t)
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
    pass
