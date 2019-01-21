from django.db import models
from django.contrib.auth.models import User

# Create your models here.


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.owner.id, filename)


class Post(models.Model):
    owner = models.ForeignKey('auth.User', related_name='post', on_delete=models.CASCADE)
    picture = models.FileField(upload_to=user_directory_path)
    text = models.CharField(max_length=1000, blank=True, default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def count_licks(self):
        sum_licks = len(self.licks.all())
        return sum_licks

    def __str__(self):
        return"{}".format(self.text)


class Lick(models.Model):
    post = models.ForeignKey('Post', related_name='licks', on_delete=models.CASCADE)
    licked_by = models.ForeignKey('auth.User', related_name='licks', on_delete=models.CASCADE)


