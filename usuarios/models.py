from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.core import validators
from django.core.validators import RegexValidator, validate_email
from django.urls import reverse


class MyUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None, **kwargs):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            **kwargs
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
            **extra_fields
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Rol(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.nombre)


class User(AbstractBaseUser):
    username = models.CharField(('username'), max_length=200, unique=True, blank=False, validators=[
        RegexValidator(
            regex='^[a-z0-9_-]*$',
            message='Usernames can only contain letters, numbers, underscores, and dashes.'
        )
    ])
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        validators=[validators.validate_email]
    )

    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'date_of_birth']

    def __str__(self):
        return '{} {}'.format(self.username, self.email)

    def get_absolute_url(self):
        return reverse('modificarusuario', kwargs={'pk': self.pk})

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


#class RolUsuario(models.Model):
#   rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
 #   usuario = models.ForeignKey(User, on_delete=models.CASCADE)
#
 #   def __str__(self):
  #      return self.rol_id,

class RolUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    class Meta:
        db_table = "rolusuario"
        verbose_name = "rolusuario"
        verbose_name_plural = "rolusuarios"
    def __str__(self):
        return self.rol_id
