
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

single_entry = input(
    "To search for a single contact, enter the contact's first name: ")
query = Entry.get(Entry.first_name == single_entry)
print(f"{query.first_name} {query.last_name} {query.address} {query.phone_number} {query.birthday}")
