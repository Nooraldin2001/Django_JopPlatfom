from django.urls import path
from .views import job_list, job_detail, JobApply
from .api import JopListAPI, JopDetailAPI

urlpatterns = [
    path('', job_list),
    path('<slug:slug>', job_detail),
    path('<slug:slug>/apply', JobApply.as_view()),


    #apis urls
    path('api/list', JopListAPI.as_view()),
    path('api/list/<int:pk>', JopDetailAPI.as_view()) #using pk istead of the var name id
]