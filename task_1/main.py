from parse_input import parse_input
from general_handlers import read_contacts, show_command_list, close_assistant


def main():
    contacts = read_contacts()
    if not contacts:
        print(show_command_list())

    while True:
        user_input = input("---> Enter a command: >>> ")
        handler, args = parse_input(user_input)

        print(handler(args, contacts=contacts))

        if handler == close_assistant:
            break


if __name__ == "__main__":
    main()
