from django.db import models

class Toiletries(models.Model):
    objects = None  # Add to prevent unresolved attribute reference error in views.py in PYCHARM.
    image = models.ImageField(upload_to='all_toiletries_images')
    title = models.CharField(max_length=255)
    price = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    affiliate_link = models.CharField(max_length=2083)
    date_and_time_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_and_time_created',)
        verbose_name_plural = 'All Toiletries'

    def __str__(self):
        return self.title 