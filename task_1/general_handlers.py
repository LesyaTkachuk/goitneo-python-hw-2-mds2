from pathlib import Path
from constants import EMPTY_PHONEBOOK, INVALID_COMMAND

CONTACTS_FILE_PATH = Path(__file__).parent / "contacts.txt"


def show_command_list(*args, **kwargs):
    return """
    *****************************
    add <name> <phone>      --> to add a contact with the provided phone number to the phonebook
    change <name> <phone>   --> to change the existing contact's phone number
    phone <name>            --> to display the existing contact's phone number
    delete <name>           --> to delete provided contact with a phone number from the phonebook
    all                     --> to display the whole phone book
    exit | stop | close     --> to exit and store contacts
    ******************************
    """


def show_unknown_command(*args, **kwargs):
    return INVALID_COMMAND


def greet_user(*args, **kwargs):
    return "Hello! How can I help you?"


def read_contacts():
    contacts = {}
    try:
        with open(CONTACTS_FILE_PATH, "r") as fh:
            contacts_list = fh.readlines()
            for contact in contacts_list:
                splitted_contact = contact.split()
                contacts[splitted_contact[0].rstrip(":")] = splitted_contact[1].rstrip(
                    "\n"
                )
    except FileNotFoundError:
        print(EMPTY_PHONEBOOK)
    except:
        print("There was an error while reading the phonebook")

    return contacts


def close_assistant(*args, contacts):
    if contacts:
        contact_list = list()
        for key, value in contacts.items():
            contact_list.append(f"{key}: {value}\n")
        with open(CONTACTS_FILE_PATH, "w") as fh:
            fh.writelines(contact_list)

    return "Good bye!"
