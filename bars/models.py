from django.db import models

# Create your models here.

RATINGS = (
    ('5', 'Excellent'),
    ('3', 'Okay'),
    ('1', 'Terrible'),
)


class Drink(models.Model):
    name = models.CharField(max_length=300)
    abv = models.CharField(max_length=10)

    def __unicode__(self):
        return self.name


class Bar(models.Model):
    name = models.CharField(max_length=250, blank=True)
    rating = models.CharField(max_length=25, choices=RATINGS, blank=False)
    drinks = models.ManyToManyField(Drink, blank=True, null=True)

    def __unicode__(self):
        return self.name