from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg

# Create your models here.
class Rating(models.Model):
    class Rate(models.IntegerChoices):
        ONE_STAR = 1
        TWO_STAR = 2
        THREE_STAR = 3
        FOUR_STAR = 4
        FIVE_STAR = 5

    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    date = models.DateTimeField(auto_now_add=True)
    rate = models.IntegerField(choices=Rate.choices)

class Subject(models.Model):
    class Meta:
        ordering = ['-date']
    
    name = models.CharField(max_length=30)
    text = models.TextField(blank=False)
    date = models.DateTimeField(auto_now_add=True)
    rating = models.ManyToManyField(Rating, null=True, blank=True)

    def get_rating(self):
        return self.rating.all().aggregate(Avg('rate')).get('rate__avg', 1)