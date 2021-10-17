from django.contrib import admin
from .Models.UserModel import users
from .Models.ReviewModel import reviews

# Register your models here.

admin.site.register(users)
admin.site.register(reviews)
