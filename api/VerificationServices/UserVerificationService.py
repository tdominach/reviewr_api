import re
#from reviewr_api.api.Models.UserModel import users


def verifyUsername(username):
    if len(username) > 5:# and users.objects.get(name=username).exists():
        return True
    else:
        return False


def verifyEmail(email):
    email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")
    if email_regex.match(email):# and users.objects.get(email=email).exists():
        return True
    else:
        return False


def verifyPassword(password):
    if len(password) > 6 and any(char.isdigit() for char in password):
        return True
    else:
        return False

