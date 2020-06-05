from .models import Camera, Service


class NotServicedCamerasController:
    @staticmethod
    def get_cameras_need_service():
        not_serviced_cameras = Service.objects.get_not_served().values()
        not_serviced_cameras_id = [i.get('pk') for i in not_serviced_cameras]
        return Camera.objects.get_problem().filter_pk(not_serviced_cameras_id)
