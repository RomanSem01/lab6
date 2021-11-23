from django.db import models


class Animal(models.Model):
    name = models.CharField(max_length=40)
    slug = models.IntegerField()

    def __str__(self):
        return self.name


class Photo(models.Model):
    img = models.ImageField(upload_to='photos')
