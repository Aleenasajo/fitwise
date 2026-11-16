from rest_framework import serializers
from django.contrib.auth.models import User

class AdminSerailizer(serializers.ModelSerializer):

    class Meta:
        
        model=User

        fields=["id","username","email","password"]