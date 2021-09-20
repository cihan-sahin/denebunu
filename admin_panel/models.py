from django.db import models
from django.utils import timezone

# Create your models here.
class PressContent(models.Model):
    label = models.TextField('label',max_length=50)
    url = models.TextField('url')
    date = models.DateTimeField('date_published',default=timezone.now)
    created = models.DateTimeField('date_created',default = timezone.now)
    modified = models.DateTimeField('date_updated', auto_now=True)

    def __str__(self):
        return self.url