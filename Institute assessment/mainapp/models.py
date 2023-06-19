from django.db import models

class base(models.Model):
    name=models.CharField(max_length=200)
    date_of_birth=models.TextField(null=True)
    date_of_joining=models.TextField(null=True)
    address=models.TextField(null=True)
    email=models.TextField(null=True)
    contact=models.IntegerField(null=True)

class Student(base):
    roll_number=models.IntegerField()
    type_of_field=models.TextField()

class Teacher(base):
    salary=models.IntegerField()
    teacher_dept=models.CharField(max_length=50)
    teacher_qualification=models.CharField(max_length=50)

class Club(base):
    club_category=models.CharField(max_length=50)
    desc=models.CharField(max_length=500)
    membership=models.IntegerField()

class Book(base):
    book_title=models.CharField(max_length=100)
    book_author=models.CharField(max_length=100)
    book_publisher=models.CharField(max_length=100)
    book_price=models.IntegerField()
    book_description=models.CharField(max_length=500)

class mainadmin(models.Model):
    fullname=models.CharField(max_length=50, default=True)
    username=models.EmailField()
    password=models.CharField(max_length=200)