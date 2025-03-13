from django.contrib import admin
from .models import Record

# Register your models here.
class RecordAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email')


admin.site.register(Record,RecordAdmin)
