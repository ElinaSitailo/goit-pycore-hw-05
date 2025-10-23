from normalize_phone import normalize_phone
CONTACT_NOT_FOUND_MSG = "Contact not found."
UNKNOWN_COMMAND_MSG = "Unknown command. Please try again."

EXPECT_AT_LEAST_2_ARGS_MSG = "Insufficient arguments. Expected at least 2 arguments."
def at_least_2_args_decorator(func):
    def action(args, contacts) -> str:
        if len(args) < 2:
            return EXPECT_AT_LEAST_2_ARGS_MSG
        else:
            return func(args, contacts)

    return action
EXPECT_AT_LEAST_1_ARGS_MSG = "Insufficient arguments. Expected at least 1 arguments."
def at_least_1_args_decorator(func):
    def action(args, contacts) -> str:
        if len(args) < 1:
            return EXPECT_AT_LEAST_1_ARGS_MSG
        else:
            return func(args, contacts)

    return action

def parse_input(user_input):
    if len(user_input.strip()) == 0:
        return ("",)
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@at_least_2_args_decorator
def add_contact(args, contacts) -> str:
    name, phone = args
    normalized_phone = normalize_phone(phone)
    if normalized_phone:
        contacts[name] = normalized_phone
        return "Contact added."
    else:
        return "Unable to add contact."


@at_least_2_args_decorator
def update_contact(args, contacts) -> str:
    name, phone = args
    normalized_phone = normalize_phone(phone)
    if normalized_phone:
        if name in contacts:
            contacts[name] = phone
            return "Contact updated."
        else:
            return CONTACT_NOT_FOUND_MSG

@at_least_1_args_decorator
def show_contact(args, contacts) -> str:
    name = args[0]
    if name in contacts:
        return f"{name}: {contacts[name]}"
    else:
        return CONTACT_NOT_FOUND_MSG


def show_all_contacts(contacts) -> str:
    if contacts:
        return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
    else:
        return "No contacts found."


def get_output_by_command(command, args, contacts):
    is_exit = False
    if command == "hello":
        output = "How can I help you?"
    elif command == "add":
        output = add_contact(args, contacts)
    elif command == "change":
        output = update_contact(args, contacts)
    elif command == "phone":
        output = show_contact(args, contacts)
    elif command == "all":
        output = show_all_contacts(contacts)
    elif command == "help" or command == "?":
        output = (
            "Available commands:\n"
            "hello - Greet the bot\n"
            "add <name> <phone> - Add a new contact. Expected phone lenght is at least 9 digits.\n"
            "change <name> <phone> - Change an existing contact's phone number. Expected phone lenght is at least 9 digits.\n"
            "phone <name> - Show the phone number of a contact\n"
            "all - Show all contacts\n"
            "exit, close, goodbye - Exit the program"
        )
    elif command in ("exit", "close", "goodbye"):
        output = "Goodbye!"
        is_exit = True
    else:
        output = UNKNOWN_COMMAND_MSG

    return output, is_exit


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        output, is_exit = get_output_by_command(command, args, contacts)
        print(output)
        if is_exit:
            break


if __name__ == "__main__":
    main()


TEST_NAME = "Vasya"
PHONE1 = "099 555-1234"
PHONE2 = "099 555-5678"
assert parse_input("  AdD  John  12345 ") == ("add", "John", "12345")
assert parse_input("EXIT") == ("exit",)
assert parse_input("") == ("",)
assert parse_input("  ") == ("",)
assert get_output_by_command("hello", [], {}) == ("How can I help you?", False)
assert get_output_by_command("add", [TEST_NAME, PHONE1], {}) == (
    "Contact added.",
    False,
)
assert get_output_by_command("phone", [TEST_NAME], {TEST_NAME: PHONE1}) == (
    f"{TEST_NAME}: {PHONE1}",
    False,
)
assert get_output_by_command("change", [TEST_NAME, PHONE2], {TEST_NAME: PHONE1}) == (
    "Contact updated.",
    False,
)
assert get_output_by_command("all", [], {TEST_NAME: PHONE2}) == (
    f"{TEST_NAME}: {PHONE2}",
    False,
)
assert get_output_by_command("exit", [], {}) == ("Goodbye!", True)
assert get_output_by_command("unknown", [], {}) == (
    UNKNOWN_COMMAND_MSG,
    False,
)
assert get_output_by_command("phone", ["NonExistent"], {}) == (
    CONTACT_NOT_FOUND_MSG,
    False,
)
assert get_output_by_command("change", ["NonExistent", PHONE1], {}) == (
    CONTACT_NOT_FOUND_MSG,
    False,
)
assert get_output_by_command("add", [TEST_NAME], {}) == (
    EXPECT_AT_LEAST_2_ARGS_MSG,
    False,
)
assert get_output_by_command("change", [TEST_NAME], {}) == (
    EXPECT_AT_LEAST_2_ARGS_MSG,
    False,
)
assert get_output_by_command("phone", [], {}) == (
    EXPECT_AT_LEAST_1_ARGS_MSG,
    False,
)
assert get_output_by_command("all", [], {}) == ("No contacts found.", False)
assert get_output_by_command("", [], {}) == (
    UNKNOWN_COMMAND_MSG,
    False,
)
assert get_output_by_command("add", [], {}) == (
    EXPECT_AT_LEAST_2_ARGS_MSG,
    False,
)
assert get_output_by_command("change", [], {}) == (
    EXPECT_AT_LEAST_2_ARGS_MSG,
    False,
)


# Приклад використання функції:
# Запустіть скрипт і введіть команди "hello" та "exit"  для перевірки роботи бота.
# python task4_bot.py
