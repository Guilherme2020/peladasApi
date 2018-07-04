from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import authentication, permissions, filters


class FilteringAndOrderingMixin(object):
    """Default settings for filtering """
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )