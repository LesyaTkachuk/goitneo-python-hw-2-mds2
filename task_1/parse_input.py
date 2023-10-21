from constants import INVALID_COMMAND
from general_handlers import (
    greet_user,
    show_command_list,
    close_assistant,
    show_unknown_command,
)
from contact_handlers import (
    add_contact,
    change_contact,
    delete_contact,
    show_all_contacts,
    show_phone_number,
)

USER_COMMANDS = {
    "hello": greet_user,
    "help": show_command_list,
    "all": show_all_contacts,
    "add": add_contact,
    "change": change_contact,
    "phone": show_phone_number,
    "delete": delete_contact,
    "close": close_assistant,
    "exit": close_assistant,
}


def parse_input(user_input):
    try:
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        if cmd in USER_COMMANDS:
            return USER_COMMANDS[cmd], args
        else:
            return show_unknown_command, []
    # to handle empty user input
    except ValueError:
        return show_unknown_command, []
