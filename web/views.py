from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Contact
from .forms import ContactForms
from django.contrib import messages

def homepage(request):
    postlar = Post.objects.all()
    return render(request, 'pages/homepage.html',{
        'postlar': postlar,
    })





def post_details(request, slug):
    post = get_object_or_404(Post, slug=slug)
    postlar = Post.objects.all()
    return render(request, 'pages/post.html',{
        'post': post,
        'postlar': postlar
    })




def Contact(request):
    if request.method == 'POST':
        form = ContactForms(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            messages.success(request, 'Mesajınız Gönderilmiştir')
            return redirect('contact',)
    else:
        form = ContactForms()
    return render(request, 'pages/contact.html', {
        'form': form
    })

