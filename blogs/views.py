from django.shortcuts import redirect, render, get_object_or_404
from .models import Blog, Category


def posts_by_category(request, category_id):
    # Fetch the posts that belongs to the category with the id caatgory_id
    posts = Blog.objects.filter(status='Published', category=category_id)
    # Use try/except block when you want to do some custom action if the category doesnt exist
    try:
        category = Category.objects.get(pk=category_id)
    except:
        # redirect the user to homepage
        return redirect('home')
    
    # Use get_object_or_404 when you want to show 404 error page if the category doesnt exist
    # category = get_object_or_404(Category, pk=category_id)
    
    context = {
        'posts':posts,
        'category':category,
    }
    return render(request, "posts_by_category.html", context)
