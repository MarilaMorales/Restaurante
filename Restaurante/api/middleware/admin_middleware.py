from django.http import JsonResponse

def admin_middleware(get_response):
    def middleware(request):
        # Verificamos si el usuario está autenticado y es un administrador
        if request.user.is_authenticated and request.user.is_staff:
            return get_response(request)
        
        # Si no es un administrador, devolvemos un error
        return JsonResponse({'error': 'No tienes permiso para acceder a esta ruta.'}, status=403)

    return middleware
