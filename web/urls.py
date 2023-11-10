from django.urls import path
from .views import homepage,projects_details, Contact
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', homepage, name='homepage'),
    path('projects-detail/<slug>/', projects_details, name='projects_details'),
    path('contact/', Contact, name='contact')
 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

