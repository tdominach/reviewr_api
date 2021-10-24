from django.db import models
from .UserModel import User


class Review(models.Model):
    yelp_review_id = models.CharField(max_length=255, unique=True)
    users_upvoted = models.ManyToManyField(User, null=True, related_name='users_upvoted', blank=True)
    users_downvoted = models.ManyToManyField(User, null=True, related_name='users_downvoted', blank=True)
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)

    def __str__(self):
        return "[yelp_review_id:     " + str(self.yelp_review_id) + "[" + str(self.upvote) + "/" + str(self.downvote) + "]"

    class Meta:
        managed = True
        db_table = 'reviews'
        app_label = "api"

    def upvote_review(self, user_id):
        user = User.objects.get(id=user_id)
        if self.has_user_downvoted(user_id):
            self.remove_downvote(user)
        if self.has_user_upvoted(user_id):
            self.remove_upvote(user)
        else:
            self.add_upvote(user)

    def downvote_review(self, user_id):
        user = User.objects.get(id=user_id)
        if self.has_user_upvoted(user_id):
            self.remove_upvote(user)
        if self.has_user_downvoted(user_id):
            self.remove_downvote(user)
        else:
            self.add_downvote(user)
            
    def add_upvote(self, user):
        self.users_upvoted.add(user)
        self.upvote += 1
    
    def remove_upvote(self, user):
        self.users_upvoted.remove(user)
        self.upvote -= 1
        
    def add_downvote(self, user):
        self.users_downvoted.add(user)
        self.downvote += 1

    def remove_downvote(self, user):
        self.users_downvoted.remove(user)
        self.downvote -= 1
        
    def has_user_upvoted(self, user_id):
        try:
            has_upvoted = self.users_upvoted.get(id=user_id)
            return True
        except User.DoesNotExist:
            return False

    def has_user_downvoted(self, user_id):
        try:
            has_downvoted = self.users_downvoted.get(id=user_id)
            return True
        except User.DoesNotExist:
            return False

