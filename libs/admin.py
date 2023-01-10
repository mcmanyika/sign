from django.contrib import admin
from .models import *

# Register your models here.
class SignModelAdmin(admin.ModelAdmin):
	list_display = ['title', 'dateFrom', 'dateTo']
	class Meta:
		model = t_sign
admin.site.register(t_sign, SignModelAdmin)