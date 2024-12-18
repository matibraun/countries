from django.db import models
from django.contrib.postgres.fields import ArrayField

class Country(models.Model):

    name = models.CharField(max_length=200, unique=True)
    official_name = models.CharField(max_length=250)
    common_name = models.CharField(max_length=250)
    official_native_name = models.CharField(max_length=250)
    common_native_name = models.CharField(max_length=250)
    
    flag_png = models.URLField(max_length=500, blank=True, null=True)
    flag_svg = models.URLField(max_length=500, blank=True, null=True)
    flag_alt = models.CharField(max_length=2600, blank=True, null=True)
    
    capital = models.CharField(max_length=200, blank=True, null=True)
    population = models.IntegerField()
    area = models.FloatField()

    latitude = models.FloatField()
    longitude = models.FloatField()
    
    continents = ArrayField(
        models.CharField(max_length=100),
        blank=True,
        null=True
    )
    
    timezones = ArrayField(
        models.CharField(max_length=50),
        blank=True,
        null=True
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Countries"
        ordering = ['name']