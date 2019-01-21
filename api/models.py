from django.db import models
# Django best practices are to use get_user_model, not the User model directly
# TL;DR is that importing User can bypass additional modifications to the User model from middleware etc
from django.contrib.auth import get_user_model

# Create your models here.


def user_directory_path(instance, filename):
    # This is the 'correct' way to do string interpolation in python < 3.7
    # but in python 3.7, we have F-STRINGS :D :D :D *cheers*
    # I'll edit this line to show you how to do it with an f-string
    return f"user_{instance.owner.id}/{filename}"


class Post(models.Model):
    # one thing to note here - the first argument to ForeignKey can be the model class directly.
    # the string name of the class is a good idea in many cases though, because it avoids
    # the DREADED circular import error
    owner = models.ForeignKey(get_user_model(), related_name='post', on_delete=models.CASCADE)
    picture = models.FileField(upload_to=user_directory_path)
    # I'm surprised this doesn't throw an error - `True` is a boolean type, but it's a charfield
    # so it should expect a string as the default. That's because the default kwarg to any model
    # field should be the literal value to be used as a default. I think there's a way to
    # use a callable too, but I don't know it off the top of my head
    text = models.CharField(max_length=1000, blank=True, default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def count_licks(self):
        # I believe this could be simplified to:
        sum_licks = self.licks.count()
        # and then the count should be done in the database - much faster!
        # This is what I was hoping you'd discover on your own by researching Managers :p
        return sum_licks

    def __str__(self):
        # self.text is a string. Why not just return it directly
        return"{}".format(self.text)


class Lick(models.Model):
    # Heeheehee Licks :3
    post = models.ForeignKey('Post', related_name='licks', on_delete=models.CASCADE)
    licked_by = models.ForeignKey('auth.User', related_name='licks', on_delete=models.CASCADE)
