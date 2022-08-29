from django.db import models
from django.core.validators import RegexValidator
from django.contrib.postgres.fields import ArrayField


class Company(models.Model):

    name = models.CharField(null=False, blank=False, max_length=255)
    location = models.CharField(null=False, blank=False, max_length=255)

    def __str__(self):
        return f"{self.id}. {self.name} @ {self.location}"

    class Meta:
        verbose_name_plural = "companies"


class Device(models.Model):

    device_id = models.CharField(primary_key=True,
                                unique=True,
                                 null=False,
                                 blank=False,
                                 max_length=255,
                                 validators=[
                                     RegexValidator(regex='^[a-zA-Z]{3}-\d{8}-\d{4}-\d{6}$',
                                                    message='Custom Device PK (ex. nrf-12312980-3138-123123)',
                                                    code='invalid_device_id'),
                                 ])

    company = models.ForeignKey(Company, null=False, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
    labels = ArrayField(models.CharField(max_length=255), default=list)

    def __str__(self):
        return f"{self.device_id}"

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Device, self).save(*args, **kwargs)


class Measurement(models.Model):

    device = models.ForeignKey(Device, to_field='device_id', on_delete=models.CASCADE)
    date = models.DateTimeField()
    data = models.JSONField(default=dict)
