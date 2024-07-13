from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import Products, Contacts, TradeLink

admin.site.register(Products)

admin.site.register(Contacts)


@admin.register(TradeLink)
class TradeLinkAdmin(admin.ModelAdmin):
    fields = ['name', 'link_network', 'product', 'supplier', 'contact', 'dept']
    list_display = ['name', 'link_network', 'product', 'supplier', 'contact', 'dept', 'get_supplier']
    list_filter = ['contact__city', 'contact__country']
    actions = ['clear_the_dept']

    def get_supplier(self, obj):
        if obj.supplier:
            url = reverse('admin:shop_tradelink_change', args=[obj.supplier.id])
            link = '<a href="{}">Посмотреть карточку поставщика</a>'.format(url)
            return mark_safe(link)

        return 'Поставщик не указан'
    get_supplier.short_description = 'Ссылка на поставщика'

    @admin.action(description="Удалить задолженность перед поставщиком")
    def clear_the_dept(self, request, queryset):
        queryset.update(dept=0)
