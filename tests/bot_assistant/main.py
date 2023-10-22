import tests.bot_assistant.test_handlers as test_handlers

if __name__ == "__main__":
    test_handlers.test_add_contact()
    test_handlers.test_change_contact()
    test_handlers.test_get_contact_phone()
    test_handlers.test_get_all_contacts()

    print("All tests passed!")
