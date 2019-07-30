from django.db import models

# Create your

from django.conf import settings

User = settings.AUTH_USER_MODEL

class Post(models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='images', null=True)
    slug = models.SlugField(unique=True)
    like = models.SmallIntegerField(default=0)
    dislike = models.SmallIntegerField(default=0)
    users_reaction = models.ManyToManyField(User, blank=True, verbose_name='Реакция юзеров', related_name='react')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/{}/'.format(self.slug)

    def get_edit_url(self):
        return '/{}/update'.format(self.slug)

    def delete_post(self):
        return '/{}/delete'.format(self.slug)


class Author(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    email = models.EmailField()
    phone = models.IntegerField()

    def __str__(self):
        return self.user.username