from django.db import models

# Create your models here.


class Result(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.first_name
