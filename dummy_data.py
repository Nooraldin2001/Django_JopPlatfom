#django setup code 
import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

import random
from job.models import Category, Company, Job
from faker import Faker

def creat_category(n):
    fake = Faker()
    for x in range(n):
        Category.objects.create(
            name = fake.name()
        )
    print(f"{n} category was added successfully")

def creat_company(n):
    fake = Faker() 
    images = ['job-list1.png', 'job-list2.png', 'job-list3.png', 'job-list4.png',]
    for x in range(n):
        Company.objects.create(
            name = fake.company(),
            website = fake.url(),
            subtitle = fake.text(),
            email = fake.email(),
            logo = f"company/{images[random.randint(0,3)]}"
        )
    print(f"{n} Company was added successfully")

def creat_job(n):
    fake = Faker()
    job_TYPE = ['FullTime','Remote', 'Freelance','Part Time']


    for x in range(n):
        Job.objects.create(
            title        = fake.name(),
            #location     = fake.sentence(),
            company      = Company.objects.all().order_by('?')[0],
            salary_start = random.randint(2000,2500),
            salary_end   = random.randint(2300,2800),
            description  = fake.sentence(),
            vacancy      = random.randint(2,5),
            job_type     = job_TYPE[random.randint(0,3)],
            experience   = random.randint(1,10),
            category     = Category.objects.all().order_by('?')[0],
        )
    print(f"{n} job was added successfully")

#creat_category()
creat_company(100)
creat_job(2000)