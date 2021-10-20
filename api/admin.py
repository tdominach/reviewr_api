from django.contrib import admin
from .models.UserModel import User
from .models.ReviewModel import Review

# Register your models here.

admin.site.register(User)
admin.site.register(Review)
