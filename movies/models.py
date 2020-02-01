"""Movies app models"""

from django.db import models


class Director(models.Model):
    """Director model"""
    name = models.CharField(max_length=70)
    birthday = models.DateField()
    nacionality = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Movie(models.Model):
    """Movie model"""
    title = models.CharField(max_length=50)
    year = models.PositiveSmallIntegerField()
    sinopsis = models.TextField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} - {self.director.name} ({self.year})'

