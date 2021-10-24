from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class User(AbstractUser):
    username = models.CharField(verbose_name="username", max_length=50, unique=True)
    email = models.EmailField('email address', unique=True)
    password = models.CharField(db_column='password', max_length=255)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="lost login", auto_now=True)
    reputation = models.IntegerField(verbose_name="reputation", default=0)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

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

    def add_reputation(self):
        self.reputation += 1

    def remove_reputation(self):
        self.reputation -= 1


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
