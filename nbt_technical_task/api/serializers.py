from rest_framework import serializers

from api.models import Company, Device, Measurement


class CompanySerializer(serializers.ModelSerializer):

    class Meta:

        model = Company
        fields = (
            'id',
            'name',
            'location',
        )


class DeviceSerializer(serializers.ModelSerializer):

    class Meta:

        model = Device
        fields = (
            'device_id',
            'company',
            'active',
            'labels',
        )


class MeasurementSerializer(serializers.ModelSerializer):

    class Meta:

        model = Measurement
        fields = (
            'device',
            'date',
            'data',
        )
