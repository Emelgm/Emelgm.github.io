from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='project/images/')

    def __str__(self) -> str:
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='project/images/')
    id_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
