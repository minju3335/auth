from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields