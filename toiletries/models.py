from django.db import models
from mdeditor.fields import MDTextField

class Toiletries(models.Model):
    objects = None  # Add to prevent unresolved attribute reference error in views.py in PYCHARM.
    image = models.ImageField(upload_to='all_toiletries_images')
    title = models.CharField(max_length=255)
    price = models.CharField(max_length=50, blank=True)
    description = MDTextField(blank=True)
    affiliate_link = models.CharField(max_length=2083)
    # Whether this item is featured (是否精选商品)
    is_featured = models.BooleanField(
        default=False, 
        verbose_name='Featured Item (精选商品)'
    )
    date_and_time_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_and_time_created', )
        verbose_name_plural = 'All Toiletries'

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
