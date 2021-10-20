from django.db import models
from .UserModel import User


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review_id = models.CharField(max_length=22)
    upvote = models.IntegerField()
    downvote = models.IntegerField()
    vote_date = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'reviews'
        unique_together = (('user', 'review_id'),)
        app_label = "api"
