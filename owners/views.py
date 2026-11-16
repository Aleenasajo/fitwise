from django.shortcuts import render

from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from django.contrib.auth.models import User

from owners.serializers import AdminSerailizer



# Create your views here.
class AdminCreateView(CreateAPIView):

    serializer_class=AdminSerailizer

    queryset=User.objects.all()

    def post(self,request):

        form_data=request.data

        serializer_instance=AdminSerailizer(data=form_data)

        if serializer_instance.is_valid():

            cleaned_data=serializer_instance.validated_data

            instance=User.objects.create_superuser(**cleaned_data)

            serializer_instance=AdminSerailizer(instance)

            return Response(serializer_instance.data)

        else:

            return Response(serializer_instance.errors)