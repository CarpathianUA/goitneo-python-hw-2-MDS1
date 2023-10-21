from tests.bot_assistant.test_handlers import test_add_contact, test_change_contact, test_get_contact_phone, \
    test_get_all_contacts

if __name__ == "__main__":
    test_add_contact()
    test_change_contact()
    test_get_contact_phone()
    test_get_all_contacts()

    print("All tests passed!")
