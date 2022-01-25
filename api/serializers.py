from rest_framework import serializers

from .models import Deviation


class DeviationSerializer(serializers.ModelSerializer):
    deviation = serializers.SerializerMethodField()

    class Meta:
        model = Deviation
        fields = ('shiftnumber', 'region', 'objectid', 'version', 'shiftbegt',
                  'shiftendt', 'attrval_start_weight', 'attrval_end_weight',
                  'acceptance_sum', 'index', 'productid', 'shipment_sum',
                  'deviation')

    def get_deviation(self, obj):
        attrval_start_weight = obj.attrval_start_weight
        shipment_sum = obj.shipment_sum
        attrval_end_weight = obj.attrval_end_weight
        acceptance_sum = obj.acceptance_sum
        result = attrval_start_weight + shipment_sum - attrval_end_weight - acceptance_sum
        return result
