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

from .views import homePageView, aboutPageView, contactPageView, ProductIndexView, ProductShowView, ProductCreateView, ProductCreatedView, CartView, CartRemoveAllView


urlpatterns = [
    path('', homePageView.as_view(), name='home'),
    path('about/', aboutPageView.as_view(), name='about'),
    path('contact/', contactPageView.as_view(), name='contact'),
    path('products/', ProductIndexView.as_view(), name='index'),
    path('products/create', ProductCreateView.as_view(), name='form'),
    path('products/created', ProductCreatedView.as_view(), name='product-created'),
    path('products/<str:id>', ProductShowView.as_view(), name='show'),

    path('image/', ImageView.as_view(), name='image_index'),
    path('image/save', ImageView.as_view(), name='image_save'),

    path('cart/', CartView.as_view(), name='cart_index'),
    path('cart/add/<str:product_id>', CartView.as_view(), name='cart_add'),
    path('cart/removeAll', CartRemoveAllView.as_view(), name='cart_removeAll'),

]