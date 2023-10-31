"""
    This class is for building api's for the project
"""
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated




from .serializers import JobSerializer
from .models import Job

"""
from rest_framework.decorators import api_view
from rest_framework.response import Response

    another way to work with api's 
    @api_view(['GET'])
    def job_list_api(request):
    
    this function well take a request 
    to serlizer
    Returns: all the jobs in json 
    
    jobs = Job.objects.all()
    data = JobSerializer(jobs, many=True).data
    return Response({'Jobs':data})

    @api_view(['GET'])
    def job_detail_api(request, id):
    
    this function will take the request and job id from the user
    Return: job dtail in jason form 
    
    job = Job.objects.get(id=id)
    data = JobSerializer(job).data
    return Response({'Job':data})
"""


class JopListAPI(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'vacancy', 'job_type']
    search_fields = ['title', 'description']
    ordering_fields = ['salary_start', 'salary_end', 'experience']
    permission_classes = [IsAuthenticated]




class JopDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all() #it can handle the only one retreving process
    serializer_class = JobSerializer