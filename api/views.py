from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from .models import Deviation
from .serializers import DeviationSerializer


class DeviationViewSet(viewsets.ModelViewSet):
    serializer_class = DeviationSerializer
    queryset = Deviation.objects.all()
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
        )
    filterset_fields = ('region', 'objectid', 'productid')
    search_fields = '__all__'
    ordering_fields = '__all__'
