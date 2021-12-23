from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField

class Armor(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='armor/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    text = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    armor = models.ForeignKey(Armor,on_delete=models.CASCADE)
    watchAgain = models.BooleanField()

    def __str__(self):
        return self.text

class Category(models.Model):
    name = models.CharField(max_length=50)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        return self.name

