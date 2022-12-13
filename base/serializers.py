from rest_framework import serializers
from django.conf import settings
from base.models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        
        fields=('id','regNumber','names','idnumber','email','course','department','gender','avatar')
        depth=2
    # course=serializers.StringRelatedField()
    department=serializers.StringRelatedField()
    names=serializers.SerializerMethodField(method_name='student_name')
    # avatar=serializers.SerializerMethodField(method_name="get_profile_picture_url")

    def get_profile_picture_url(self, obj):
        request = self.context['request']
        return request.build_absolute_uri(settings.MEDIA_URL + obj['avatar'])

    def student_name(self,student:Student):
        return f'{student.firstname} {student.otherme} {student.surname}'

class LecturerSerializer(serializers.ModelSerializer):

    course=serializers.StringRelatedField()
    name=serializers.SerializerMethodField(method_name="lect_name")
    class Meta:
        model=Lecturer
        fields=("name","idnumber","course")

    def lect_name(self,lecturer:Lecturer):
        return f'{lecturer.firstname} {lecturer.othername} {lecturer.surname}'

class  TimetableSerializer(serializers.ModelSerializer):
    class Meta:
        model=Timetable
        fields="__all__"     
        depth=3                                        


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields="__all__"

class CourseExamSerializer(serializers.ModelSerializer):

    class Meta:
        model=CourseExams
        fields="__all__"
        depth=3