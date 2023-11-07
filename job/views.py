from django.shortcuts import render
from .models import Job, JobApply
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import CreateView
from .forms import JobApplyForm, JobForm
#brings the normal get but with error handling 404
from django.shortcuts import get_object_or_404


def mydebug(request):
    data = Job.objects.all()
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