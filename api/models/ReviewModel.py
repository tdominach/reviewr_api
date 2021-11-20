from django.db import models
from .UserModel import User


class Review(models.Model):
    yelp_review_id = models.CharField(max_length=255, unique=True, default=0)
    users_upvoted = models.ManyToManyField(User, verbose_name="users_upvoted", null=True, related_name='users_upvoted', blank=True)
    users_downvoted = models.ManyToManyField(User, verbose_name="users_downvoted",null=True, related_name='users_downvoted', blank=True)
    upvote = models.IntegerField(verbose_name="upvotes", default=0)
    downvote = models.IntegerField(verbose_name="downvotes", default=0)

    def __str__(self):
        return "[yelp_review_id:     " + str(self.yelp_review_id) \
               + "[" + str(self.upvote) + " / " + str(self.downvote) + "]"

    class Meta:
        managed = True
        db_table = 'reviews'
        app_label = "api"

    def get_upvotes(self):
        return self.upvote

    def get_downvotes(self):
        return self.downvote

    def upvote_review(self, user_id):
        if self.has_user_downvoted(user_id):
            self.remove_downvote(user_id)

        if self.has_user_upvoted(user_id):
            self.remove_upvote(user_id)
        else:
            self.add_upvote(user_id)

    def downvote_review(self, user_id):
        if self.has_user_upvoted(user_id):
            self.remove_upvote(user_id)

        if self.has_user_downvoted(user_id):
            self.remove_downvote(user_id)
        else:
            self.add_downvote(user_id)
            
    def add_upvote(self, user_id):
        user = User.objects.get(id=user_id)
        user.add_reputation()
        user.save()
        self.users_upvoted.add(user)
        self.upvote += 1
    
    def remove_upvote(self, user_id):
        user = User.objects.get(id=user_id)
        user.remove_reputation()
        user.save()
        self.users_upvoted.remove(user)
        self.upvote -= 1
        
    def add_downvote(self, user_id):
        user = User.objects.get(id=user_id)
        user.add_reputation()
        user.save()
        self.users_downvoted.add(user)
        self.downvote += 1

    def remove_downvote(self, user_id):
        user = User.objects.get(id=user_id)
        user.remove_reputation()
        user.save()
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

