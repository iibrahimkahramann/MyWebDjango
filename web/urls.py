from django.urls import path
from .views import homepage, project,post_details


urlpatterns = [
    path('', homepage, name='homepage'),
    path('project/', project, name='project'),
    path('post/<slug>/', post_details, name='post_details')
 ]
