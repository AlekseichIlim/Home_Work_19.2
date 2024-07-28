from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import ContactsView, ProductListView, ProductDetailView, BlogCreateView, BlogListView, \
    BlogDetailView, BlogUpdateView, BlogDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('blog/create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/view/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/edit/<int:pk>/', BlogUpdateView.as_view(), name='blog_update'),
    path('blog/delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete'),
]
