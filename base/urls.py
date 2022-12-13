from django.urls import path,include
from .views import getStudent,getStaff,getCourses,TimeTableView,StaffTimeTableView
from . import views
urlpatterns=[
    path("students/login/<path:pk>",getStudent,name="login"),
     path("staff/login/<path:pk>",getStaff,name="staff-login"),


    path("timetable/<id>",TimeTableView.as_view(),name="timetable"),
    path("stafftimetable/<id>",StaffTimeTableView.as_view(),name="stafftimetable"),
    path("examination/<id>",views.StudentExamsView.as_view(),name="exams"),
    path("courses",getCourses,name="courses")
    
]