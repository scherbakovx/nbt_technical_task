from django.urls import path
from django.views.generic import TemplateView

from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

from api.views import CompanyViewset, DeviceViewset, MeasurementViewset

router = DefaultRouter()

router.register(r"companies", CompanyViewset)
router.register(r"devices", DeviceViewset)
router.register(r"measurements", MeasurementViewset)
