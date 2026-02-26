from django.urls import path
from django.core.files.storage import default_storage
from .views import (
    homePageView,
    aboutPageView,
    contactPageView,
    ProductIndexView,
    ProductShowView,
    ProductCreateView,
    ImageViewFactory,
)

ImageView = ImageViewFactory(default_storage)

urlpatterns = [
    path('', homePageView.as_view(), name='home'),
    path('about/', aboutPageView.as_view(), name='about'),
    path('contact/', contactPageView.as_view(), name='contact'),
    path('products/', ProductIndexView.as_view(), name='index'),
    path('products/create', ProductCreateView.as_view(), name='form'),
    path('products/<str:id>', ProductShowView.as_view(), name='show'),
    path('image/', ImageView.as_view(), name='image_index'),
    path('image/save', ImageView.as_view(), name='image_save'),
]