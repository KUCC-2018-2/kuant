from django.db import models


class User(models.Model):
    user_id = models.CharField(max_length=25, primary_key=True)
    password = models.CharField(max_length=32)
    email = models.CharField(max_length=255)
    create_at = models.DateTimeField()
    update_at = models.DateTimeField()
    profile_image = models.CharField(max_length=255)
    user_name = models.CharField(max_length=45)
    phone_num = models.CharField(max_length=45)
    is_banned = models.BooleanField()
    detail_exist = models.BooleanField()