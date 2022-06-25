from django.urls import path, include
from .views import*
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name=('home')),
    path('add', add_emp, name=('add_emp')),
    path('view', view_all, name=('view_emp')),
    path('remove', remove_emp, name=('remove_emp')),
    path('details', details_emp, name=('details_emp')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
