from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.http import JsonResponse
from .models import HomepageSoftware, BlogAndReview, Message  # 本应用的模型
# 从其他应用导入模型
from BabyClothes.models import BabyClothes
from DailyEssentials.models import DailyEssentials
from FeedingSupplies.models import FeedingSupplies
from LargeItems.models import LargeItems
from SleepEssentials.models import SleepEssentials
from toiletries.models import Toiletries
from django.views.decorators.csrf import ensure_csrf_cookie

@ensure_csrf_cookie
def homepage_view(request):
    context = {
        'homepage_software': [],
        'blog_and_review': [],
        'featured_products': {
            'baby_clothes': [],
            'daily_essentials': [],
            'feeding_supplies': [],
            'large_items': [],
            'sleep_essentials': [],
            'toiletries': [],
        }
    }

    try:
        # 获取精选商品
        context['featured_products']['baby_clothes'] = BabyClothes.objects.filter(is_featured=True)
        context['featured_products']['daily_essentials'] = DailyEssentials.objects.filter(is_featured=True)
        context['featured_products']['feeding_supplies'] = FeedingSupplies.objects.filter(is_featured=True)
        context['featured_products']['large_items'] = LargeItems.objects.filter(is_featured=True)
        context['featured_products']['sleep_essentials'] = SleepEssentials.objects.filter(is_featured=True)
        context['featured_products']['toiletries'] = Toiletries.objects.filter(is_featured=True)

        # 获取其他数据
        context['homepage_software'] = HomepageSoftware.objects.all()
        context['blog_and_review'] = BlogAndReview.objects.all()

    except Exception as e:
        messages.error(request, f'An error occurred: {str(e)}')

    return render(request, 'homepage_html/homepage.html', context)

def blog_and_review_detail_view(request, pk):
    """
    显示单个博客和评论的详细视图
    """
    try:
        # 获取指定的博客和评论，如果不存在则返回404
        blog_and_review = get_object_or_404(BlogAndReview, pk=pk)
        
        # 准备上下文数据
        context = {
            'blog_and_review': blog_and_review
        }
        
        # 渲染详细页面
        return render(request, 'homepage_html/blog_and_review_detail.html', context)
        
    except Exception as e:
        messages.error(request, f'An error occurred: {str(e)}')
        return render(request, 'homepage_html/blog_and_review_detail.html', {'blog_and_review': None})

def mark_as_completed(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        action = request.POST.get('action', 'complete')
        
        if product_id:
            response = JsonResponse({'status': 'success'})
            
            if action == 'cancel':
                # 删除 cookie
                response.delete_cookie(f'completed_product_{product_id}')
            else:
                # 设置 cookie
                response.set_cookie(
                    f'completed_product_{product_id}', 
                    'true', 
                    max_age=365*24*60*60,
                    samesite='Lax',
                    secure=False,
                    httponly=False
                )
            return response
            
        return JsonResponse({'status': 'error', 'message': 'No product_id provided'}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)
