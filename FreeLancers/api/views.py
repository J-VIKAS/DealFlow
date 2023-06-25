from rest_framework.response import Response
from rest_framework import generics
from FreeLancers.models import FreeLancer
from FreeLancers.api.pagination import FreeLancerListPagination
from django_filters.rest_framework import DjangoFilterBackend
from FreeLancers.api.serializers import FreeLancerSerializer

# Create your views here.
class FreeLancerList(generics.ListCreateAPIView):
    queryset = FreeLancer.objects.all()
    serializer_class = FreeLancerSerializer
    filter_backends = [DjangoFilterBackend] 
    filterset_fields = ['first_name','last_name','email','phone_number','followers']
    pagination_class = FreeLancerListPagination