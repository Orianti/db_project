class CameraManager(models.Manager):
    def get_camera(self, camera_id):
        try:
            q = self.get(pk=camera_id)
        except self.DoesNotExist:
            q = None

        return q

    def get_problem(self):
        return self.exclude(state__state='OK')

    def get_error(self):
        return self.filter(state__state='ERROR')

    def get_warning(self):
        return self.filter(state__state='WARNING')

    def get_failure(self):
        return self.filter(state__state='FAILURE')

    def filter_pk(self, pk):
        return self.filter(pk__in=pk)
