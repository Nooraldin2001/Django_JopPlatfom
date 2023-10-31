from django.contrib import admin
from .models import Category, Job, Company
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.

class JobAdmin(SummernoteModelAdmin):
    list_display = ['title','location','company','job_type','vacancy', 'category']
    search_fields = ['title', 'category', 'description']
    list_filter = ['job_type','vacancy','category', 'experience']
    summernote_fields = '__all__'
admin.site.register(Job, JobAdmin)
admin.site.register(Company)
admin.site.register(Category)