from constants import (
    YES_CHOICE,
    NO_CHOICE,
    YES_NO_CHOICE,
    ABORTED,
    INVALID_COMMAND,
    EMPTY_PHONEBOOK,
)


def input_error(default_response=INVALID_COMMAND):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except ValueError:
                return "Please provide two arguments: name and phone"
            except IndexError:
                return "Please provide contact's name"
            except KeyError:
                return "Please provide the right key"
            except:
                return default_response

        return wrapper

    return decorator


@input_error()
def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        user_input = input(
            f"Contact {name} already exists. Would you like to update it?{YES_NO_CHOICE}"
        )
        user_input = user_input.strip().lower()

        if user_input == YES_CHOICE:
            contacts[name] = phone
            return f"Contact {name} was updated."
        elif user_input == NO_CHOICE:
            return ABORTED
        else:
            return INVALID_COMMAND
    else:
        contacts[name] = phone
        return f"Contact {name} was added."


@input_error()
def change_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        user_input = input(
            f"There is no contact with the name {name}. Would you like to add?{YES_NO_CHOICE}"
        )
        user_input = user_input.strip().lower()

        if user_input == YES_CHOICE:
            contacts[name] = phone
            return f"Contact {name} was added."
        elif user_input == NO_CHOICE:
            return ABORTED
        else:
            return INVALID_COMMAND
    else:
        contacts[name] = phone
        return f"Contact {name} was updated."


@input_error()
def delete_contact(args, contacts):
    name = args[0]
    user_input = input(
        f"Do you really want to delete {name} from contacts?{YES_NO_CHOICE}"
    )
    user_input = user_input.strip().lower()

    if user_input == YES_CHOICE:
        if name in contacts:
            contacts.pop(name)
            return f"Contact {name} was deleted."
        else:
            return f"Contact with the name {name} doesn't exists in contacts"

    elif user_input == NO_CHOICE:
        return ABORTED
    else:
        return INVALID_COMMAND


@input_error()
def show_phone_number(args, contacts):
    name = args[0]
    if name in contacts:
        return f"{name}'s phone number is {contacts[name]}"
    else:
        return f"Contact with the name {name} was not found"


def show_all_contacts(*args, contacts):
    if not len(contacts):
        return EMPTY_PHONEBOOK
    contacts_list = list()
    for name, phone in contacts.items():
        contacts_list.append("{:<10}:  {}".format(name, phone))
    contacts_string = "\n".join(contacts_list)
    return f"{'*'*15}\n{contacts_string}\n{'*'*15}"
