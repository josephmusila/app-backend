from django.urls import path,include
from .views import LoginView,getStudent
urlpatterns=[
    path("students/login/<path:pk>",getStudent,name="login"),
]