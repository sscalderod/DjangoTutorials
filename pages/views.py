from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
from django.shortcuts import render, redirect


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
    
class Product:
    products = [
        {'id':'1', 'name':'TV', 'description':'Smart TV 55 inches', 'price': 890},
        {'id':'2', 'name':'iPhone', 'description':'Latest iPhone model', 'price': 1299},
        {'id':'3', 'name':'Chromecast', 'description':'Streaming device', 'price': 70},
        {'id':'4', 'name':'Glasses', 'description':'Best glasses', 'price': 40},
    ]

class ProductIndexView(View):
    template_name='products/index.html'
    
    def get(self, request):
        viewData = {}
        viewData['title'] = 'Products - Online Store'
        viewData['subtitle'] = 'List of products'
        viewData['products'] = Product.products
        
        return render(request, self.template_name, viewData)
    
class ProductShowView(View):
    template_name='products/show.html'
    
    def get(self, request, id):
        try:
            id=int(id)
            if id<1 or id>len(Product.products):
                return HttpResponseRedirect(reverse('home'))
            
            product = Product.products[int(id)-1]
            
        except (ValueError, IndexError):
            return HttpResponseRedirect(reverse('home'))
        
        viewData = {}
        viewData['title'] = product['name'] + ' - Online Store'
        viewData['subtitle'] = product['name'] + ' - Product Information'
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
        
        
class CartView(View):
   template_name = 'cart/index.html'
   
   def get(self, request):
       # Simulated database for products
       products = {}
       products[121] = {'name': 'Tv samsung', 'price': '1000'}
       products[11] = {'name': 'Iphone', 'price': '2000'}
 
       # Get cart products from session
       cart_products = {}
       cart_product_data = request.session.get('cart_product_data', {})
 
       for key, product in products.items():
           if str(key) in cart_product_data.keys():
               cart_products[key] = product
 
       # Prepare data for the view
       view_data = {
           'title': 'Cart - Online Store',
           'subtitle': 'Shopping Cart',
           'products': products,
           'cart_products': cart_products
       }
 
       return render(request, self.template_name, view_data)
 
   def post(self, request, product_id):
       # Get cart products from session and add the new product
       cart_product_data = request.session.get('cart_product_data', {})
       cart_product_data[product_id] = product_id
       request.session['cart_product_data'] = cart_product_data
 
       return redirect('cart_index')
 
 
class CartRemoveAllView(View):
   def post(self, request):
       # Remove all products from cart in session
       if 'cart_product_data' in request.session:
           del request.session['cart_product_data']
 
       return redirect('cart_index')