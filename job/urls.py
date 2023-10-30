from django.urls import path
from .views import job_list, job_detail
from .api import job_list_api, job_detail_api, JopListAPI, JopDetailAPI

urlpatterns = [
    path('', job_list),
    path('<slug:slug>', job_detail),


    #apis urls
    path('api/list', JopListAPI.as_view()),
    path('api/list/<int:id>', JopDetailAPI.as_view())
]