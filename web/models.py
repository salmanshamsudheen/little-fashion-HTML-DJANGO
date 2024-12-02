from django.db import models
from django.utils.translation import gettext_lazy as _                    # _ in verbose


class Spotlight(models.Model):
    image = models.ImageField(upload_to='media')
    title = models.CharField(max_length=250)
    description = models.TextField()
    reference = models.CharField(max_length=255, null=True, blank=True)
    reference_description = models.TextField()
    order_id = models.PositiveIntegerField(blank=True, null=True)
    
    class Meta:
        db_table = 'fasion_spotlight'
        verbose_name = _('Spotlight')
        verbose_name_plural = _('Spotlights')
        ordering = ('-id', )
    
    def __str__(self):
        return f"{self.title}"


class Contact(models.Model):
    name = models.CharField(max_length=225)
    email = models.EmailField()
    subject = models.TextField()
    detail = models.TextField()
    
    class Meta:
        db_table = 'fasion_contact'
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')
        ordering = ('-id', )
    
    def __str__(self):
        return f"{self.name}"
 
 
class CustomerReview(models.Model):
    name = models.CharField(max_length=225)
    type = models.CharField(max_length=225)
    description = models.TextField()
    image = models.ImageField(upload_to='media', blank=True,)
    
    class Meta:
        db_table = 'fasion_customer_review'
        verbose_name = ('Customer Review')
        verbose_name_plural = ('Customer Reviews')
        ordering = ('-id',)
        
    def __str__(self):
        return f"{self.name}"       