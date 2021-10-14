from django.db import models


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