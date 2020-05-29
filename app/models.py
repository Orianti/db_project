from django.db import models


class City(models.Model):
    name = models.CharField(max_length=30, verbose_name='название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'город'
        verbose_name_plural = 'города'


class Location(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='город')
    street = models.CharField(max_length=100, verbose_name='улица')
    support = models.IntegerField(verbose_name='номер опоры')
    notes = models.TextField(verbose_name='заметки')

    def __str__(self):
        return f'{self.city}, {self.street}, {self.support}'

    class Meta:
        verbose_name = 'положение'
        verbose_name_plural = 'положения'


class State(models.Model):
    STATES = (
        (0, 'OK'),
        (1, 'WARNING'),
        (2, 'ERROR'),
        (3, 'FAILURE'),
    )

    state = models.IntegerField(choices=STATES, verbose_name='состояние')
    logs = models.TextField(verbose_name='журнал')

    def __str__(self):
        return self.get_state_display()

    class Meta:
        verbose_name = 'состояние'
        verbose_name_plural = 'состояния'


class Producer(models.Model):
    organization = models.CharField(max_length=100, verbose_name='название организации')
    city = models.ManyToManyField(City, verbose_name='город')
    phone = models.CharField(max_length=10, verbose_name='телефон')
    contract_expires = models.DateField(verbose_name='срок действия договора')
    notes = models.TextField(verbose_name='заметки')

    def __str__(self):
        return self.organization

    def get_organization(self):
        return self.organization

    class Meta:
        verbose_name = 'производитель'
        verbose_name_plural = 'производители'


class Specifications(models.Model):
    TYPES = (
        (0, 'Speed'),
        (1, 'AVERAGE_SPEED'),
        (2, 'RED_LIGHT'),
        (3, 'DOUBLE_WHITE_LINE'),
        (4, 'BUS_LANE'),
        (5, 'TOLLBOOTH'),
        (6, 'LEVEL_CROSSING'),
        (7, 'CONGESTION_CHARGE'),
    )

    type = models.IntegerField(choices=TYPES, verbose_name='тип')
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE, verbose_name='производитель')
    date_of_manufacture = models.DateField(verbose_name='дата производства')
    service_frequency = models.IntegerField(verbose_name='частота сервисного обслуживания')
    notes = models.TextField(verbose_name='заметки')

    def __str__(self):
        return f'{self.get_type_display() ({self.producer.get_organization()})}'

    class Meta:
        verbose_name = 'спецификация'
        verbose_name_plural = 'спецификации'


class Camera(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, verbose_name='местоположение')
    specifications = models.OneToOneField(Specifications, on_delete=models.CASCADE, verbose_name='спецификации')
    state = models.ForeignKey(State, on_delete=models.CASCADE, verbose_name='состояние')

    def __str__(self):
        return f'камера №{self.id}'

    class Meta:
        verbose_name = 'камера'
        verbose_name_plural = 'камеры'


class ServiceOrganization(models.Model):
    organization = models.CharField(max_length=100, verbose_name='название организации')
    city = models.ManyToManyField(City, verbose_name='город')
    phone = models.CharField(max_length=10, verbose_name='телефон')
    contract_expires = models.DateField(verbose_name='срок действия договора')
    notes = models.TextField(verbose_name='заметки')

    def __str__(self):
        return self.organization

    class Meta:
        verbose_name = 'сервисная организация'
        verbose_name_plural = 'сервисные организации'


class Service(models.Model):
    camera = models.ForeignKey(Camera, on_delete=models.CASCADE, verbose_name='ID камеры')
    service_organization = models.ForeignKey(ServiceOrganization, on_delete=models.CASCADE,
                                             verbose_name='сервисная организация')
    service_data = models.DateField(verbose_name='дата сервис')
    info = models.TextField(verbose_name='информация')

    def __str__(self):
        return f'сервис №{self.id}'

    class Meta:
        verbose_name = 'сервис'
        verbose_name_plural = 'сервисы'
