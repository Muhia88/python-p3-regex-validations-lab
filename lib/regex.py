import re

# Name regex:
# - Starts with uppercase letter
# - Can have letters, apostrophes, hyphens
# - Words separated by a single space only
name = r"^[A-Z][a-zA-Z]*(?:['-][A-Za-z]+)*(?: [A-Z][a-zA-Z]*(?:['-][A-Za-z]+)*)*$"
name_regex = re.compile(name)


# Phone regex:
# - Matches 10 digits, or 3-3-4 with dashes, or (nnn) nnn-nnnn
phone_number = r"^(?:\d{10}|\d{3}-\d{3}-\d{4}|\(\d{3}\) \d{3}-\d{4})$"
phone_regex = re.compile(phone_number)


# Email regex:
# - Starts with alpha
# - Followed by alphanumerics or dots
# - Single @
# - Domain with alphas only, then a dot, then alphas
email_address = r"^[A-Za-z][A-Za-z0-9]*(?:\.[A-Za-z0-9]+)*@[A-Za-z]+\.[A-Za-z]+$"
email_regex = re.compile(email_address)
