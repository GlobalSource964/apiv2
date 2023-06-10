# permissions.py
from rest_framework import permissions
from django.conf import settings


class ApiKeyPermission(permissions.BasePermission):
    """
    Eğer API key doğruysa tüm ilanları döndürmeye izin verir, yanlışsa sadece istek yapan domainle eşleşen ilanları döndürür
    """

    def has_permission(self, request, view):
        # API anahtarını al
        api_key = request.META.get('HTTP_AUTHORIZATION', '').split(' ')[-1]

        # Anahtar doğruysa tüm ilanları döndürmeye izin ver
        if api_key == settings.API_KEY:
            return True

        # Anahtar yanlışsa sadece istek yapan domainle eşleşen ilanları döndürmeye izin ver
        return True
