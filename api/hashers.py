from django.contrib.auth.hashers import PBKDF2PasswordHasher

# This file contains custom hashers that can be added to the PASSWORD_HASHERS list in setttings.py
# https://docs.djangoproject.com/en/3.2/topics/auth/passwords/


class MyPBKDF2PasswordHasher(PBKDF2PasswordHasher):
    """
    A subclass of PBKDF2PasswordHasher that uses 100 times more iterations.
    """
    iterations = PBKDF2PasswordHasher.iterations * 1
