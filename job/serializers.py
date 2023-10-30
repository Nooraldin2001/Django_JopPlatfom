from rest_framework import serializers
from .models import Job



class JobSerializer(serializers.ModelSerializer):
    """
    this class will take all the data 
    Returns it in a json form 
    """
    class Meta:
        model = Job
        #fields = '__all__'
        exclude = ('location',)