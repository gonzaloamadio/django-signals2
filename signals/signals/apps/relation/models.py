from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

#from tektank.apps.entities.models import Tester
#from tektank.apps.posts.models import Job

class Relation(models.Model):
    tester_id = models.ForeignKey('entities.Person', on_delete=models.CASCADE, verbose_name="Person")
    job_id = models.ForeignKey('related.Job', on_delete=models.CASCADE, verbose_name="Job")

    def __str__(self):
        return self.job_id.title[:32] + ' - ' + self.tester_id.email

