from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)
    # Ajoutez d'autres champs nécessaires ici

    def __str__(self):
        return self.username

