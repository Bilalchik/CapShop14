from django.urls import path
from . import views

urlpatterns = [
    path('product_list/', views.ProductListView.as_view()),
    path('index/', views.IndexView.as_view())
]
