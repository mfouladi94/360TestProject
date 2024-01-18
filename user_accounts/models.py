from django.core import validators
from django.db import models
from django.db.models import CASCADE
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# utils method
import random
import string


def generate_random_referral(length=6):
    """Generate a random string of the specified length."""
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))


# Create your models here
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    mobile_number = models.BigIntegerField(_('mobile number'), null=True, blank=True,
                                           validators=[validators.RegexValidator(r'^989[0-3,9]\d{8}$',
                                                                                 _('Enter a valid mobile number'))])
    description = models.CharField(_("description"), max_length=255, blank=True)
    location = models.CharField(_("location"), max_length=255, blank=True)
    last_seen = models.DateTimeField(_("last seen"), default=timezone.now)
    is_banned = models.BooleanField(_("banned"), default=False)

    is_vip = models.BooleanField(_("vip"), default=False)
    is_kyc_l1_done = models.BooleanField(_("KYC 1"), default=False)
    is_kyc_l2_done = models.BooleanField(_("KYC 2"), default=False)

    irr_balance = models.FloatField(default=0)
    total_balance = models.FloatField(default=0)
    freeze_balance = models.FloatField(default=0)

    referral_code = models.CharField(max_length=50, default=generate_random_referral, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('profile')
        verbose_name_plural = _("profiles")

    def __str__(self):
        return f" name: {self.user.first_name} , family: {self.user.last_name} , mail : {self.user.email}, joined : {self.date_joined} "

    def __unicode__(self):
        return self.user.username
