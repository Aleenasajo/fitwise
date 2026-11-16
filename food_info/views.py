from django.shortcuts import render,get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import authentication,permissions

from food_info.models import FoodLog
from food_info.serializers import FoodLogSerializer



from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView

# Create your views here.
class FoodLogListCreateView(ListAPIView,CreateAPIView):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    serializer_class=FoodLogSerializer

    queryset=FoodLog.objects.all()


    def post(self,request):

        form_data=request.data

        serializer_instance=FoodLogSerializer(data=form_data)

        if serializer_instance.is_valid():


            serializer_instance.save()

            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)

        else:

            return Response(serializer_instance.data,status=status.HTTP_400_BAD_REQUEST)

class FoodLogRetrieveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    serializer_class=FoodLogSerializer

    queryset=FoodLog.objects.all()

    def put(self,request,pk=None):

        form_data=request.data

        instance=get_object_or_404(FoodLog,id=pk)

        serializer_instance=FoodLogSerializer(data=form_data,instance=instance)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(serializer_instance.data,status=status.HTTP_200_OK)

        else:

            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

        

        


        
