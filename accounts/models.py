from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid


class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField()
    password = models.CharField(max_length=128)
    
    class Meta:
        db_table = 'fasion_profile'
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')
        ordering = ('-id', )
    
    def __str__(self):
        return f"{self.email}"

