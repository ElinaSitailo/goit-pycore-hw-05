import re


def phone_error_decorator(func):
    def normalize_phone_wrapper(inphone: str) -> str:
        try:
            result = func(inphone)
            if not result:
                print(
                    f"Invalid phone number format. Valid phone is at least 9 symbols."
                )
            return result
        except Exception as e:
            print(f"Error normalizing phone number '{inphone}': {e}")
            return EMPTY_PHONE

    return normalize_phone_wrapper


# The method normalizes phone strings by removing non-numbers and addind leading ''+'' if needed.
# If phone number starts with 0 - replace it with +380
# If phone number starts with 3 - add leading +
# If phone number starts with 8 - replace it with +38
#
# Output phone format: +380952345678
EMPTY_PHONE = ""


@phone_error_decorator
def normalize_phone(inphone: str) -> str:

    phone = re.sub(r"\D", "", inphone)  # Remove all non-digit characters
    if len(phone) < 9:  # Assuming a valid phone number has at least 9 digits
        return EMPTY_PHONE

    if phone.startswith("0"):
        phone = "38" + phone
    elif phone.startswith("8"):
        phone = "3" + phone

    phone = "+" + phone

    return phone


# TESTS:
assert normalize_phone("099 555-1234") == "+380995551234"
assert normalize_phone("+380995551234") == "+380995551234"
assert normalize_phone("80995551234") == "+380995551234"
assert normalize_phone("380995551234") == "+380995551234"
assert normalize_phone("995551234") == "+995551234"
assert normalize_phone("12345") == EMPTY_PHONE
