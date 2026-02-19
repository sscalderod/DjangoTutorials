from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product


class homePageView(TemplateView):
    template_name = 'pages/home.html'
    
class aboutPageView(TemplateView):
    template_name = 'pages/about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': 'About Us - Online Store',
            'subtitle': 'About us',
            'description': 'This is the about page of our online store.',
            'author': 'Developed by Samuel Calderon',
        })
        return context
    
class contactPageView(TemplateView):
    template_name = 'pages/contact.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'description': 'Feel free to reach out to us through the following contact information.',
            'name': 'Online Store Support',
            'correo': 'contact@onlinestore.com',
            'numtel': '+1234567890',
        })
        return context

class ProductIndexView(View):
    template_name='products/index.html'
    
    def get(self, request):
        viewData = {}
        viewData['title'] = 'Products - Online Store'
        viewData['subtitle'] = 'List of products'
        viewData['products'] = Product.objects.all()
        
        return render(request, self.template_name, viewData)
    
class ProductShowView(View):
    template_name='products/show.html'
    
    def get(self, request, id):
        try:
            product_id=int(id)
            if product_id<1:
                raise ValueError("Product ID must be 1 or greater.")
            product = get_object_or_404(Product, pk=product_id)
        except (ValueError, IndexError):
            return HttpResponseRedirect(reverse('home'))
        
        viewData = {}
        product = get_object_or_404(Product, pk=id)
        viewData['title'] = product.name + ' - Online Store'
        viewData['subtitle'] = product.name + ' - Product Information'
        viewData['product'] = product

        return render(request, self.template_name, viewData)
    
class ProductForm(forms.Form):
    name=forms.CharField(required=True)
    price=forms.FloatField(required=True)
    
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is None or price <= 0:
            raise forms.ValidationError('Price must be greater than zero.')
        return price
    
class ProductCreateView(View):
    template_name='products/create.html'
    
    def get(self, request):
        form = ProductForm()
        viewData = {}
        viewData['title'] = 'Create Product'
        viewData['form'] = form
        return render(request, self.template_name, viewData)
    
    def post(self, request):
        form = ProductForm(request.POST)
        
        if form.is_valid():
            viewData = {}
            viewData['title'] = 'Product Created'
            viewData['subtitle'] = form.cleaned_data['name']
            viewData['price'] = form.cleaned_data['price']
            return render(request, 'products/created.html', viewData)
        else:
            viewData = {}
            viewData['title'] = 'Create Product'
            viewData['form'] = form
            return render(request, self.template_name, viewData)

class ProductListView(ListView): 
    model = Product 
    template_name = 'product_list.html' 
    context_object_name = 'products'  # This will allow you to loop through 'products' in your template 
 
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs) 
        context['title'] = 'Products - Online Store' 
        context['subtitle'] = 'List of products' 
        return context 
        