from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=10000)
    introduction = models.TextField()
    body = models.TextField(blank=True, null=True)
    content = CKEditor5Field(config_name='default', blank=True, null=True )
    images = models.ImageField(blank=True, null=True,default='default.jpg')
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1

            while Blog.objects.filter(slug=slug).exclude(id=self.id).exists():
                slug=f"{base_slug}-{counter}"
                counter +=1

            self.slug = slug

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
