from codecs import lookup
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from base.models import *
from base.serializers import StudentSerializer
from rest_framework.response import Response
from django.db.models import Q
from rest_framework import generics
# from django.shortcuts import get
# Create your views here.


class StudentView(ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    lookup_field="regNumber"

    def get_serializer_context(self):
        return {"request":self.request}

     
@api_view(["GET"])
def getStudent(request,pk):
    try:
        students=Student.objects.get(regNumber=pk)
        # if students.isEmpty():
        #     return Response("No Such Student")
        serializer=StudentSerializer(students,many=False,context={"request":request})

        return Response(serializer.data)
    except Student.DoesNotExist:
        return Response({"Error":"Reg Numnber Does Not Exist"})



# @api_view(["GET","POST"])
# def user_api(request,search):
#     queryset=User.objects.all()
#     serializer=user_serializer.CurrentUserSerializer(queryset,many=False)

#     return response.Response(serializer.data)
#     # data = {'sample_data': 123}
#     # return Response(data, status=HTTP_200_OK)

class LoginView(generics.ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    def get(self, request, *args, **kwargs):
        
        print( kwargs['id'])
        LoginView.queryset=Student.objects.filter(Q(regNumber=kwargs['id']))
                                                 
        
        return self.list(request, *args, **kwargs)
