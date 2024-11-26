from django.contrib import admin  # Import Django admin module
from django.urls import path, include, re_path  # Import path, include, and re_path functions for URL routing
from django.conf import settings  # Import settings for configuration
from django.views.static import serve  # Import serve view to serve static files

# 修改 admin 站点标题
admin.site.site_header = 'Beginmama Admin'  # 登录页面和管理页面的顶部标题
admin.site.site_title = 'Beginmama Admin Portal'  # 浏览器标签页标题
admin.site.index_title = 'Welcome to Beginmama Admin Portal'  # 管理页面的欢迎文本

urlpatterns = [
    # app routing at project level
    path('admin/', admin.site.urls),  # Route for Django admin site
    path('', include('homepage.urls')),  # Route for homepage app URLs (default)
    path('', include('software.urls')),  # Route for software app URLs
    path('sleep-essentials/', include('SleepEssentials.urls')),  # Route for SleepEssentials app URLs
    path('baby-clothes/', include('BabyClothes.urls')),  # Route for BabyClothes app URLs
    path('toiletries/', include('toiletries.urls')),  # Route for Toiletries app URLs
    path('feeding-supplies/', include('FeedingSupplies.urls')),  # Route for FeedingSupplies app URLs
    path('daily-essentials/', include('DailyEssentials.urls')),  # Route for DailyEssentials app URLs
    path('large-items/', include('LargeItems.urls')),  # Route for LargeItems app URLs
    # serve static files
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),  # Route to serve media files
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),  # Route to serve static files
]
