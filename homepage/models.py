from django.db import models  # Import the models module from Django
from django.utils import timezone  # 添加这行导入
from mdeditor.fields import MDTextField  # Import the MDTextField module from mdeditor


# Homepage Software Section object
class HomepageSoftware(models.Model):
    objects = None  # Add to prevent unresolved attribute reference error in views.py in PYCHARM.

    # Field for storing an image, uploaded to 'homepage_software_images' directory
    image = models.ImageField(upload_to='homepage_software_images', blank=True, null=True)

    # Field for the title of the software, with a maximum length of 255 characters
    title = models.CharField(max_length=255)

    # Field for the price of the software, optional, with a maximum length of 50 characters
    price = models.CharField(max_length=50, blank=True)

    # Field for a description of the software, optional, with no maximum length
    description = models.TextField(blank=True)

    # Field for storing an affiliate link, with a maximum length of 2083 characters
    affiliate_link = models.CharField(max_length=2083)

    # Field for storing the creation date and time, automatically set when an object is created
    date_and_time_created = models.DateTimeField(auto_now_add=True)

    # Meta class
    class Meta:
        # Order objects by creation date in descending order
        ordering = ('-date_and_time_created',)

        # Display name for the model in the admin portal
        verbose_name_plural = 'Homepage Software Only'

    # Method to return a string representation of the object
    def __str__(self):
        # Return title of the object
        return self.title


# Blog and Review Section Object
class BlogAndReview(models.Model):
    DoesNotExist = None  # Add to prevent unresolved attribute reference error in views.py in PYCHARM.
    objects = None  # Add to prevent unresolved attribute reference error in views.py in PYCHARM.

    # Field for storing an image, uploaded to 'blog_and_review_images' directory
    image = models.ImageField(upload_to='blog_and_review_images', blank=True, null=True)

    # Field for the title of the blog or review, with a maximum length of 255 characters
    title = models.CharField(max_length=255)

    # Field for the URL slug, generated from title
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    # Field for an excerpt or summary of the blog or review, with no maximum length
    excerpt = models.TextField(blank=True, null=True)

    # Field for storing the markdown content
    content = MDTextField(blank=True)

    # Field for storing an affiliate link, optional, with a maximum length of 2083 characters
    affiliate_link = models.CharField(max_length=2083, blank=True)

    # Field for storing the creation date and time, automatically set when an object is created
    date_and_time_created = models.DateTimeField(auto_now_add=True)

    def get_content_html(self):
        import markdown2
        import re
        
        content = self.content if self.content else ''
        
        # 处理没有alt文本的图片
        def process_images(content):
            # 匹配markdown图片语法: ![alt](url) 或 ![](url)
            pattern = r'!\[(.*?)\]\((.*?)\)'
            def replace(match):
                alt, url = match.groups()
                # 如果没有alt文本，使用博客标题
                if not alt:
                    alt = self.title
                return f'![{alt}]({url})'
            
            return re.sub(pattern, replace, content)
        
        # 处理图片的alt文本
        content = process_images(content)
        
        # 转换markdown为HTML
        extras = ['fenced-code-blocks', 'tables', 'code-friendly']
        return markdown2.markdown(content, extras=extras)

    def save(self, *args, **kwargs):
        if not self.slug:
            from django.utils.text import slugify
            # 生成基础slug
            base_slug = slugify(self.title)
            # 检查是否存在相同的slug
            slug = base_slug
            n = 1
            while BlogAndReview.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{n}"
                n += 1
            self.slug = slug
        super().save(*args, **kwargs)

    # Meta class
    class Meta:
        # Order objects by creation date in descending order
        ordering = ('-date_and_time_created',)

        # Display name for the model in the admin portal
        verbose_name_plural = 'Blogs & Reviews'

    # Method to return a string representation of the object
    def __str__(self):
        # Return title of the object
        return self.title


# Message Section Object
class Message(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Message from {self.full_name}"
