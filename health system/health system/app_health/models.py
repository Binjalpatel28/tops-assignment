from django.db import models

# Create your models here.

class User(models.Model):
    fullname=models.CharField(max_length=50)
    username=models.EmailField(unique=True)
    password=models.CharField(max_length=50)
    profilepic = models.FileField(upload_to='media/',default="anonymous.jpg")
    contact=models.CharField(max_length=10)
    def __str__(self):
        return self.fullname
    
class doctor_User(models.Model):
    doctorname=models.CharField(max_length=50)
    specializations=models.CharField(max_length=50)
    doctorpic=models.FileField(upload_to='media/',default="anonymous.jpg")
    contact=models.CharField(max_length=10)
    desc=models.CharField(max_length=1500)
    disease=models.CharField(max_length=50)

    def __str__(self):
        return self.doctorname
    
class disease_User(models.Model):
    doctor=models.ForeignKey(doctor_User, on_delete=models.CASCADE,null=True)
    diseasename=models.CharField(max_length=50)
    symptoms=models.CharField(max_length=100)
    precaution=models.CharField(max_length=500)
    medicinename=models.CharField(max_length=50)
    descpic=models.FileField(upload_to='media/',default="anonymous.jpg")

    def __str__(self):
        return self.diseasename
    
class medicine_User(models.Model):
    diseasename=models.ForeignKey(disease_User, on_delete=models.CASCADE,null=True)
    medicinename=models.CharField(max_length=50)
    medprecaution=models.CharField(max_length=100)
    meddesc=models.CharField(max_length=100)
    medprice=models.CharField(max_length=10)
    medpic=models.FileField(upload_to='media/',default="anonymous.jpg")

    def __str__(self):
        return self.medicinename

class cart(models.Model):
    medicine=models.ForeignKey(medicine_User,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0)
    total=models.IntegerField(default=0)

    def __str__(self):
        return str(self.quantity)+" "+str(self.medicine.medicinename)