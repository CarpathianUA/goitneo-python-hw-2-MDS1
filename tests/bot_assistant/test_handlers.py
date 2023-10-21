from modules.bot_assistant.handlers.handlers import add_contact, change_contact, get_contact_phone, get_all_contacts


def test_add_contact():
    contacts = {}
    result = add_contact(("John", "555-1234"), contacts)
    assert result == "Contact John added."

    result = add_contact(("John", "555-5678"), contacts)
    assert result == "Contact John already exists."

    print("test: add contact: passed!")


def test_change_contact():
    contacts = {"John": "555-1234"}
    result = change_contact(("John", "555-5678"), contacts)
    assert result == "Contact John changed."

    result = change_contact(("Alice", "555-9876"), contacts)
    assert result == "Contact Alice doesn't exist."

    print("test: change contact: passed!")


def test_get_contact_phone():
    contacts = {"John": "555-1234", "Alice": "555-5678"}
    result = get_contact_phone(("John",), contacts)
    assert result == "Phone: 555-1234"

    result = get_contact_phone(("Bob",), contacts)
    assert result == "Contact doesn't exist."

    print("test: get contact phone: passed!")


def test_get_all_contacts():
    contacts = {"John": "555-1234", "Alice": "555-5678"}
    result = get_all_contacts(contacts)
    assert result == "John - 555-1234\nAlice - 555-5678\n"

    # Test when there are no contacts
    empty_contacts = {}
    result = get_all_contacts(empty_contacts)
    assert result == "You don't have any contacts."

    print("test: get all contacts: passed!")
