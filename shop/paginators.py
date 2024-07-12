from rest_framework.pagination import PageNumberPagination


class ProductsPaginator(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'


class TradeLinkPaginator(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
