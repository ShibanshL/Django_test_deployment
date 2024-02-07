from rest_framework import serializers
from .models import *

class testDataSr(serializers.ModelSerializer):
    class Meta():
        model = testData
        fields = '__all__'
