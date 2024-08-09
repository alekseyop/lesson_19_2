from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductUpdateView, ContactsView, ProductCreateView, ProductDeleteConfirm, \
    ProductDetailView

app_name = CatalogConfig.name





urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('catalog/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('catalog/create/', ProductCreateView.as_view(), name='product_create'),
    path('catalog/<int:pk>/update', ProductUpdateView.as_view(), name='product_update'),
    path('catalog/<int:pk>/delete', ProductDeleteConfirm.as_view(), name='product_delete'),

]
