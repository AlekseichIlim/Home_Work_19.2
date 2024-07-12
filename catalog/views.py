from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def product_list(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, 'home.html', context)

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name}, контактный телефон: {phone}\nСообщение: {message}')
    return render(request, 'contacts.html')

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        "product": product
    }
    return render(request, 'product_detail.html', context)

