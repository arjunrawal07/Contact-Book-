
import argparse
from peewee import *
from datetime import date
db = PostgresqlDatabase('contactbook', user='postgres', password='',
                        host='localhost', port=5432)


class BaseModel(Model):
    class Meta:
        database = db


class Entry(BaseModel):
    first_name = CharField()
    last_name = CharField()
    address = CharField()
    phone_number = CharField()
    birthday = DateField()


db.connect()
db.drop_tables([Entry])
db.create_tables([Entry])

arjun = Entry(first_name='Arjun', last_name='Rawal', address='34 Viper Way, Fang, TX, 20001',
              phone_number='123-456-7890', birthday=date(1994, 8, 13))
arjun.save()

dolores = Entry(first_name='Dolores', last_name='Umbridge', address='1234 Owls Lane',
                phone_number='567-943-0943', birthday=date(1980, 4, 23))
dolores.save()

begin = input(
    "What would you like to do? Find a contact or create a new entry? Find = Find, Create = Create ")

if begin == "Find":
    # Query by First Name
    single_entry = input(
        "To search for a single contact, enter the contact's first name: ")
    single_query = Entry.get(Entry.first_name == single_entry)
    print(f"{single_query.first_name} {single_query.last_name} {single_query.address} {single_query.phone_number} {single_query.birthday}")

elif begin == "Create":
    # Create a new Entry

    create_first_name = input(
        "Follow the prompts to create a new entry. First name: ")
    create_last_name = input(
        "Last name: "
    )
    create_address = input("Address: ")
    create_phone_number = input("Phone Number (000-000-0000)")
    create_birthday = input("Birthday (YYYY, MM, DD): ")

    new_entry = Entry.create(first_name=create_first_name, last_name=create_last_name,
                             address=create_address, phone_number=create_phone_number, birthday=create_birthday)
    new_entry.save()
    print(f"{new_entry.first_name} {new_entry.last_name} {new_entry.address} {new_entry.phone_number} {new_entry.birthday}")
