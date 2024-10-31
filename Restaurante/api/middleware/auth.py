from  django.utils.deprecation import MiddlewareMixin
from rest_framework.exceptions import PermissionDenied;

class AdminRequiredMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Asegúrate de que el usuario esté autenticado
        if request.user.is_authenticated and not request.user.is_staff:
            raise PermissionDenied("Acceso Denegado")
