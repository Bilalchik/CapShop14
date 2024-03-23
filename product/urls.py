from django.urls import path
from . import views

urlpatterns = [
    path('product_list/', views.ProductListView.as_view()),
    path('index/', views.IndexView.as_view()),
    path('product_detail/<int:pk>/', views.ProductDetailView.as_view()),
    path('storage_create/', views.StorageCreateView.as_view()),
    path('storage_update/<int:pk>/', views.StorageUpdateView.as_view()),
    path('storage_delete/<int:pk>/', views.StorageDeleteView.as_view()),
    path('basket_list/<int:pk>/', views.BasketListCreateView.as_view()),
    path('basket_detail/<int:pk>/', views.BasketDetailView.as_view()),
    path('basket_update/<int:pk>/', views.BasketListCreateView.as_view()),
    path('basket_delete/<int:pk>/', views.BasketDeleteView.as_view()),
]
