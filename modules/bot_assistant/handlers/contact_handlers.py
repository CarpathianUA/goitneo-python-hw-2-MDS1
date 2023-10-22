from modules.bot_assistant.decorators.decorators import input_error
from modules.bot_assistant.utils.phone_numbers import is_valid_phone


@input_error
def add_contact(args, contacts):
    """
    Add contact to contacts.
    :param args:
    :param contacts:
    """
    name, phone = args
    if name not in contacts:
        contacts[name] = is_valid_phone(phone)
    else:
        return f"Contact {name} already exists."
    return f"Contact {name} added."


@input_error
def change_contact(args, contacts):
    """
    Change contact in contacts.
    :param args:
    :param contacts:
    """
    name, phone = args
    if name in contacts:
        contacts[name] = is_valid_phone(phone)
    else:
        return f"Contact {name} doesn't exist."
    return f"Contact {name} changed."


@input_error
def get_contact_phone(args, contacts):
    """
    Get contact phone from contacts.
    :param args:
    :param contacts:
    """
    name = args[0]
    return f"Phone: {contacts[name]}"


# we don't need to decorate this function
# if contacts dict is empty, we return message about empty contacts
def get_all_contacts(contacts):
    """
    Get all contacts from contacts.
    :param contacts:
    """
    if not contacts:
        return "You don't have any contacts."
    return "".join([f"{name} - {phone}\n" for name, phone in contacts.items()])
