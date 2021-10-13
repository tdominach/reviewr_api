from django.contrib.auth.hashers import make_password
from django.db import models

# Create your models here.

"""
class users(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    password = models.CharField(max_length=256)

    def _str_(self):
        return {self.id, self.username, self.email, self.password}
"""


class reviews(models.Model):
    user = models.OneToOneField('Users', models.DO_NOTHING, primary_key=True)
    review_id = models.CharField(max_length=22)
    upvote = models.IntegerField()
    downvote = models.IntegerField()
    vote_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'reviews'
        unique_together = (('user', 'review_id'),)


class users(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=256)
    # Field renamed because it was a Python reserved word.
    pass_field = models.CharField(db_column='pass', max_length=256)

    class Meta:
        managed = False
        db_table = 'users'
