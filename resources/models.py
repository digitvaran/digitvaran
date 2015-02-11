from django.db import models

class Audiobook(models.Model):
    """
    A link refering to resource material.
    """
    def __str__(self):
        return self.name
    name=models.CharField(max_length=100)
    description=models.TextField()
    link=models.CharField(max_length=300)
    tags=models.ManyToManyField('Tag')
class Tag(models.Model):
    "A tag for resources. Used in searches"
    def __str__(self):
        return self.name
    name=models.CharField(max_length=100)
