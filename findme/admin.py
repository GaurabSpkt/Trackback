from django.contrib import admin
from .models import ItemLost
from .models import Contact
# Register your models here.
admin.site.register(ItemLost)
admin.site.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'submitted_at')
    search_fields = ('name', 'email')