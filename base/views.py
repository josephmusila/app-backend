from codecs import lookup
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from base.models import *
from base.serializers import CourseExamSerializer, CourseSerializer,StudentSerializer,TimetableSerializer,LecturerSerializer
from rest_framework.response import Response
from django.db.models import Q
from rest_framework import generics
# from django.shortcuts import get
# Create your views here.



     
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

    
@api_view(["GET"])
def getStaff(request,pk):
    try:
        staff=Lecturer.objects.get(idnumber=pk)
        # timetable=Timetable.objects.filter()
        # if students.isEmpty():
        #     return Response("No Such Student")
        serializer=LecturerSerializer(staff,many=False,context={"request":request})

        return Response(serializer.data)
    except Lecturer.DoesNotExist:
        return Response({"Error":"Reg Numnber Does Not Exist"})


class TimeTableView(generics.ListAPIView):
    queryset=Timetable.objects.all()
    serializer_class=TimetableSerializer
    allowed_method=["GET"]

    def get(self, request, *args, **kwargs):
        queryset=Timetable.objects.filter(course__id=kwargs["id"])
        serializer=TimetableSerializer(queryset,many=True)
        return Response({"timetable":serializer.data})

class StaffTimeTableView(generics.ListAPIView):
    queryset=Timetable.objects.all()
    serializer_class=TimetableSerializer
    allowed_method=["GET"]

    def get(self, request, *args, **kwargs):
        queryset=Timetable.objects.filter(lecturer__idnumber=kwargs["id"])
        serializer=TimetableSerializer(queryset,many=True)
        return Response({"timetable":serializer.data})



class StudentExamsView(generics.ListAPIView):
    queryset=CourseExams.objects.all()
    serializer_class=CourseExams
    allowed_method=["GET"]

    def get(self, request, *args, **kwargs):
        queryset=CourseExams.objects.filter(units__unit__student=kwargs["id"])
        serializer=CourseExamSerializer(queryset,many=True)
        return Response({"exams":serializer.data})

@api_view(["GET"])
def getCourses(request):
    try:
        course=Course.objects.all()
        serializer=CourseSerializer(course,many=True)
        return Response({"courses":serializer.data})

    except Course.DoesNotExist:
        return Response({"Error":"Course Does Not Exist"})