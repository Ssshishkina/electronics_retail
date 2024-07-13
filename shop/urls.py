from django.urls import path
from .apps import ShopConfig
from .views import (ProductsCreateAPIView, ProductsListAPIView, ProductsRetrieveAPIView, ProductsUpdateAPIView,
                    ProductsDestroyAPIView, ContactsCreateAPIView, ContactsListAPIView, ContactsRetrieveAPIView,
                    ContactsUpdateAPIView, ContactsDestroyAPIView, TradeLinkCreateAPIView, TradeLinkListAPIView,
                    TradeLinkRetrieveAPIView, TradeLinkUpdateAPIView, TradeLinkDestroyAPIView)

app_name = ShopConfig.name

urlpatterns = [
    path('products/create/', ProductsCreateAPIView.as_view(), name='products-create'),
    path('products/', ProductsListAPIView.as_view(), name='products-list'),
    path('products/<int:pk>/', ProductsRetrieveAPIView.as_view(), name='products-get'),
    path('products/update/<int:pk>/', ProductsUpdateAPIView.as_view(), name='products-update'),
    path('products/delete/<int:pk>/', ProductsDestroyAPIView.as_view(), name='products-delete'),
    path('contacts/create/', ContactsCreateAPIView.as_view(), name='contacts-create'),
    path('contacts/', ContactsListAPIView.as_view(), name='contacts-list'),
    path('contacts/<int:pk>/', ContactsRetrieveAPIView.as_view(), name='contacts-get'),
    path('contacts/update/<int:pk>/', ContactsUpdateAPIView.as_view(), name='contacts-update'),
    path('contacts/delete/<int:pk>/', ContactsDestroyAPIView.as_view(), name='contacts-delete'),
    path('trade_link/create/', TradeLinkCreateAPIView.as_view(), name='trade_link-create'),
    path('', TradeLinkListAPIView.as_view(), name='trade_link-list'),
    path('trade_link/<int:pk>/', TradeLinkRetrieveAPIView.as_view(), name='trade_link-get'),
    path('trade_link/update/<int:pk>/', TradeLinkUpdateAPIView.as_view(), name='trade_link-update'),
    path('trade_link/delete/<int:pk>/', TradeLinkDestroyAPIView.as_view(), name='trade_link-delete'),
]
