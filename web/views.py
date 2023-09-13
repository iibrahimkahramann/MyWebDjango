from django.shortcuts import render, get_object_or_404
from .models import Post
def homepage(request):
    return render(request, 'pages/homepage.html')



def project(request,):
    postlar = Post.objects.all()
    return render(request, 'pages/project.html', {
        'postlar': postlar,
    })
