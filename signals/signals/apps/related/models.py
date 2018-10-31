from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

class RelatedModel(models.Model):
    """
        Abstract model with basic info
    """
    title = models.CharField(max_length=128, db_index=True, verbose_name='Name')
    company = models.ForeignKey('entities.Company', on_delete=models.SET_NULL, verbose_name="Company", null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

class Job(RelatedModel):
    """
        Proposals of jobs
        Now we are not adding any new field. But we leave it open
    """
    class Meta:
        verbose_name_plural = 'jobs'
