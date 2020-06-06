from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import ServiceForm, CameraForm, AuthUserForm, ServiceOrganizationForm
from .models import Camera, Service, ServiceOrganization


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


class ServiceListReverseView(ListView):
    model = Service
    template_name = 'app/services.html'
    context_object_name = 'services'

    camera = None

    def get_queryset(self):
        self.camera = get_object_or_404(Camera, pk=self.kwargs['camera'])
        return Service.objects.get_new_by_camera(self.camera)

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
    success_url = reverse_lazy('audit_camera')

    def get_context_data(self, **kwargs):
        kwargs['cameras'] = Camera.objects.get_problem().order_by('-state__state')
        return super().get_context_data(**kwargs)


class ServiceCreateReverseView(CreateView):
    model = Service
    template_name = 'app/audit.html'
    form_class = ServiceForm
    success_url = reverse_lazy('audit_camera')

    def get_context_data(self, **kwargs):
        kwargs['cameras'] = Camera.objects.get_problem().order_by('state__state')
        return super().get_context_data(**kwargs)


class CameraCreateView(CreateView):
    model = Camera
    template_name = 'app/editing.html'
    form_class = CameraForm
    success_url = reverse_lazy('camera_list')

    def get_context_data(self, **kwargs):
        kwargs['cameras'] = Camera.objects.all()
        return super().get_context_data(**kwargs)


class CameraUpdateView(UpdateView):
    model = Camera
    template_name = 'app/editing.html'
    form_class = CameraForm
    success_url = reverse_lazy('camera_list')

    def get_context_data(self, **kwargs):
        kwargs['update'] = True
        kwargs['cameras'] = Camera.objects.all()
        return super().get_context_data(**kwargs)


class CameraDeleteView(DeleteView):
    model = Camera
    template_name = 'app/editing.html'
    success_url = reverse_lazy('camera_list')


class AppLoginView(LoginView):
    template_name = 'app/login.html'
    form_class = AuthUserForm

    def get_success_url(self):
        return reverse_lazy('login')


class AppLogoutView(LogoutView):
    next_page = reverse_lazy('login')


class ServiceOrganizationCreateView(CreateView):
    model = ServiceOrganization
    template_name = 'app/contracts.html'
    form_class = ServiceOrganizationForm
    success_url = reverse_lazy('service_org_list')

    def get_context_data(self, **kwargs):
        kwargs['service_organizations'] = ServiceOrganization.objects.all()
        return super().get_context_data(**kwargs)


class ServiceOrganizationUpdateView(UpdateView):
    model = ServiceOrganization
    template_name = 'app/contracts.html'
    form_class = ServiceOrganizationForm
    success_url = reverse_lazy('service_org_list')

    def get_context_data(self, **kwargs):
        kwargs['update'] = True
        kwargs['service_organizations'] = ServiceOrganization.objects.all()
        return super().get_context_data(**kwargs)


class ServiceOrganizationDeleteView(DeleteView):
    model = ServiceOrganization
    template_name = 'app/contracts.html'
    success_url = reverse_lazy('service_org_list')
