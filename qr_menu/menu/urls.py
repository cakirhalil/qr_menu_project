from django.urls import path
from . import views
from .views import category_detail

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<int:category_id>/', category_detail, name='category_detail'),
]
