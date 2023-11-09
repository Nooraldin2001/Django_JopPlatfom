from django.shortcuts import render
from .models import Job, JobApply
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import CreateView
from .forms import JobApplyForm, JobForm
from django.db.models import Q, F
from django.db.models.aggregates import Sum, Min, Max, Count, Avg
#brings the normal get but with error handling 404
from django.shortcuts import get_object_or_404


from django.views.decorators.cache import cache_page


@cache_page(60 * 1)
def mydebug(request):
    # data = Job.objects.filter(experience__lte=5)
    # data = Job.objects.filter(experience__lt=5)
    # data = Job.objects.filter(experience__gt=5)
    # data = Job.objects.filter(experience__gte=5)
    # data = Job.objects.filter(experience__range=(2,4))



    # data = Job.objects.filter(company__id=5)
    # data = Job.objects.filter(company__id__gt=5)

    # data = Job.objects.filter(title__contains='backend')
    # data = Job.objects.filter(title__startswith='a')
    # data = Job.objects.filter(title__endswith='needed')
    # data = Job.objects.filter(salary_start__isnull=True)



    # data = Job.objects.filter(created_at__year=2023)    
    # data = Job.objects.filter(created_at__month=10)    
    # data = Job.objects.filter(created_at__date='2023-10-25')    
    
    
    
    
    # data = Job.objects.filter(salary_start__gt=1000, experience__gt=5)  # and
   
    # data = Job.objects.filter(
    #     Q(salary_start__gt=1000) |
    #     Q(experience__gt=5))  # or
    
    # data = Job.objects.filter(
    #     Q(salary_start__gt=1000) &
    #     Q(experience__gt=5))  # and 
    
    # data = Job.objects.filter(
    #     Q(salary_start__gt=1000) &
    #     ~Q(experience__gt=5))  # not

    # data = Job.objects.filter(salary_start=F('salary_end'))
    
    # data = Job.objects.all().order_by('experience')decs 
    # data = Job.objects.all().order_by('-experience')asce
    # data = Job.objects.order_by('-experience', 'salary_start')
    # data = Job.objects.all().order_by('experience')[0]
    # data = Job.objects.all().earliest('experience')
    # data = Job.objects.all().latest('experience')

    # data = Job.objects.all()[:5]
    # data = Job.objects.all()[5:10]
    
    
    
    # data = Job.objects.values_list('id','title')
    # data = Job.objects.values('id','title').distinct()
    # data = Job.objects.values('id','title')

    # data = Job.objects.only('id','title')
    # data = Job.objects.defer('category')

    # data = Job.objects.aggregate(mysum = Sum('experience'), minsalary=Min('salary_start'))

    # data = Job.objects.annotate(salary_with_tax = F('salary_start')*1.25)


    data = Job.objects.only('id','title')

    return render(request, 'job/debug.html', {'data':data})










def job_list(request):

    all_jobs = Job.objects.all()

    jobs_count = all_jobs.count()

    page = request.GET.get('page', 1)

    paginator = Paginator(all_jobs, 50)
    try:
        all_jobs = paginator.page(page)
    except PageNotAnInteger:
        all_jobs = paginator.page(1)
    except EmptyPage:
        all_jobs = paginator.page(paginator.num_pages)
    return render(request,'job/job_list.html',{'jobs':all_jobs, 'jobs_count':jobs_count})



def job_detail(request, slug):
    job = Job.objects.get(slug=slug)
    return render(request, 'job/job_detail.html',{'job':job})


class JobApply(CreateView):
    model = JobApply
    success_url = '/jobs'
    #fields = ['username', 'email', 'linkedIn_url', 'githup_url', 'cv', 'cover_letter']
    form_class = JobApplyForm

    def form_valid(self, form):
        # Get the job slug from the URL
        job_slug = self.kwargs.get('slug')

        # Retrieve the job associated with the slug
        job = get_object_or_404(Job, slug=job_slug)

        # Set the job field in the form to the retrieved job
        form.instance.job = job

        # Save the form and set the success_url
        response = super().form_valid(form)

        return response
    
class AddJob(CreateView):
    model = Job
    #fields = ['title', 'location', 'company', 'salary_start', 'salary_end', 'description', 'vacancy', 'job_type', 'experience', 'category']
    success_url = '/jobs/'
    form_class = JobForm