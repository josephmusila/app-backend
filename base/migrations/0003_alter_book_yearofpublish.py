# Generated by Django 4.0.1 on 2022-11-02 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_student_avatar_alter_student_course_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='yearOfPublish',
            field=models.DateField(blank=True, null=True),
        ),
    ]
