from rest_framework import serializers

from .models import Deviation


class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()


class DeviationSerializer(serializers.ModelSerializer):
    deviation = serializers.SerializerMethodField()

    class Meta:
        model = Deviation
        fields = ('id', 'region', 'objectid', 'productid', 'shiftnumber',
                  'shiftbegt', 'shiftendt', 'acceptance_sum', 'shipment_sum',
                  'attrval_start_weight', 'attrval_end_weight', 'version',
                  'deviation')

    def get_deviation(self, obj):
        return (obj.attrval_start_weight + obj.shipment_sum
                - obj.attrval_end_weight - obj.acceptance_sum)
