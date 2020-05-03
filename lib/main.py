
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
# db.drop_tables([Entry])
db.create_tables([Entry])

# arjun = Entry(first_name='Arjun', last_name='Rawal', address='34 Viper Way, Fang, TX, 20001',
#               phone_number='123-456-7890', birthday=date(1994, 8, 13))
# arjun.save()

# dolores = Entry(first_name='Dolores', last_name='Umbridge', address='1234 Owls Lane',
#                 phone_number='567-943-0943', birthday=date(1980, 4, 23))
# dolores.save()


def search_Contacts():
    begin = input(
        "What would you like to do? Find a contact or create a new entry? Find = Find, FindAll = FindAll, Create = Create, Update = Update, Delete = Delete ")

    if begin == "Find":
        # Query by First Name
        single_entry = input(
            "To search for a single contact, enter the contact's first name: ")
        single_query = Entry.get(Entry.first_name == single_entry)
        print(f"{single_query.first_name} {single_query.last_name} {single_query.address} {single_query.phone_number} {single_query.birthday}")
        next = input(
            'Would you like to continue searching your contactbook? (Y/N) If not, the app will exit: ').lower()
        if next == "y":
            search_Contacts()

    elif begin == "Create":
        # Create a new Entry
        create_first_name = input(
            "Follow the prompts to create a new entry. First name: ")
        create_last_name = input(
            "Last name: "
        )
        create_address = input("Address: ")
        create_phone_number = input("Phone Number (000-000-0000): ")
        create_birthday = input("Birthday (YYYY MM DD): ")

        new = Entry(first_name=create_first_name, last_name=create_last_name,
                    address=create_address, phone_number=create_phone_number, birthday=create_birthday)
        new.save()

        print(
            f'{new.first_name} {new.last_name} {new.address} {new.phone_number} {new.birthday}')

        next = input(
            'Would you like to continue searching your contactbook? (Y/N) If not, the app will exit: ').lower()
        if next == "y":
            search_Contacts()

    elif begin == "FindAll":
        for contact in Entry.select():
            print(
                f"{contact.first_name} {contact.last_name}, {contact.address}, {contact.phone_number}, {contact.birthday}")
        next = input(
            'Would you like to continue searching your contactbook? (Y/N) If not, the app will exit: ').lower()
        if next == "y":
            search_Contacts()
    elif begin == "Update":
        for contact in Entry.select():
            print(
                f"{contact.first_name} {contact.last_name}, {contact.address}, {contact.phone_number}, {contact.birthday}")
        single_entry = input(
            "Find the contact you want to update by typing in their first name: ")
        single_query = Entry.get(Entry.first_name == single_entry)
        print(f"{single_query.first_name} {single_query.last_name} {single_query.address} {single_query.phone_number} {single_query.birthday}")

        question_update = input(
            'What would you like to update?\nFirst Name = First Name\n Last Name = Last Name\n Address = Address\n Phone Number = Phone Number\n Birthday = Birthday ')
        if question_update == "First Name":
            new_first_name = input('Enter the updated first name: ')
            single_query.first_name = new_first_name
            single_query.save()
            print(f"{single_query.first_name} {single_query.last_name} {single_query.address} {single_query.phone_number} {single_query.birthday}")
        elif question_update == "Last Name":
            new_last_name = input('Enter the updated last name: ')
            single_query.last_name = new_last_name
            single_query.save()
            print(f"{single_query.first_name} {single_query.last_name} {single_query.address} {single_query.phone_number} {single_query.birthday}")
        elif question_update == "Address":
            new_address = input('Enter the updated address: ')
            single_query.address = new_address
            single_query.save()
            print(f"{single_query.first_name} {single_query.last_name} {single_query.address} {single_query.phone_number} {single_query.birthday}")
        elif question_update == "Phone Number":
            new_phone_number = input("Enter the updated phone number")
            single_query.phone_number = new_phone_number
            single_query.save()
            print(f"{single_query.first_name} {single_query.last_name} {single_query.address} {single_query.phone_number} {single_query.birthday}")
        next = input(
            'Would you like to continue searching your contactbook? (Y/N) If not, the app will exit: ').lower()
        if next == "y":
            search_Contacts()
    elif begin == "Delete":
        for contact in Entry.select():
            print(
                f"{contact.first_name} {contact.last_name}, {contact.address}, {contact.phone_number}, {contact.birthday}")
        single_entry = input(
            "Find the contact you want to delete by typing in their first name: ")
        single_query = Entry.get(Entry.first_name == single_entry)
        print(f"{single_query.first_name} {single_query.last_name} {single_query.address} {single_query.phone_number} {single_query.birthday}")

        single_query.delete_instance()
        for contact in Entry.select():
            print(
                f"{contact.first_name} {contact.last_name}, {contact.address}, {contact.phone_number}, {contact.birthday}")
        next = input(
            'Would you like to continue searching your contactbook? (Y/N) If not, the app will exit: ').lower()
        if next == "y":
            search_Contacts()


search_Contacts()
db.close()
