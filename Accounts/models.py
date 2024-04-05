from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_admin = models.BooleanField('Is admin', default=False)
    is_cr = models.BooleanField('Is cr', default=False)
    is_student = models.BooleanField('Is student', default=True)

    middle_name = models.CharField('Middle name', max_length=255, null=True)
    registration_number = models.CharField('Registration number', max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    
   


    # Set custom related names for permissions and groups
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='custom_user_permissions',
        related_query_name='user',
    )
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='custom_user_groups',
        related_query_name='user',
    )
