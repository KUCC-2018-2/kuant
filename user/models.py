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


class Scrap(models.Model):
    scrap_id = models.IntegerField()
    created_at = models.DateTimeField()
    content = models.ForeignKey('posting.Content', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Write(models.Model):
    write_id = models.IntegerField(primary_key=True)
    created_at = models.DateTimeField()
    content = models.ForeignKey('posting.Content', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Message(models.Model):
    message_id = models.IntegerField(primary_key=True)
    message_title = models.CharField(max_length=32)
    message_text = models.CharField(max_length=1000)
    send_date = models.DateTimeField()
    with_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="friend")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="self")


class Comment(models.Model):
    comment_id = models.IntegerField()
    registerd_at = models.DateTimeField()
    message = models.CharField(max_length=2000)
    is_recreated = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)