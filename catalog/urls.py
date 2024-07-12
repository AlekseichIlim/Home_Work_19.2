from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, index

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts')
]
