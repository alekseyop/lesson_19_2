from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, product_detail

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
    # path('product_list/', product_list, name='product_list'),
    # path('product_detail/', product_detail, name='product_detail'),
    #  path('product/<int:pk>/', product_detail, name='product_detail'),
    path('contacts/', contacts, name='contacts'),
]
