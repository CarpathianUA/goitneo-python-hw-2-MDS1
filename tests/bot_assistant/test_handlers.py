import modules.bot_assistant.handlers.contact_handlers as contact_handlers


def test_add_contact():
    contacts = {}
    result = contact_handlers.add_contact(("John", "1111111111"), contacts)
    assert result == "Contact John added."

    result = contact_handlers.add_contact(("John", "2222222222"), contacts)
    assert result == "Contact John already exists."

    print("test: add contact: passed! [Module: {}]".format(contact_handlers.__name__))


def test_change_contact():
    contacts = {"John": "555-1234"}
    result = contact_handlers.change_contact(("John", "1111111111"), contacts)
    assert result == "Contact John changed."

    result = contact_handlers.change_contact(("Alice", "2222222222"), contacts)
    assert result == "Contact Alice doesn't exist."

    print("test: change contact: passed! [Module: {}]".format(contact_handlers.__name__))


def test_get_contact_phone():
    contacts = {"John": "1111111111", "Alice": "2222222222"}
    result = contact_handlers.get_contact_phone(("John",), contacts)
    assert result == "Phone: 1111111111"

    result = contact_handlers.get_contact_phone(("Bob",), contacts)
    assert result == "Contact doesn't exist."

    print("test: get contact phone: passed! [Module: {}]".format(contact_handlers.__name__))


def test_get_all_contacts():
    contacts = {"John": "1111111111", "Alice": "2222222222"}
    result = contact_handlers.get_all_contacts(contacts)
    assert result == "John - 1111111111\nAlice - 2222222222\n"

    # Test when there are no contacts
    empty_contacts = {}
    result = contact_handlers.get_all_contacts(empty_contacts)
    assert result == "You don't have any contacts."

    print("test: get all contacts: passed! [Module: {}]".format(contact_handlers.__name__))
