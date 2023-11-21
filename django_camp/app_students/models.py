from django.db import models

# Create your models here.
class FavoriteSub(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self) -> str:
        return self.name

class Division(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self) -> str:
        return self.name

class StudentInfo(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=60, unique=True)
    psu_id = models.CharField(max_length=11, unique=True)
    division_set = models.ForeignKey(Division, on_delete=models.SET_NULL ,null=True)
    favorite_subject = models.ManyToManyField('FavoriteSub')
    date = models.DateTimeField(auto_now_add=True)

