"""
    This class is for building api's for the project
"""
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import JobSerializer
from .models import Job


@api_view(['GET'])
def job_list_api(request):
    """
    this function well take a request 
    to serlizer
    Returns: all the jobs in json 
    """
    jobs = Job.objects.all()
    data = JobSerializer(jobs, many=True).data
    return Response({'Jobs':data})

@api_view(['GET'])
def job_detail_api(request, id):
    """
    this function will take the request and job id from the user
    Returns: job dtail in jason form 
    """
    job = Job.objects.get(id=id)
    data = JobSerializer(job).data
    return Response({'Job':data})