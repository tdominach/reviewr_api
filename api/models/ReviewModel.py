from django.db import models


class Review(models.Model):
    user = models.OneToOneField('User', models.DO_NOTHING, primary_key=True)
    review_id = models.CharField(max_length=22)
    #yelp api thing. Talk with Josh about this. Grabbing restaurant IDs?
    upvote = models.IntegerField()
    downvote = models.IntegerField()
    vote_date = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'reviews'
        unique_together = (('user', 'review_id'),)
        app_label = "api"
