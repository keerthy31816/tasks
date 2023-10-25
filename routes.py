from django.urls import path
from .views import ProductListView, ProductDetailView

urlpatterns = [
    path('product/', ProductListView.as_view(), name='productlist'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='productdetail'),
    path('product/search/', ProductListView.as_view(), name='productsearch'),
]
