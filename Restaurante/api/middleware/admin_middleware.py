# from django.http import JsonResponse
# from django.contrib.auth.models import User


# def admin_middleware(get_response):
#     def middleware(request):
#         # Verificamos si el usuario está autenticado
#         if request.User.is_authenticated:
#             # Verificamos si el rol del usuario es 'admin'
#             if request.User.rol == 'admin':
#                 return get_response(request)

#         # Si no es un administrador, devolvemos un error
#         return JsonResponse({'error': 'No tienes permiso para acceder a esta ruta.'}, status=403)

#     return middleware
