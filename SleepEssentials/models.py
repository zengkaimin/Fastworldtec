from django.db import models  # Import the models module from django.db
from mdeditor.fields import MDTextField  # Import MDTextField from mdeditor.fields


# SleepEssential object
class SleepEssentials(models.Model):
    objects = None  # Add to prevent unresolved attribute reference error in views.py in PYCHARM.

    # Image field to upload software images, storing them in 'all_software_images' directory
    image = models.ImageField(upload_to='all_sleep_essentials_images')

    # CharField for the sleep essential title with a maximum length of 255 characters
    title = models.CharField(max_length=255)

    # CharField for the sleep essential price with a maximum length of 50 characters, can be blank
    price = models.CharField(max_length=50, blank=True)

    # MDTextField for the sleep essential description, can be blank
    description = MDTextField(blank=True)

    # CharField for the affiliate link with a maximum length of 2083 characters
    affiliate_link = models.CharField(max_length=2083)

    # Whether this item is featured (是否精选商品)
    is_featured = models.BooleanField(
        default=False, 
        verbose_name='Featured Item (精选商品)'
    )

    # DateTimeField to store the date and time when the sleep essential was created, automatically set on creation
    date_and_time_created = models.DateTimeField(auto_now_add=True)

    # Metaclass to define metadata for the model
    class Meta:
        # Order sleep essential by date and time created in descending order
        ordering = ('-date_and_time_created', )

        # Change the plural name of the model in the admin portal
        verbose_name_plural = 'All Sleep Essentials'

    # Function to return the sleep essential title in admin portal
    def __str__(self):
        return self.title

    def get_content_html(self):
        import markdown2
        import re
        
        content = self.description if self.description else ''
        
        # 处理没有alt文本的图片
        def process_images(content):
            # 匹配markdown图片语法: ![alt](url) 或 ![](url)
            pattern = r'!\[(.*?)\]\((.*?)\)'
            def replace(match):
                alt, url = match.groups()
                # 如果没有alt文本，使用商品名称
                if not alt:
                    alt = self.title
                return f'![{alt}]({url})'
            
            return re.sub(pattern, replace, content)
        
        # 处理图片的alt文本
        content = process_images(content)
        
        # 转换markdown为HTML
        extras = ['fenced-code-blocks', 'tables', 'code-friendly']
        return markdown2.markdown(content, extras=extras)
