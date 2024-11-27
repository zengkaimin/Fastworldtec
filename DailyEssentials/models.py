from django.db import models  # Import the models module from django.db


# DailyEssentials object
class DailyEssentials(models.Model):
    objects = None  # Add to prevent unresolved attribute reference error in views.py in PYCHARM.

    # Image field to upload daily essentials images, storing them in 'all_daily_essentials_images' directory
    image = models.ImageField(upload_to='all_daily_essentials_images')

    # CharField for the daily essentials title with a maximum length of 255 characters
    title = models.CharField(max_length=255)

    # CharField for the daily essentials price with a maximum length of 50 characters, can be blank
    price = models.CharField(max_length=50, blank=True)

    # TextField for the daily essentials description, can be blank
    description = models.TextField(blank=True)

    # CharField for the affiliate link with a maximum length of 2083 characters
    affiliate_link = models.CharField(max_length=2083)

    # Whether this item is featured (是否精选商品)
    is_featured = models.BooleanField(
        default=False, 
        verbose_name='Featured Item (精选商品)'
    )

    # DateTimeField to store the date and time when the daily essentials was created, automatically set on creation
    date_and_time_created = models.DateTimeField(auto_now_add=True)

    # Metaclass to define metadata for the model
    class Meta:
        # Order daily essentials by date and time created in descending order
        ordering = ('-date_and_time_created', )

        # Change the plural name of the model in the admin portal
        verbose_name_plural = 'All Daily Essentials'

    # Function to return the daily essentials title in admin portal
    def __str__(self):
        return self.title
