from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class UserManager(BaseUserManager):
    def _create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('User must have and email address')

        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_admin') is not True:
            raise ValueError('Superuser must have is_admin=True.')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='이메일 주소', max_length=255, unique=True)
    username = models.CharField('이름', max_length=30)
    english_name = models.CharField('영문이름', max_length=50, null=True, blank=True)
    birth_day = models.DateField('생년월일', null=True, blank=True)
    resident_registration_number = models.CharField(max_length=7)
    phone = models.CharField('휴대폰 번호', max_length=20)

    home_address = models.CharField('집 주소', max_length=100, null=True, blank=True)
    home_phone = models.CharField('집 전화번호', max_length=50, null=True, blank=True)

    company_name = models.CharField('회사 이름', max_length=30, null=True, blank=True)
    company_address = models.CharField('회사 주소', max_length=50, null=True, blank=True)
    company_phone = models.CharField('회사 전화번호', max_length=50, null=True, blank=True)

    is_active = models.BooleanField(verbose_name='계정 활성화 여부', default=True)
    is_admin = models.BooleanField(verbose_name='관리자', default=False)
    is_superuser = models.BooleanField(verbose_name='superuser 권한', default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = '사용자'
        verbose_name_plural = '사용자'

    def __str__(self):
        return f'{self.username}'

    @property
    def is_staff(self):
        return self.is_superuser

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser
