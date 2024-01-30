import django_filters
# from django_filters import DateFilter
from .models import *

class OrderFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(field_name='date_created',lookup_expr='gte',label='Starting from date')
    end_date = django_filters.DateFilter(field_name='date_created',lookup_expr='lte',label='to')
    class Meta:
        model = Order
        fields = ['product','status']
