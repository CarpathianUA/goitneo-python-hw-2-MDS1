import modules.bot_assistant.models.address_book as ab


def test_add_contact():
    book = ab.AddressBook()
    book.add_record(ab.Record("John"))
    assert book.find("John") is not None

    print("test: add contact: passed! [Module: {}]".format(ab.__name__))


def test_change_contact():
    book = ab.AddressBook()
    book.add_record(ab.Record("John"))
    book.find("John").add_phone("1111111111")
    book.find("John").add_phone("2222222222")

    book.find("John").edit_phone("1111111111", "3333333333")
    assert book.find("John").find_phone("3333333333") is not None

    print("test: change contact: passed! [Module: {}]".format(ab.__name__))


def test_get_contact_phone():
    book = ab.AddressBook()
    book.add_record(ab.Record("John"))
    book.find("John").add_phone("1111111111")
    book.find("John").add_phone("2222222222")

    assert book.find("John").find_phone("1111111111") is not None

    print("test: get contact phone: passed! [Module: {}]".format(ab.__name__))


def test_delete_contact():
    book = ab.AddressBook()
    book.add_record(ab.Record("John"))
    book.find("John").add_phone("1111111111")
    book.find("John").add_phone("2222222222")

    book.delete("John")
    assert book.data == {}

    print("test: delete contact: passed! [Module: {}]".format(ab.__name__))


def test_get_all_contacts():
    book = ab.AddressBook()
    book.add_record(ab.Record("John"))
    book.find("John").add_phone("1111111111")
    book.find("John").add_phone("2222222222")

    book.add_record(ab.Record("Jane"))
    book.find("Jane").add_phone("3333333333")

    assert len(book.data) == 2

    result = [(str(name), str(record)) for name, record in book.data.items()]
    assert result == [('John', 'Contact name: John, phones: 1111111111; 2222222222'),
                      ('Jane', 'Contact name: Jane, phones: 3333333333')]

    print("test: get all contacts: passed! [Module: {}]".format(ab.__name__))
