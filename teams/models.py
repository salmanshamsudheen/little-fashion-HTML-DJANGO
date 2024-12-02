from django.db import models
from django.utils.translation import gettext_lazy as _                    # _ in verbose


class TeamMember(models.Model):
    image = models.ImageField(upload_to='media')
    name = models.CharField(max_length=250)
    role = models.CharField(max_length=250)
    order_id = models.PositiveIntegerField(blank=True, null=True)
    
    class Meta:
        db_table = 'fasion_team_member'
        verbose_name = _('Team Member')
        verbose_name_plural = _('Team Members')
        ordering = ('-id', )
    
    def __str__(self):
        return f"{self.name}"
    
    