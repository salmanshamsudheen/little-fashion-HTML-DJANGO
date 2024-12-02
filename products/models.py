from django.db import models
from django.utils.translation import gettext_lazy as _                    # _ in verbose


class Product(models.Model):
    image = models.ImageField(upload_to='media')
    name = models.CharField(max_length=250)
    description = models.TextField()
    price = models.CharField(max_length=250, null=True, blank=True)
    created_date = models.DateField(null=True, blank=True)
    is_popular = models.BooleanField(default=False)
    is_trending = models.BooleanField(default=False)
    new_arrival = models.BooleanField(default=False)
    discounted_price = models.BooleanField(default=False)
    order_id = models.PositiveIntegerField(blank=True, null=True)
    
    class Meta:
        db_table = 'fasion_product'
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
        ordering = ('-id', )
    
    def __str__(self):
        return f"{self.name}"