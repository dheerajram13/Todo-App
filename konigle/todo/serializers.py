from rest_framework import serializers
from .models import Todo

#creating a seaializer class for the to do model
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'