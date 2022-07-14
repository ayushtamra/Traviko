from pyexpat import model
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(
        'username',
        max_length=50,
        unique=True,
        help_text='Required. 50 characters or fewer. Letters, digits and @/./+/-/_ only.',
        error_messages={
            'unique': "A user with that username already exists.",
        },
    )
    email = models.EmailField(unique=True, blank=False,
                              error_messages={
                                  'unique': "A user with that email already exists.",
                              })
    status = models.BooleanField(default=False)
    about = models.TextField(blank=True)

    # Required for prediction
    gender = models.CharField(max_length=20)
    education = models.CharField(max_length=20)
    residence = models.CharField(max_length=20)
    age = models.IntegerField

    citySearched = models.CharField(max_length=20)

 

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "gender"]

    def __unicode__(self):
        return self.email

    def __str__(self):
        return self.get_full_name()
