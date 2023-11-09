from django.db import models
from autoslug import AutoSlugField



class Post(models.Model):
    title = models.CharField(max_length=120)
    summary = models.CharField(max_length=155)
    desing = models.CharField(max_length=120)
    services = models.CharField(max_length=120)
    team = models.CharField(max_length=120)
    content = models.TextField()
    process = models.TextField()
    result = models.TextField()
    date = models.DateField(auto_now_add=True)
    oneimage = models.ImageField(upload_to='news_images/', default='default_image.jpg')
    twoimage = models.ImageField(upload_to='news_images/', default='default_image.jpg')
    threeimage = models.ImageField(upload_to='news_images/', default='default_image.jpg')
    fourimage = models.ImageField(upload_to='news_images/', default='default_image.jpg')
    slug = AutoSlugField(populate_from='title', unique=True, editable=True, blank=True)


    class Meta:
        db_table = 'Post'
        verbose_name = 'Post'
        verbose_name_plural = 'Post'

    def __str__(self):
        return self.title




class Contact(models.Model):
    name_surname = models.CharField(max_length=120)
    email = models.EmailField(max_length=120)
    mesaj = models.TextField()



    class Meta:
        db_table = 'Contact'
        verbose_name = 'İletişim'
        verbose_name_plural = 'İletişim'

    def __str__(self):
        return self.name_surname