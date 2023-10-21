from modules.bot_assistant.constants.exit_commands import EXIT_COMMANDS
from modules.bot_assistant.handlers.parsers import parse_input
from modules.bot_assistant.handlers.handlers import add_contact, change_contact, get_contact_phone, get_all_contacts


def main():
    contacts = dict()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in EXIT_COMMANDS:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(get_contact_phone(args, contacts))
        elif command == "all" and not args:
            print(get_all_contacts(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
