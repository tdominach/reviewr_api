import re


def verifyUsername(username):
    if len(username) > 5:
        return True
    else:
        return False


def verifyEmail(email):
    email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")
    if email_regex.match(email):
        return True
    else:
        return False


def verifyPassword(password):
    if len(password) > 6 and any(char.isdigit() for char in password):
        return True
    else:
        return False
