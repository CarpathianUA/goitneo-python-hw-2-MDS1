from collections import UserDict
from modules.bot_assistant.utils.phone_numbers import is_valid_phone


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    # we don't need to override __init__ method here from super class
    # since Name class doesn't have any additional attributes, just a 'value' from Field class
    pass


class Phone(Field):
    def __init__(self, value):
        if not self.__validate_phone(value):
            raise ValueError("Invalid phone number")
        super().__init__(value)

    @staticmethod
    def __validate_phone(phone):
        return is_valid_phone(phone)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = list()

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def edit_phone(self, phone, new_phone):
        for p in self.phones:
            if p.value == phone:
                p.value = new_phone

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def __is_key_exist(self, key):
        return key in self.data

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        if not self.__is_key_exist(name):
            raise ValueError(f"Contact '{name}' doesn't exist.")
        return self.data[name]

    def delete(self, name):
        if not self.__is_key_exist(name):
            raise ValueError(f"Contact '{name}' doesn't exist.")
        self.data.pop(name, None)
        return f"Contact '{name}' has been deleted."

    def __str__(self):
        return '\n'.join(str(record) for record in self.data.values())
