from django.http import request
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Product


# def product_list(request):
#     products = Product.objects.all()
#     context = {
#         "products": products
#     }
#     return render(request, 'products_list.html', context)

class ProductListView(ListView):
    model = Product


# def contacts(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         print(f'{name}, контактный телефон: {phone}\nСообщение: {message}')
#     return render(request, 'contacts.html')

class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'

    def get_context_data(self, **kwargs):
        context = super(ContactsView, self).get_context_data(**kwargs)
        contacts = self.request.POST.get('name')
        print(contacts)
        return context


# def product_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {
#         "product": product
#     }
#     return render(request, 'product_detail.html', context)


class ProductDetailView(DetailView):
    model = Product


