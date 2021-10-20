from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class User(models.Model):
    username = models.CharField(verbose_name="username", max_length=50, unique=True)
    email = models.CharField(verbose_name="email", max_length=255, unique=True)
    password = models.CharField(db_column='password', max_length=255)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="lost login", auto_now=True)

    def __str__(self):
        return "[Username:      " + self.username + "] [Email:     " + self.email + "]"

    class Meta:
        managed = True
        db_table = 'users'
        app_label = "api"

    def set_username(self, username):
        self.username = username

    def set_password(self, password):
        self.password = password

    def set_email(self, email):
        self.email = email
