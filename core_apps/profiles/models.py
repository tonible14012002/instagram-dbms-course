from django.db import models
from core_apps.common.models import TimeStampedModel
from django_countries.fields import CountryField
from django.conf import settings


# Create your models here.
class Profile(TimeStampedModel):

    class GENDER(models.TextChoices):
        MALE = ('MALE', 'Male')
        FEMALE = ('FEMALE', 'Female')
        OTHER = ('OTHER', 'Other')

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(default='/default-avatar.png')
    gender = models.CharField(choices=GENDER.choices, max_length=20, default=GENDER.OTHER)
    country = CountryField(null=False, default="VN")
    followers = models.ManyToManyField("self", related_name='following', symmetrical=False)
    city = models.CharField(max_length=200, default="Ho Chi Minh")
    _nickname = models.CharField(max_length=100, default='', unique=True)

    class Meta:
        db_table = "profile"

    def follow(self, profile):
        self.followers.add(profile)

    def unfollow(self, profile):
        self.followers.remove(profile)

    def check_is_follow(self, profile):
        return self.followers.filter(pkid=profile.pkid).exists()

    @property
    def nickname(self):
        return self._nickname

    @nickname.getter
    def nickname(self):
        if not self._nickname:
            return self.user.username
        return self._nickname

    @nickname.setter
    def nickname(self, value):
        self._nickname = value