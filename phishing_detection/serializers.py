from rest_framework import serializers
from .models import isPhishing



class isPhishingSerializer(serializers.ModelSerializer):
    class Meta:
        model = isPhishing
        fields = ('id','isPhishing', 'rules')
