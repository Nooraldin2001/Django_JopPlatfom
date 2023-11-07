from django import forms
from .models import JobApply
from django.core.validators import FileExtensionValidator





class JobApplyForm(forms.ModelForm):
    cv = forms.FileField(
        label='CV',
        widget=forms.ClearableFileInput(attrs={'accept': '.pdf'}),
        validators=[FileExtensionValidator(allowed_extensions=['pdf'], message='Only PDF files are allowed.')]
    )
    class Meta:
        model = JobApply
        fields = ['username', 'email', 'linkedIn_url', 'githup_url', 'cv', 'cover_letter']
       