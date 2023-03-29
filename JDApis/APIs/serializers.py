from django.db.models import fields
from rest_framework import serializers
from .models import JD
 
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = JD
        fields = ('title', 'department', 'industry', 'description')