from email.utils import formataddr
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from signals.libs.models import AuditedModel, PersistentModel

from django.db.models.signals import post_save
from django.dispatch import receiver
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='/tmp/signals.log',
                    filemode='w')
logger = logging.getLogger(__name__)

class CompanyModel(AuditedModel):
    """
        Abstract model with basic info of a company
    """
    name = models.CharField(max_length=64, db_index=True, verbose_name='Name', null=True, blank=True)

    class Meta:
        abstract = True

    @property
    def full_name(self):
        if self.name:
            return self.name
        return ""

    def __str__(self):
        return self.full_name

    def clean(self):
        # Strip whitespaces
        fields = ['name']
        for field in fields:
            value = getattr(self, field, None)
            if value:
                setattr(self, field, value.strip())

class PersonModel(AuditedModel):
    """
        Abstract model with basic info of a person type user
    """
    # Basic info, location
    name = models.CharField(max_length=64, db_index=True, verbose_name='Name', null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class Person(PersonModel):
    """
        Model of a Person
    """
    # Link with user
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, blank=True, related_name='%(class)s_user')
    last_name = models.CharField(max_length=64, verbose_name='Name', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'persons'

    @property
    def full_name(self):
        return "{} {}".format(self.name or "", self.last_name or "").strip()

    def __str__(self):
        return self.full_name

class Company(CompanyModel,PersistentModel):
    """
        Model of a company
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, blank=True, related_name='%(class)s_user')

    class Meta:
        verbose_name_plural = 'companies'


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def user_create_profile(sender, instance, created, **kwargs):
    """
        Depending of user_type on the User model, we want to create
        a specific "type of profile"
    """
    logger.info('[entities receiver]')
    if created:
        # Here we will put the logic of which type of user we will create.
        # Will be dicted by the type of user, given by the user_type field.
        logger.info('[entities receiver created]')
        if instance.user_type == 1:
            Person.objects.create(user=instance)
        elif instance.user_type == 2:
            Company.objects.create(user=instance)
        else:
            pass
