from django.db import models
# Base of django standard user model
from django.contrib.auth.models import AbstractBaseUser
# Allows for addition of users
from django.contrib.auth.models import PermissionsMixin
# User model manager for teaching django how to use profile model
from django.contrib.auth.models import BaseUserManager

# Create your models here.

class UserProfileManager(BaseUserManager):
    """Helps Django work with custom user model."""

    def create_user(self, email, name, password=None):
        """Creates a new user profile."""

        if not email:
            raise ValueError('Users must have an email address.')

        email = self.normalize_email(email)
        # New user profile object
        user = self.model(email=email, name=name)

        # Set and encrypt password
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Creates and saves a new superuser with given details."""

        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user



class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
    Represents a 'user profile' inside the system.
    Stores all user account related data, such as 'email address' and 'name'
    """

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Django uses this when it needs to get the user's full name."""

        return self.name

    def get_short_name(self):
        """Django uses this when it needs to get the users abbreviated name."""

        return self.name

    def __str__(self):
        """Django uses this when it needs to convert the object to text."""

        return self.email
