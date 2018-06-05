from django.db import models

class User(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=250)

    score=models.IntegerField()
    image=models.ImageField(default='default.png',blank=True)
    def __str__(self):
        return self.name
