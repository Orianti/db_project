from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .forms import ServiceForm

from .models import Camera, Service


class CameraListView(ListView):
    model = Camera
    template_name = 'app/editing.html'
    context_object_name = 'cameras'


class CameraDetailView(DetailView):
    model = Camera
    template_name = 'app/detail.html'
    context_object_name = 'camera'


class CameraStateListView(ListView):
    model = Camera
    template_name = 'app/audit.html'
    context_object_name = 'cameras'


class ServiceListView(ListView):
    model = Service
    template_name = 'app/services.html'
    context_object_name = 'services'

    camera = None

    def get_queryset(self):
        self.camera = get_object_or_404(Camera, pk=self.kwargs['camera'])
        return Service.objects.get_latest_by_camera(self.camera)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['camera'] = self.camera
        return context


class AuditDetailView(DetailView):
    model = Camera
    template_name = 'app/audit_detail.html'
    context_object_name = 'camera'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['service'] = Service.objects.get_by_camera(pk=self.kwargs['pk'])
        return context


class ServiceCreateView(CreateView):
    model = Service
    template_name = 'app/audit.html'
    form_class = ServiceForm
    success_url = reverse_lazy('/')

    def get_context_data(self, **kwargs):
        kwargs['cameras'] = Camera.objects.all()
        return super().get_context_data(**kwargs)

