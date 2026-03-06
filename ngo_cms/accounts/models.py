from django.db import models
from django.contrib.auth.hashers import make_password

class User(models.Model):

    ROLE_CHOICES = (
        ('admin','Admin'),
        ('staff','Staff'),
        ('volunteer','Volunteer'),
    )

    STATUS_CHOICES = (
        ('active','Active'),
        ('inactive','Inactive'),
    )

    user_id = models.AutoField(primary_key=True)

    full_name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)

    password_hash = models.CharField(max_length=255)

    role = models.CharField(max_length=50, choices=ROLE_CHOICES)

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.password_hash.startswith('pbkdf2'):
            self.password_hash = make_password(self.password_hash)
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.email