class AuditDetailView(DetailView):
    model = Camera
    template_name = 'app/audit_detail.html'
    context_object_name = 'camera'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['service'] = Service.objects.get_by_camera(pk=self.kwargs['pk'])
        return context


