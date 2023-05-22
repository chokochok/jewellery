from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', related_name='userprofile', on_delete=models.CASCADE)
    is_vendor = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} Profile'
