from django.http import JsonResponse
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.urls import reverse


class JWTAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not self.is_login_or_register_route(request):
            auth = JWTAuthentication()
            user, token = auth.authenticate(request)

            if user is not None:
                request.user = user
            else:
                request.user = None

                # Return unauthenticated response
                return JsonResponse({"message": "User is unauthenticated"}, status=401)

            response = self.get_response(request)
            return response

    def is_login_or_register_route(self, request):
        return request.path == reverse('login') or request.path == reverse('register')
