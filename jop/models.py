from django.db import models
from django_countries.fields import CountryField
from django.utils import timezone



JOP_TYPE = [
    ('FullTime', 'Full Time'),
    ('Remote', 'Remote'),
    ('Freelance', 'Freelance'),
    ('PartTime', 'Part Time'),
]
# Create your models here.



class Job(models.Model):
    title = models.CharField(max_length=120)
    location = CountryField()
    company = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='jop_company')
    created_at = models.DateTimeField(default=timezone.now)
    salary_start = models.IntegerField(null=True, blank=True)
    salary_end = models.IntegerField(null=True, blank=True)
    description = models.TextField(max_length=15000)
    vacancy = models.IntegerField()
    jop_type = models.CharField(choices=JOP_TYPE, max_length=10)
    experience = models.IntegerField()
    category = models.ForeignKey('Category', related_name='job_category', on_delete= models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title






class Category(models.Model):
    name = models.CharField(max_length=30)
    logo = models.CharField(max_length=30)
    def __str__(self):
        return self.name










class Company(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='company')
    subtitle = models.TextField(max_length=1000)
    website = models.URLField(max_length=200)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.name


