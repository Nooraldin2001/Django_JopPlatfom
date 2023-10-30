from django.urls import path
from .views import job_list, job_detail
from .api import JopListAPI, JopDetailAPI

urlpatterns = [
    path('', job_list),
    path('<slug:slug>', job_detail),


    #apis urls
    path('api/list', JopListAPI.as_view()),
    path('api/list/<int:pk>', JopDetailAPI.as_view()) #using pk istead of the var name id
]