from django.db import models

class Business(models.Model):
    business_id = models.CharField(max_length=200)
