from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Meta:
        app_label = 'accounts'

    # Add custom related_name to avoid clashes with the default auth.User model
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='accounts_user_set',  # Custom related name for groups
        blank=True
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='accounts_user_permissions_set',  # Custom related name for user_permissions
        blank=True
    )