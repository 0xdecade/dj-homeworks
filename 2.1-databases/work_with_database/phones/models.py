from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    name = models.CharField(max_length=64, unique=True, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    image = models.URLField(blank=True)
    release_date = models.DateField(blank=False)
    lte_exists = models.BooleanField(blank=False)
    slug = models.SlugField(max_length=200, unique=True, blank=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
