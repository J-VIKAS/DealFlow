from rest_framework import serializers
from FreeLancers.models import FreeLancer

class FreeLancerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreeLancer
        fields = "__all__"