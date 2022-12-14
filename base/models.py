from calendar import TUESDAY, WEDNESDAY
from dataclasses import fields
import datetime
from distutils.command.upload import upload
from sqlite3 import Date
from django.db import models
from django.utils.text import slugify 
from datetime import date
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    email=models.EmailField(unique=True)






class Course(models.Model):
    
    courseName=models.CharField(max_length=200)
    
    yearOfStudy=models.IntegerField()
    numberOfStudents=models.IntegerField()
    courseCode=models.CharField(max_length=5)

    def __str__(self):
        return f'{self.courseName}'

class Units(models.Model):
    
    unitName=models.CharField(max_length=200)
    unitCode=models.CharField(max_length=8)

    def __str__(self):
        return f'{self.unitName}'


class Lecturer(models.Model):
    firstname=models.CharField(max_length=50)
    othername=models.CharField(max_length=50)
    surname=models.CharField(max_length=50)
    idnumber=models.IntegerField(unique=True)
    dateOfBirth=models.DateField()
    course=models.ForeignKey(Course,on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.firstname}'


class Student(models.Model):

    MALE="M"
    FEMALE="F"
    OTHER="O"
    GENDER_CHOICES=[
        (MALE,"Male"),
        (FEMALE,"Female"),
        (OTHER,"Other")
    ]
    
    id = models.AutoField(primary_key=True)
    
    firstname = models.CharField(max_length=50,blank=True,null=True)
    otherme = models.CharField(max_length=50,blank=True,null=True)
    surname= models.CharField(max_length=50,blank=True,null=True)
    idnumber = models.IntegerField(unique=True,blank=True,null=True)
    dateOfBirth = models.DateField(blank=True,null=True)
    password=models.IntegerField(default=12345678,blank=True,null=True)
    email = models.EmailField(unique=True,blank=True,null=True)
    residence = models.CharField(max_length=50,blank=True,null=True)
    religion = models.CharField(max_length=50,default="Christian",blank=True,null=True)
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES,default=OTHER,blank=True,null=True)
    avatar=models.ImageField(upload_to="student_avatars",blank=True,null=True)
    
    course=models.ForeignKey(Course,on_delete=models.DO_NOTHING,blank=True,null=True)
    regNumber = models.SlugField(blank=True,null=True)

    def __str__(self) -> str:
        return self.regNumber
 
    def save(self, *args, **kwargs):
        # if self.department.departmentName == "IT":
        # self.regNumber = f'{self.course.courseCode}/{self.id}/{date.today().year}'
        # self.department=self.course.department
        # self.school=self.course.department.school
        # self.faculty=self.course.department.school.faculty
        self.password=self.idnumber
        super().save(*args, **kwargs)

       
def student_post_save(sender,instance,created, *args,**kwargs,):
    
     instance.regNumber = f'{instance.course.courseCode}/{"0"* (5-(len(str(instance.id))))}{instance.id}/{date.today().year}'
     instance.course.numberOfStudents = instance.course.numberOfStudents +1
     if created:
       
        instance.save()

post_save.connect(student_post_save,sender=Student)







class Timetable(models.Model):

    MONDAY="MONDAY"
    TUESDAY="TUESDAY"
    WEDNESDAY="WEDNESDAY"
    THURSDAY="THURSDAY"
    FRIDAY="FRIDAY"
    WEEKDAY_CHOICE=[
        (MONDAY,"MONDAY"),
        (TUESDAY,"TUESDAY"),
        (WEDNESDAY,"WEDNESDAY"),
        (THURSDAY,"THURSDAY"),
        (FRIDAY,"FRIDAY"),
    ]


    TIMESLOT_1="7:00-9:00"
    TIMESLOT_2="9:00-11:00"
    TIMESLOT_3="11:00-1:00"
    TIMESLOT_4="1:00-2:00"
    TIMESLOT_5="2:00-4:00"
    TIMESLOT_6="4:00-6:00"
    TIMESLOT_CHOICE=[
        (TIMESLOT_1,"7:00-9:00"),
        (TIMESLOT_2,"9:00-11:00"),
        (TIMESLOT_3,"11:00-1:00"),
        (TIMESLOT_4,"1:00-2:00"),
        (TIMESLOT_5,"2:00-4:00"),
        (TIMESLOT_6,"4:00-6:00"),
    ]

    course=models.ForeignKey(Course,on_delete=models.DO_NOTHING)
    day=models.CharField(max_length=10,choices=WEEKDAY_CHOICE,blank=False)
    unit=models.ForeignKey(Units,on_delete=models.DO_NOTHING  )
    time=models.CharField(max_length=20,choices=TIMESLOT_CHOICE)
    lecturer=models.ForeignKey(Lecturer,on_delete=models.DO_NOTHING)




