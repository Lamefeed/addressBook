# The AddressBook!


As of writing this the addressbook program is in pre-alpha, this will change as I've what I consider to be the 
required amount of features to call it alpha.
As you might already know this program only supports CLI(command line interface), this is to push people into becoming comfy using such a powerfull tool.


## Features as we speak
* Adding people
* Printing everything
* Searching for people in the book
* Editing existing people
* Exporting from db to a different medium(for backup)
* Importing from csv to db


# Using the addressbook:


## Exporting and importing files:

If you want to use the function to import contacts from anywhere, please use
this formatting:

Name        |Number     |Address      |Email
------------|-----------|-----------|----------
Test        |404        |Testaddress|test@example.example
                
If you want to use another type of formatting change this section in
Modules/data.py:

'''python
def import_csv(self, file_name):
    with open(file_name, 'r+') as f:
        dr = csv.DictReader(f)  # comma is the default delimiter
        to_db = [(i['Name'],
                  i['Number],
                  i['Address'],
                  i['Email']) for i in dr]

        
    c.executemay("""INSERT INTO book (name, phoneNumber, address, email)
                    VALUES (?, ?, ?, ?);""", to_db)
    conn.commit()
'''
## Branches
The branches are as following:
* Master(Stable)
* Beta(Development)

## Run
Requirements:
* python 3.6

## What's next
 Making a graphical user interface so that all the normies can use this addressbook. I will also update the CLI client so that it looks better than what it currently does. 

