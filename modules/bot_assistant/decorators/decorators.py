def input_error(func):
    """
    Decorator for input errors.
    :param func:
    """

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and correct phone number please."
        except IndexError:
            return "Give me phone and name of contact please."
        except KeyError:
            return "Contact doesn't exist."
        except NameError:
            return "Contacts dictionary doesn't exist."

    return wrapper
