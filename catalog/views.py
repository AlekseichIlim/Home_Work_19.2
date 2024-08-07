from django.http import request
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify
from django.core.mail import send_mail

from catalog.forms import ProductForm
from catalog.models import Product, Blog


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')




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

    def post(self, request):
        if self.request.method == 'POST':
            name = self.request.POST.get('name')
            phone = request.POST.get('phone')
            message = request.POST.get('message')
            print(f'{name}, контактный телефон: {phone}\nСообщение: {message}')
        return render(request, 'catalog/contacts.html')


# def product_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {
#         "product": product
#     }
#     return render(request, 'product_detail.html', context)


class ProductDetailView(DetailView):
    model = Product


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        """выводит только опубликованные блоги"""
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content', 'picture')
    success_url = reverse_lazy('catalog:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        """Cчетчик просмотров блога"""
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'content', 'picture')

    # success_url = reverse_lazy('materials:list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:blog_detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blog_list')
