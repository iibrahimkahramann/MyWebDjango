from django.urls import path
from .views import homepage, project


urlpatterns = [
    path('', homepage, name='homepage'),
    path('project/', project, name='project')
 ]
