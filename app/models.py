from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self) -> str:
        return self.name


class Photo(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='images', null=False, blank=False)
    topic = models.CharField(max_length=30, default='Add topic here')

    def __str__(self) -> str:
        return self.topic
