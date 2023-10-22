from modules.bot_assistant.constants.exit_commands import EXIT_COMMANDS
from modules.bot_assistant.handlers.input_parsers import parse_input
import modules.bot_assistant.handlers.contact_handlers as contact_handlers


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
            print(contact_handlers.add_contact(args, contacts))
        elif command == "change":
            print(contact_handlers.change_contact(args, contacts))
        elif command == "phone":
            print(contact_handlers.get_contact_phone(args, contacts))
        elif command == "all" and not args:
            print(contact_handlers.get_all_contacts(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
