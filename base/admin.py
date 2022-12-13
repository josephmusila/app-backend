from pyexpat import model
from django.contrib import admin
from django.contrib.admin import TabularInline, StackedInline, site
from super_inlines.admin import SuperInlineModelAdmin, SuperModelAdmin

from . import models
# Register your models here.

@admin.register(models.Student) 
class StudentAdmin(admin.ModelAdmin):
    list_display=['firstname','surname','course','regNumber',]
    readonly_fields = ('regNumber','password',)



@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display=['courseName','yearOfStudy','numberOfStudents']



@admin.register(models.Units)
class UnitAdmin(admin.ModelAdmin):
    list_display=['unitName','unitCode',]


    


@admin.register(models.Timetable)
class TimeTableAdmin(SuperModelAdmin):
    # inlines=(TimetableInlineAdmin,)
    model=models.Timetable
    list_display=['course','year_of_study']


    def year_of_study(self,timetable):
        return timetable.course.yearOfStudy

    def department(self,timetable):
        return timetable.course.department



@admin.register(models.Lecturer)
class LectureAdmin(admin.ModelAdmin):
   
    list_display=['firstname','surname']


@admin.register(models.SupportStaff)
class SupportStaffAdmin(admin.ModelAdmin):
    list_display=['firstname']

@admin.register(models.Fees)
class FeeAdmin(admin.ModelAdmin):
    list_display=['paymentCode','amount','cashier','student','paymentMethod']
    readonly_fields=('paymentCode',)

@admin.register(models.CustomExams)
class CustomExamAdmin(admin.ModelAdmin):
    list_display=["unit","student"]


admin.site.register(models.CourseExams)
admin.site.register(models.UnitMarks)
# admin.site.register(models.CustomExams)