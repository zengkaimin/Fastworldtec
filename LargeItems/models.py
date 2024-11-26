from django.db import models  # Import the models module from django.db


# Large item object
class LargeItems(models.Model):
    objects = None  # Add to prevent unresolved attribute reference error in views.py in PYCHARM.

    # Image field to upload tool images, storing them in 'all_tool_images' directory
    image = models.ImageField(upload_to='all_large_items_images')

    # CharField for the large item title with a maximum length of 255 characters
    title = models.CharField(max_length=255)

    # CharField for the large item price with a maximum length of 50 characters, can be blank
    price = models.CharField(max_length=50, blank=True)

    # TextField for the large item description, can be blank
    description = models.TextField(blank=True)

    # CharField for the affiliate link with a maximum length of 2083 characters
    affiliate_link = models.CharField(max_length=2083)

    # DateTimeField to store the date and time when the large item was created, automatically set on creation
    date_and_time_created = models.DateTimeField(auto_now_add=True)

    # Metaclass to define metadata for the model
    class Meta:
        # Order tools by date and time created in descending order
        ordering = ('-date_and_time_created',)

        # Change the plural name of the model in the admin portal
        verbose_name_plural = 'All Large Items'

    # Function to return the large item title in admin portal
    def __str__(self):
        return self.title
