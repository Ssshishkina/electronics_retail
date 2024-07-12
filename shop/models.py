from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Products(models.Model):
    """Модель товара"""

    name = models.CharField(max_length=250, verbose_name='название')
    product_model = models.CharField(max_length=250, verbose_name='модель товара')
    date_of_release = models.DateField(verbose_name='дата выхода товара на рынок', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'


class Contacts(models.Model):
    """Модель контактного лица"""

    email = models.EmailField(verbose_name='email контактного лица')
    country = models.CharField(max_length=100, verbose_name='страна')
    city = models.CharField(max_length=100, verbose_name='город')
    street = models.CharField(max_length=150, verbose_name='улица')
    house = models.CharField(max_length=20, verbose_name='номер дома')

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'


class TradeLink(models.Model):
    """Модель звена сети"""

    TRADE_LINK_FACTORY = 'FACTORY'
    TRADE_LINK_RETAIL_NETWORK = 'RETAIL_NETWORK'
    TRADE_LINK_INDIVIDUAL_ENTREPRENEUR = 'INDIVIDUAL_ENTREPRENEUR'
    TRADE_LINK_CHOICES = ((TRADE_LINK_FACTORY, 'завод'),
                          (TRADE_LINK_RETAIL_NETWORK, 'розничная сеть'),
                          (TRADE_LINK_INDIVIDUAL_ENTREPRENEUR, 'индивидуальный предприниматель')
                          )

    name = models.CharField(verbose_name='название организации', max_length=250)
    link_network = models.CharField(max_length=150, verbose_name='звено цепи', choices=TRADE_LINK_CHOICES)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name='продукт', **NULLABLE)
    supplier = models.ForeignKey('TradeLink', on_delete=models.SET_NULL, verbose_name='поставщик', **NULLABLE)
    contact = models.ForeignKey(Contacts, on_delete=models.DO_NOTHING, verbose_name='контакты', **NULLABLE)
    dept = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='задолженность перед поставщиком', **NULLABLE)
    time = models.DateTimeField(auto_now_add=True, verbose_name='дата и время создания', **NULLABLE)

    def __str__(self):
        return f'{self.name} - {self.link_network}'

    class Meta:
        verbose_name = 'звено сети'
        verbose_name_plural = 'звенья сети'
