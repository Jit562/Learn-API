from rest_framework import serializers
from .models import *


class jarwisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jaarwis

        fields = "__all__"