import pandas as pd

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, generics, status
from rest_framework.response import Response

from .models import Deviation
from .serializers import DeviationSerializer, FileUploadSerializer


class UploadFileView(generics.CreateAPIView):
    serializer_class = FileUploadSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        reader = pd.read_csv(file)
        for _, row in reader.iterrows():
            new_file = Deviation(
                    shiftnumber=row['shiftnumber'],
                    region=row['region'],
                    objectid=row['objectid'],
                    version=row['version'],
                    shiftbegt=row['shiftbegt'],
                    shiftendt=row['shiftendt'],
                    attrval_start_weight=row['attrval__start_weight'],
                    attrval_end_weight=row['attrval__end_weight'],
                    acceptance_sum=row['acceptance_sum'],
                    productid=row['productid'],
                    shipment_sum=row['shipment_sum'],
                    )
            new_file.save()
        return Response({"status": "success"}, status.HTTP_201_CREATED)


class DeviationViewSet(viewsets.ModelViewSet):
    serializer_class = DeviationSerializer
    queryset = Deviation.objects.all()
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
        )
    filterset_fields = ('region', 'objectid', 'productid')
    search_fields = ('shiftnumber', 'region', 'objectid', 'version',
                     'shiftbegt', 'shiftendt', 'attrval_start_weight',
                     'attrval_end_weight', 'acceptance_sum', 'productid',
                     'shipment_sum',)
