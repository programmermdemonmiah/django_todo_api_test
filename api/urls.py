from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import get_user, create_user


urlpatterns = [
    path('users/', get_user , name='get_user'),
    path('create_user', create_user, name='create_user')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)