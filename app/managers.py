import datetime

from django.db import models


class ProducerManager(models.Manager):
    def get_by_city(self, city):
        return self.filter(city__name=city)


class SpecificationsManager(models.Manager):
    def get_older_than(self, term):
        return self.filter(date_of_manufacture__lte=datetime.date.today() - term)

    def get_last(self):
        return self.order_by('-date_of_manufacture')


class CameraManager(models.Manager):
    def get_camera(self, camera_id):
        try:
            q = self.get(pk=camera_id)
        except self.DoesNotExist:
            q = None

        return q

    def get_problem(self):
        return self.exclude(state__state=0)

    def get_error(self):
        return self.filter(state__state=1)

    def get_warning(self):
        return self.filter(state__state=2)

    def get_failure(self):
        return self.filter(state__state=3)

    def filter_pk(self, pk):
        return self.filter(pk__in=pk)


class ServiceOrganizationManager(models.Manager):
    def get_by_city(self, city):
        return self.filter(city__name=city)


class ServiceManager(models.Manager):
    def get_record(self, service_id):
        try:
            q = self.get(pk=service_id)
        except self.DoesNotExist:
            q = None

        return q

    def get_by_camera(self, pk):
        return self.filter(camera=pk)

    def get_latest_by_camera(self, pk):
        return self.filter(camera=pk).order_by('-service_data')

    def get_new_by_camera(self, pk):
        return self.filter(camera=pk).order_by('service_data')

    def get_not_served(self):
        return self.filter(service_data__lte=datetime.date.today())
