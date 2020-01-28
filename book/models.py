from django.db import models


# DataFlair Models
class Book(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField()
    author = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    describe = models.TextField()

    def __str__(self):
        return self.name