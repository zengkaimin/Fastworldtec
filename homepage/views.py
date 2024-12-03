from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.http import JsonResponse
from .models import HomepageSoftware, BlogAndReview, Message  # 本应用的模型
from .forms import MessageForm  # 添加这行导入
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
    # Handle POST requests to collect and save user messages
    if request.method == 'POST':
        # Instantiate the form with POST data
        form = MessageForm(request.POST)

        if form.is_valid():
            # Clean the form data
            cleaned = form.cleaned_data
            user_messages = Message(
                full_name=cleaned['full_name'],
                email=cleaned['email'],
                message=cleaned['message'],
            )
            try:
                # Save the message to the database
                user_messages.save()

                # Return a JSON response indicating success
                return JsonResponse({'status': 'success', 'message': 'Message sent successfully!'})
            except Exception as e:
                # Return error response
                return JsonResponse({'status': 'error', 'message': f'An error occurred: {str(e)}'}, status=500)
        else:
            # Return validation error response
            return JsonResponse({'status': 'error', 'message': 'Invalid form data'}, status=400)

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

def blog_and_review_detail(request, slug):
    """
    View function for displaying a specific blog or review.
    """
    # Get the specific blog or review object or return 404 if not found
    blog_and_review = get_object_or_404(BlogAndReview, slug=slug)
    
    # Create a context dictionary with the blog or review object
    context = {
        'blog_and_review': blog_and_review,
    }
    
    # Render the blog and review detail template with the context
    return render(request, 'homepage_html/blog_and_review_detail.html', context)

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
