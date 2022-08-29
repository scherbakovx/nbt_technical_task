import logging

from django.utils import dateparse
from django.db.models import Avg, FloatField
from django.db.models.functions import Cast
from django.db.models.fields.json import KeyTextTransform

from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from api.models import Company, Device, Measurement
from api.serializers import CompanySerializer, DeviceSerializer, MeasurementSerializer

LOGGER = logging.getLogger()


class CompanyViewset(viewsets.ModelViewSet):

    model = Company
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class DeviceViewset(viewsets.ModelViewSet):

    model = Device
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

    def filter_queryset(self, queryset):

        if company_id := self.request.GET.get('company_id'):
            queryset = queryset.filter(company_id=company_id)

        if labels := self.request.query_params.getlist("labels[]"):
            queryset = queryset.filter(labels__overlap=labels)

        return super().filter_queryset(queryset)


class MeasurementViewset(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin):

    model = Measurement
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def filter_queryset(self, queryset):

        if device_id := self.request.GET.get('device_id'):
            queryset = queryset.filter(device_id=device_id)

        if company_id := self.request.GET.get('company_id'):
            queryset = queryset.filter(device__company_id=company_id)

        # ex. before=2003-06-29T11:00:00+00:00
        if before_string := self.request.GET.get('before'):
            before_datetime = dateparse.parse_datetime(before_string.replace(" ", "+"))
            queryset = queryset.filter(date__lte=before_datetime)

        # ex. after=1983-06-29T11:00:00+00:00
        if after_string := self.request.GET.get('after'):
            after_datetime = dateparse.parse_datetime(after_string.replace(" ", "+"))
            queryset = queryset.filter(date__gte=after_datetime)

        return super().filter_queryset(queryset)

    @action(methods=["get"], detail=False)
    def average_temperatures(self, request):

        queryset = self.filter_queryset(self.queryset)

        temperature = Cast(KeyTextTransform('temperature', 'data'), FloatField())

        average_temperatures = queryset.annotate(temperature=temperature).values('device_id').annotate(
            avg_temperature=Avg('temperature'))

        return Response({"average_temperatures": average_temperatures}, status=status.HTTP_200_OK)
