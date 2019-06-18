from django.db import models

# Create your

from django.conf import settings

User = settings.AUTH_USER_MODEL

class Post(models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    phone = models.IntegerField()

    def __str__(self):
        return self.user.username