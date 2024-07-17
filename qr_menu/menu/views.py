from django.shortcuts import render,get_object_or_404
from .models import Category, Company

def home(request):
    categories = Category.objects.all()
    company = Company.objects.first()  # Sadece bir şirket bilgisi al
    return render(request, 'menu/home.html', {'categories': categories, 'company': company})


def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    menu_items = category.menu_items.all()
    return render(request, 'menu/category_detail.html', {'category': category, 'menu_items': menu_items})

def category_view(request, category_id):
    category = Category.objects.get(id=category_id)
    categories = Category.objects.all()
    context = {
        'category': category,
        'categories': categories,
    }
    return render(request, 'category_template.html', context)