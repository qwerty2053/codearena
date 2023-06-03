import uuid

from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import FileExtensionValidator
from django.db import models


def generate_image_path(instance, filename):
    ext = filename.split('.')[-1]
    return f"media/avatars/{uuid.uuid4()}.{ext}"


class User(AbstractBaseUser):
    email = models.EmailField("Почта", max_length=70, unique=True)
    nickname = models.CharField("Никнейм", max_length=70, unique=True)
    avatar = models.ImageField("Аватар", upload_to=generate_image_path, null=True, blank=True, validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])])
    first_name = models.CharField("Имя", max_length=70, null=True, blank=True)
    last_name = models.CharField('Фамилия', max_length=70, null=True, blank=True)
    bio = models.TextField("Обо мне", null=True, blank=True, max_length=512)
    problems_solved = models.PositiveIntegerField(default=0, verbose_name='Решено задач')
    rating = models.PositiveIntegerField(default=0, verbose_name='Рейтинг')
    # country = models.ForeignKey(Country)
    date_joined = models.DateTimeField(auto_now_add=True)
    birthdate = models.DateField(null=True, blank=True)
    github = models.CharField(max_length=32, null=True, blank=True)
    show_email = models.BooleanField(default=False)

    is_active = models.BooleanField("Активный", default=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # TO DO: sign in with nickname or email
    # Now just with nickname
    USERNAME_FIELD = 'nickname'
    REQUIRED_FIELDS = ['nickname', 'email']

    def __str__(self):
        return  self.nickname

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
