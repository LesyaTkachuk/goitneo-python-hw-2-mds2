import re
from collections import UserDict


class PhoneValidationError(Exception):
    pass


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, name):
        super().__init__(name)


class Phone(Field):
    def __init__(self, phone):
        try:
            # acceptable formats 1111111111, (111)-111-1-111, 111 111 1 111, 111-111-11-11, (111)111-11-11, (111)111 11 11
            valid_phone_number = re.search(
                r"(^[(]?[\d]{3}[)\-\s]?[\d]{3}[-\s]?[\d]{2}[-\s]?[\d]{2}$)|(^[(]?[\d]{3}[)\-\s]?[\d]{3}[-\s]?[\d]{1}[-\s]?[\d]{3}$)",
                phone,
            )
            if not valid_phone_number:
                phone = None
                raise PhoneValidationError
        except PhoneValidationError:
            print("Phone number should consists of 10 digits in international format")

        super().__init__(phone)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join([p.value for p in self.phones])}"

    def add_phone(self, phone):
        phone_number = Phone(phone)
        if phone_number.value:
            self.phones.append(phone_number)

    def find_phone(self, phone_number):
        for phone in self.phones:
            if str(phone) == phone_number:
                return phone
        print(
            f"There is no phone number {phone_number} in the {self.name}'s phone list"
        )
        return None

    def edit_phone(self, phone_to_change, new_phone):
        new_phone_number = Phone(new_phone)
        phone = self.find_phone(phone_to_change)
        if phone and new_phone_number.value:
            self.phones = [
                number
                for number in map(
                    lambda i: new_phone_number if str(i) == phone_to_change else i,
                    self.phones,
                )
            ]

    def remove_phone(self, phone_number):
        phone = self.find_phone(phone_number)
        if phone:
            self.phones.remove(phone)


class AddressBook(UserDict):
    def __str__(self):
        records_string = "\n".join([str(r) for r in self.data.values()])
        return f"{records_string}"

    def add_record(self, record):
        self[str(record.name)] = record

    def find(self, name):
        if name in self.data:
            return self.data[name]
        else:
            print(f"No contact with the name {name}")
            return None

    def delete(self, name):
        record = self.find(name)
        if record:
            self.data.pop(name)
