from django.contrib.auth.decorators import permission_required
from django.urls import path
from app import views

urlpatterns = [
    path('', views.AppLoginView.as_view(), name='login'),
    path('logout', views.AppLogoutView.as_view(), name='logout'),

    path('editing', permission_required('app.add_camera')(views.CameraCreateView.as_view()), name='camera_list'),
    path('editing/delete/<int:pk>', permission_required('app.add_camera')(views.CameraDeleteView.as_view()),
         name='delete_camera'),
    path('editing/update/<int:pk>', permission_required('app.add_camera')(views.CameraUpdateView.as_view()),
         name='update_camera'),

    path('audit', permission_required('app.add_camera')(views.ServiceCreateView.as_view()), name='audit_camera'),
    path('audit/services/<int:camera>', permission_required('app.add_camera')(views.ServiceListView.as_view()),
         name='camera_services'),
    path('audit/detail/<int:pk>', permission_required('app.add_camera')(views.AuditDetailView.as_view()),
         name='audit_detail'),

    path('service-organizations', views.ServiceOrganizationCreateView.as_view(), name='service_org_list'),
    path('service-organizations/update/<int:pk>', views.ServiceOrganizationUpdateView.as_view(),
         name='service_org_update'),
    path('service-organizations/delete/<int:pk>', views.ServiceOrganizationDeleteView.as_view(),
         name='service_org_delete'),
]