class StaffDepartment(models.Model):

    FINANCE="FINANCE"
    CLEANING='CLEANING'
    KITCHEN="KITCHEN"
    TECHNICIAN="TECHNICIAN"
    DRIVERS="DRIVERS"
    HEALTH="HEALTH"
    SECURITY="SECURITY"
    RECEPTIONS="RECEPTIONS"
    LIBRARY="LIBRARY"




    department=models.CharField(max_length=100)
    departmentCode=models.CharField(max_length=5)


class SupportStaff(models.Model):
    MALE="M"
    FEMALE="F"
    OTHER="O"
    GENDER_CHOICES=[
        (MALE,"Male"),
        (FEMALE,"Female"),
        (OTHER,"Other")
    ]
    
   
    firstname = models.CharField(max_length=50,blank=False)
    otherme = models.CharField(max_length=50,blank=False)
    surname= models.CharField(max_length=50,blank=True)
    idnumber = models.IntegerField(unique=True,blank=True)
    dateOfBirth = models.DateField()
    password=models.IntegerField(default=12345678)
    email = models.EmailField(unique=True)
    residence = models.CharField(max_length=50)
    religion = models.CharField(max_length=50)
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES,default=OTHER)
    avatar=models.CharField(max_length=200)
    department=models.ForeignKey(StaffDepartment,on_delete=models.DO_NOTHING)


#social media tables

class Post(models.Model):
    creator=models.ForeignKey(Student,on_delete=models.DO_NOTHING)
    content=models.TextField(max_length=500)
    image=models.ImageField()
    created=models.DateTimeField(auto_now_add=True)
    verified=models.BooleanField(default=False)
    likes=models.IntegerField()
    
class Comment(models.Model):
    commentedBy=models.ForeignKey(Student,on_delete=models.DO_NOTHING)
    comment=models.TextField(max_length=200)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    verified=models.BooleanField(default=False)


#Library tables


class Book(models.Model):
    bookName=models.CharField(max_length=50)
    bookSerialNumber=models.CharField(max_length=20)
    publisher=models.CharField(max_length=50)
    author=models.CharField(max_length=100)
    yearOfPublish=models.DateField(blank=True,null=True)


class Library(models.Model):
    student=models.ForeignKey(Student,on_delete=models.DO_NOTHING)
    dateJoined=models.DateField(auto_now_add=True)
    bookBorrowed=models.ForeignKey(Book,on_delete=models.DO_NOTHING)
    dateOfReturn=models.DateField()
    issuedBy=models.ForeignKey(SupportStaff,on_delete=models.DO_NOTHING)




    
class Fees(models.Model):

    PAYMENT_METHOD_MOBILE="MOBILE"
    PAYMENT_METHOD_CHEQUE='CHEQUE'
    PAYMENT_METHOD_CASH="CASH"

    PAYMENT_METHOD=[
        (PAYMENT_METHOD_MOBILE,"MOBILE"),
        (PAYMENT_METHOD_CHEQUE,"CHEQUE"),
        (PAYMENT_METHOD_CASH,"CASH")
    ]
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    cashier=models.ForeignKey(SupportStaff,on_delete=models.DO_NOTHING,null=True)
    student=models.ForeignKey(Student,on_delete=models.DO_NOTHING)   
    paymentTime=models.DateTimeField(auto_now_add=True,null=True)
    paymentMethod=models.CharField(max_length=20,choices=PAYMENT_METHOD,default=PAYMENT_METHOD_CHEQUE,null=False)
    paymentCode=models.CharField(max_length=30)


def fee_post_save(sender,instance,created,*args,**kwargs):
    if(instance.paymentMethod==instance.PAYMENT_METHOD_MOBILE):
        instance.paymentCode=f'MOB/{instance.student.regNumber}/{instance.paymentTime}'
    if created:
        instance.save()

post_save.connect(fee_post_save,sender=Fees)






class CustomExams(models.Model):
    student=models.ForeignKey(Student,on_delete=models.DO_NOTHING)
    marks=models.IntegerField()
    grade=models.CharField(max_length=1,blank=True,null=True)
    unit=models.ForeignKey(Units,on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.unit.unitName
    

def grade_post_save(sender,instance,created,*args,**kwargs):
    if(instance.marks>70):
        instance.grade="A"
    else:
        instance.grade="D" 

    if created:
        instance.save()

post_save.connect(grade_post_save,sender=CustomExams)

class UnitMarks(models.Model):
    unit=models.ManyToManyField(CustomExams)
    


    # def __str__(self) -> str:
    #     return self.unit



class CourseExams(models.Model):
    course=models.ForeignKey(Course,on_delete=models.DO_NOTHING)
    examdate=models.DateField(auto_now_add=True)
    semester=models.IntegerField()
    units=models.ManyToManyField(UnitMarks)
    
    def __str__(self) -> str:
        return self.course.courseName
    
