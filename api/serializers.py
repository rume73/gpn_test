from rest_framework import serializers

from .models import Deviation


class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()


class DeviationSerializer(serializers.ModelSerializer):
    deviation = serializers.SerializerMethodField()

    class Meta:
        model = Deviation
        fields = ('id', 'shiftnumber', 'region', 'objectid', 'version',
                  'shiftbegt','shiftendt', 'attrval_start_weight',
                  'attrval_end_weight', 'acceptance_sum', 'index', 'productid',
                  'shipment_sum', 'deviation')

    def get_deviation(self, obj):
        return (obj.attrval_start_weight + obj.shipment_sum
                - obj.attrval_end_weight - obj.acceptance_sum)
