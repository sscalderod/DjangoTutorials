from django.urls import path
from .views import homePageView, aboutPageView, contactPageView, ProductIndexView, ProductShowView, ProductCreateView, ProductCreatedView

urlpatterns = [
    path('', homePageView.as_view(), name='home'),
    path('about/', aboutPageView.as_view(), name='about'),
    path('contact/', contactPageView.as_view(), name='contact'),
    path('products/', ProductIndexView.as_view(), name='index'),
    path('products/create', ProductCreateView.as_view(), name='form'),
    path('products/created', ProductCreatedView.as_view(), name='product-created'),
    path('products/<str:id>', ProductShowView.as_view(), name='show'),
]