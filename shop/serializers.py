from rest_framework import serializers
from .models import Products, Contacts, TradeLink


class ProductsSerializer(serializers.ModelSerializer):
    """Сериализатор продукта"""
    class Meta:
        model = Products
        fields = ('pk', 'name', 'product_model', 'date_of_release')


class ContactsSerializer(serializers.ModelSerializer):
    """Сериализатор контактов"""
    class Meta:
        model = Contacts
        fields = ('pk', 'email', 'country', 'city', 'street', 'house')
        read_only_fields = ('email',)


class TradeLinkSerializer(serializers.ModelSerializer):
    """Сериализатор звена сети"""
    class Meta:
        model = TradeLink
        fields = ('pk', 'name', 'link_network', 'product', 'supplier', 'contact', 'dept', 'time')
        read_only_fields = ('dept',)
