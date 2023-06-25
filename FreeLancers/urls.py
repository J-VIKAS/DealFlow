from django.urls import path, include
from FreeLancers.api.views import FreeLancerList

urlpatterns = [
    path('', FreeLancerList.as_view(), name = "All Users"),
]
