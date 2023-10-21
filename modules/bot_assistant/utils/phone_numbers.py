import re


def validate_e164(phone):
    """
    Validate phone number in E.164 format.
    :param phone:
    """
    pattern = re.compile(r"^\+?[1-9](-?\d){2,14}$")
    return bool(pattern.match(phone))


def is_valid_phone(phone):
    """
    Check if phone number is valid.
    :param phone:
    """
    if validate_e164(phone):
        return phone
    else:
        raise ValueError
