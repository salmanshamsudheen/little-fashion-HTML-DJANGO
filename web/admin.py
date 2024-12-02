from django.contrib import admin
from .models import Spotlight, Contact, CustomerReview


class SpotlightAdmin(admin.ModelAdmin):
    list_display = ('title', )
    search_fields = ('title', )
    
admin.site.register(Spotlight, SpotlightAdmin)  


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)  

admin.site.register(Contact, ContactAdmin)

class CustomerReviewAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(CustomerReview, CustomerReviewAdmin)    

