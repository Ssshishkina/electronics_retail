from django.contrib import admin
from django.utils.html import format_html
from .models import Products, Contacts, TradeLink

admin.site.register(Products)

admin.site.register(Contacts)


@admin.register(TradeLink)
class TradeLinkAdmin(admin.ModelAdmin):
    fields = ['name', 'link_network', 'product', 'supplier', 'contact', 'dept']
    list_display = ['name', 'link_network', 'product', 'supplier', 'contact', 'dept', 'get_supplier']
    list_filter = ['contact__city', 'contact__country']
    actions = ['clear_the_dept']
    readonly_fields = ['dept']

    @admin.action(description="Удалить задолженность перед поставщиком")
    def clear_the_dept(self, request, queryset):
        count = queryset.update(dept=0)
        self.message_user(request, f"Изменено {count} записей!")

    @admin.display(description="Поставщик")
    def get_supplier(self, obj):
        if obj.supplier is not None:
            return format_html("<a href='{url}'>{name}</a>", url=obj.supplier.id, name=obj.supplier.name)
        return "-"
