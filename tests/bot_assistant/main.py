import tests.bot_assistant.test_handlers as test_handlers
import tests.bot_assistant.test_address_book as test_address_book

if __name__ == "__main__":
    # test command handlers
    test_handlers.test_add_contact()
    test_handlers.test_change_contact()
    test_handlers.test_get_contact_phone()
    test_handlers.test_get_all_contacts()

    # test address book model
    test_address_book.test_add_contact()
    test_address_book.test_change_contact()
    test_address_book.test_get_contact_phone()
    test_address_book.test_delete_contact()
    test_address_book.test_get_all_contacts()

    print("All tests passed!")
