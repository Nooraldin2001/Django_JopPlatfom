from django import forms
from .models import JobApply, Job
from django.core.validators import FileExtensionValidator
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget






class JobApplyForm(forms.ModelForm):
    cv = forms.FileField(
        label='CV',
        widget=forms.ClearableFileInput(attrs={'accept': '.pdf'}),
        validators=[FileExtensionValidator(allowed_extensions=['pdf'], message='Only PDF files are allowed.')]
    )
    class Meta:
        model = JobApply
        fields = ['username', 'email', 'linkedIn_url', 'githup_url', 'cv', 'cover_letter']
       

class JobForm(forms.ModelForm):
    description = forms.CharField(widget=SummernoteWidget())
    class Meta:
        model = Job
        fields = ['title', 'location', 'company', 'salary_start', 'salary_end', 'description', 'vacancy', 'job_type', 'experience', 'category']

        