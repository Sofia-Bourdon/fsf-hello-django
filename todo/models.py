from django.db import models

# Create your models here.
class item(models.Model):
    name = models.Charfield(max_lengh=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)
