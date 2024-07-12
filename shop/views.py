from rest_framework import generics
from .models import Products, TradeLink, Contacts
from .paginators import TradeLinkPaginator, ProductsPaginator
from .permissions import IsActivePermission
from .serializers import ContactsSerializer, ProductsSerializer, TradeLinkSerializer


class ProductsCreateAPIView(generics.CreateAPIView):
    """
    Контроллер создания товара
    """
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()
    permission_classes = [IsActivePermission]


class ProductsListAPIView(generics.ListAPIView):
    """
    Контроллер просмотра списка товаров
    """
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()
    permission_classes = [IsActivePermission]
    pagination_class = ProductsPaginator


class ProductsRetrieveAPIView(generics.RetrieveAPIView):
    """
    Контроллер просмотра товара
    """
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()
    permission_classes = [IsActivePermission]


class ProductsUpdateAPIView(generics.UpdateAPIView):
    """
    Контроллер обновления товара
    """
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()
    permission_classes = [IsActivePermission]


class ProductsDestroyAPIView(generics.DestroyAPIView):
    """
    Контроллер удаления товара
    """
    queryset = Products.objects.all()
    permission_classes = [IsActivePermission]


class ContactsCreateAPIView(generics.CreateAPIView):
    """
    Контроллер создания контакта
    """
    serializer_class = ContactsSerializer
    queryset = Contacts.objects.all()
    permission_classes = [IsActivePermission]

    def perform_create(self, serializer):
        new_contact = serializer.save()
        new_contact.owner = self.request.user
        new_contact.save()


class ContactsListAPIView(generics.ListAPIView):
    """
    Контроллер просмотра списка контактов
    """
    serializer_class = ContactsSerializer
    queryset = Contacts.objects.all()
    permission_classes = [IsActivePermission]


class ContactsRetrieveAPIView(generics.RetrieveAPIView):
    """
    Контроллер просмотра контакта
    """
    serializer_class = ContactsSerializer
    queryset = Contacts.objects.all()
    permission_classes = [IsActivePermission]


class ContactsUpdateAPIView(generics.UpdateAPIView):
    """
    Контроллер обновления контакта
    """
    serializer_class = ContactsSerializer
    queryset = Contacts.objects.all()
    permission_classes = [IsActivePermission]


class ContactsDestroyAPIView(generics.DestroyAPIView):
    """
    Контроллер удаления контакта
    """
    queryset = Contacts.objects.all()
    permission_classes = [IsActivePermission]


class TradeLinkCreateAPIView(generics.CreateAPIView):
    """
    Контроллер создания товара
    """
    serializer_class = TradeLinkSerializer
    queryset = TradeLink.objects.all()
    permission_classes = [IsActivePermission]

    def perform_create(self, serializer):
        new_trade_link = serializer.save()
        new_trade_link.owner = self.request.user
        new_trade_link.save()


class TradeLinkListAPIView(generics.ListAPIView):
    """
    Контроллер просмотра списка звеньев сети
    """
    serializer_class = TradeLinkSerializer
    queryset = TradeLink.objects.all()
    permission_classes = [IsActivePermission]
    pagination_class = TradeLinkPaginator


class TradeLinkRetrieveAPIView(generics.RetrieveAPIView):
    """
    Контроллер просмотра звена сети
    """
    serializer_class = TradeLinkSerializer
    queryset = TradeLink.objects.all()
    permission_classes = [IsActivePermission]


class TradeLinkUpdateAPIView(generics.UpdateAPIView):
    """
    Контроллер обновления звена сети
    """
    serializer_class = TradeLinkSerializer
    queryset = TradeLink.objects.all()
    permission_classes = [IsActivePermission]


class TradeLinkDestroyAPIView(generics.DestroyAPIView):
    """
    Контроллер удаления звена сети
    """
    queryset = TradeLink.objects.all()
    permission_classes = [IsActivePermission]
