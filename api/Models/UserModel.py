from django.db import models

#TODO Make this so that we have a count of how many reviews the user has interacted with?

class users(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=256)
    password = models.CharField(db_column='pass', max_length=256)

    class Meta:
        managed = False
        db_table = 'users'