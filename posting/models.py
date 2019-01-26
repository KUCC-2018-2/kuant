from django.db import models


class WorkPlace(models.Model):
    workplace_name = models.CharField(max_length=30, null=False)
    level = models.IntegerField(default=0)
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE)


class WorkType(models.Model):
    worktype_name = models.CharField(max_length=30, null=False)
    level = models.IntegerField(default=0)
    parend_id = models.ForeignKey('self', on_delete=models.CASCADE)


class Content(models.Model):
    how_used = models.BooleanField(default=0)
    title = models.CharField(max_length=200, null=False)
    text = models.TextField
    create_at = models.DateTimeField(auto_now=True, null=False)
    due_date = models.DateTimeField(null=False)
    work_startdate = models.DateTimeField
    work_enddate = models.DateTimeField
    pay = models.IntegerField(default=0)
    experience = models.CharField(max_length=1000)
    workplace = models.ForeignKey(WorkPlace, on_delete=models.CASCADE)
    worktype = models.ForeignKey(WorkType, on_delete=models.CASCADE)
    image = models.CharField(max_length=1000)