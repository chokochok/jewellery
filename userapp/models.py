from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', related_name='userprofile', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'
