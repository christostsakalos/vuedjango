from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .models import Customer

DEFAULT_PAGE = 1
DEFAULT_PAGE_SIZE = 15



class CustomPagination(PageNumberPagination):
    page = DEFAULT_PAGE
    page_size = DEFAULT_PAGE_SIZE
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        rowsNumber = Customer.objects.all().count()
        return Response({
            'data': data,
            'pagination': {
                # Thanks to https://stackoverflow.com/questions/46626994/
                'last_page': self.page.paginator.num_pages,
                'page': int(self.request.GET.get('page', DEFAULT_PAGE)),
                'rowsNumber': rowsNumber,
                'rowsPerPage': int(self.request.GET.get('page_size', self.page_size))
            }
        })

class CategoryPagination(PageNumberPagination):
    page = DEFAULT_PAGE
    page_size = 5
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response({
            'data': data,
            'meta': {
                # Thanks to https://stackoverflow.com/questions/46626994/
                'last_page': self.page.paginator.num_pages,
                'page': int(self.request.GET.get('page', DEFAULT_PAGE)),
                'page_size': int(self.request.GET.get('page_size', self.page_size))
            }
        })
