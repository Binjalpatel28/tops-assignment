from django.shortcuts import render, redirect
from mainapp.models import *
from django.conf import settings
from django.contrib.auth.hashers import make_password,check_password
from django.core.mail import send_mail
import random
from rest_framework.views import APIView
from mainapp.serializers import *
from rest_framework.response import Response

def index(request):
    session_user_data=mainadmin.objects.get(username=request.session['email'])
    all_books=Book.objects.all().count()
    all_teachers=Teacher.objects.all().count()
    all_students=Student.objects.all().count()
    all_clubs=Club.objects.all().count()
    return render(request,"home.html",{"session_userdata":session_user_data,"all_clubs":all_clubs,"all_books":all_books,"all_teachers":all_teachers,"all_students":all_students})

    # try:
    #     request.session["email"]
    #     session_userdata=mainadmin.objects.get(username=request.POST['email'])
    #     return render(request,"index.html",{"session_userdata":session_userdata})
    # except:
    #     return render(request,"index.html")
def home(request):
    all_books=Book.objects.all().count()
    all_teachers=Teacher.objects.all().count()
    all_students=Student.objects.all().count()
    all_clubs=Club.objects.all().count()
    return render(request,"index.html",{"all_clubs":all_clubs,"all_books":all_books,"all_teachers":all_teachers,"all_students":all_students})

def register(request):
    if request.method=="POST":
            try:
                mainadmin.objects.get(username=request.POST['email'])
                return render(request,"register.html",{'msg':"User Already exist"})
            except:
                #   return render(request,"register.html",{'msg':"User Not exist"}
                if request.POST['password']==request.POST['cpassword']:
                    global votp
                    votp=random.randint(100000,999999)
                    subject = 'OTP VERIFICATION INSTITUTE MANAGEMENT'
                    message = f'HI THNAKS FOR CHOOSING YOUR OTP IS {votp}'
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [request.POST['email'],]
                    send_mail( subject, message, email_from, recipient_list )
                    global temp
                    temp={
                        'fname':request.POST['fname'],
                        'uname':request.POST['email'],
                        'pass':make_password(request.POST["password"])
                    }
                    return render(request,"otp.html")
                else:
                    return render(request,"register.html",{'msg':"Password and Confirm Password Not match"})
    else:
        return render(request,"register.html")
    
def otp(request):
        if request.method=="POST":
            if votp==int(request.POST['otp']):
                mainadmin.objects.create(
                fullname=temp['fname'],
                username=temp['uname'],
                password=temp['pass']
            )
                return render(request,"login.html")
            else:
                return render(request,"otp.html",{'msg':'Invalid OTP'})
        else:
                return render(request,"otp.html")

def login(request):
    if request.method=="POST":
        try:
            user_data=mainadmin.objects.get(username=request.POST['email'])
            if check_password(request.POST["password"],user_data.password):
                    request.session['email']=request.POST['email']
                    request.session['name']=user_data.fullname
                    session_userdata=mainadmin.objects.get(username=request.POST['email'])
                    return render(request,"index.html",{"session_userdata":session_userdata})
            else:
                    return render(request,"login.html",{"msg":"Invalid Password"})
        except:
            return render(request,"login.html",{"msg":"Account not exist please register"}) 
    else:
        return render(request,"login.html")


def forgotpassword(request):
   
        if request.method=="POST":
            try:
                user_data=mainadmin.objects.get(username=request.POST['email'])
                request.session['e_email']=request.POST["email"]
                global votp
                votp=random.randint(100000,999999)
                subject = 'OTP VERIFICATION INSTITUTE MANAGEMENT'
                message = f'HI Thanks FOR CHOOSING YOUR OTP IS {votp}'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [request.POST['email'],]
                send_mail( subject, message, email_from, recipient_list )
                return render(request,"forgot_otp.html") 
            except:
                return render(request,"forgot-password.html",{'msg':"your email is not register please register first"})
        else:
            return render(request,"forgot-password.html") 

def forgot_otp(request):
   
        if request.method=="POST":
            if votp==int(request.POST['otp']):
                return render(request,"reset-password.html",{"msg":"Registration succesfully"})
            else:
                return render(request,"forgot_otp.html",{"msg":"OTP is Incorrect Password"})
        else:
            return render(request,"forgot_otp.html")

def reset_password(request):
    if request.method =="POST":
         if request.POST['password']==request.POST['cpassword']:
            user_data=mainadmin.objects.get(username=request.session['e_email'])
            user_data.password= make_password(request.POST['password'])
            user_data.save()
            return render(request,"index.html",{"msg":"password reset successfully"})
         else:
            return render(request,"reset-password.html",{"msg":"password not match"})
    else:
        return render(request,"reset-password.html")

def logout(request):
    try:
        request.session['email']
        del request.session['email']
        return render(request,"index.html")

    except:
        return render(request,"index.html")

def student(request):
    user_data=Student.objects.all()
    session_userdata=mainadmin.objects.get(username=request.session['email'])
    return render(request,"student.html",{"user_data":user_data,"session_userdata":session_userdata})


def update_student(request,pk):
    if request.method=="POST":
        oneuser_data=Student.objects.get(id=pk)
        oneuser_data.name=request.POST['fname']
        oneuser_data.date_of_birth=request.POST['dob']
        oneuser_data.date_of_joining=request.POST['doj']
        oneuser_data.address=request.POST['address']
        oneuser_data.email=request.POST['email']
        oneuser_data.contact=request.POST['contact']
        oneuser_data.roll_number=request.POST['rnum']
        oneuser_data.type_of_field=request.POST['field']
        oneuser_data.save()
        user_data=Student.objects.all()
        return student(request)
    else:
        oneuser_data=Student.objects.get(id=pk)
        user_data=Student.objects.all()
        session_userdata=mainadmin.objects.get(username=request.session['email'])
        return render(request,"update_student.html",{"oneuser_data":oneuser_data,"user_data":user_data,"session_userdata":session_userdata})

def delete_student(request,pk):
        user_data =Student.objects.get(id=pk)
        user_data.delete()
        return student(request)

def teacher(request):
    user_data=Teacher.objects.all()
    session_userdata=mainadmin.objects.get(username=request.session['email'])
    return render(request,"teacher.html",{"user_data":user_data,"session_userdata":session_userdata})

def update_teacher(request,pk):
    if request.method=="POST":
        oneuser_data=Teacher.objects.get(id=pk)
        oneuser_data.name=request.POST['fname']
        oneuser_data.date_of_birth=request.POST['dob']
        oneuser_data.date_of_joining=request.POST['doj']
        oneuser_data.address=request.POST['address']
        oneuser_data.email=request.POST['email']
        oneuser_data.contact=request.POST['contact']
        oneuser_data.salary=request.POST['salary']
        oneuser_data.teacher_dept=request.POST['dept']
        oneuser_data.teacher_qualification=request.POST['qualification']
        oneuser_data.save()
        user_data=Teacher.objects.all()
        return teacher(request)
    else:
        oneuser_data=Teacher.objects.get(id=pk)
        user_data=Teacher.objects.all()
        session_userdata=mainadmin.objects.get(username=request.session['email'])
        return render(request,"update_teacher.html",{"oneuser_data":oneuser_data,"user_data":user_data,"session_userdata":session_userdata})

def delete_teacher(request,pk):
        user_data =Teacher.objects.get(id=pk)
        user_data.delete()
        return teacher(request)

def club(request):
    user_data=Club.objects.all()
    session_userdata=mainadmin.objects.get(username=request.session['email'])
    return render(request,"club.html",{"user_data":user_data,"session_userdata":session_userdata})

def update_club(request,pk):
    if request.method=="POST":
        oneuser_data=Club.objects.get(id=pk)
        oneuser_data.name=request.POST['fname']
        oneuser_data.address=request.POST['address']
        oneuser_data.email=request.POST['email']
        oneuser_data.contact=request.POST['contact']
        oneuser_data.club_category=request.POST['cat']
        oneuser_data.desc=request.POST['desc']
        oneuser_data.membership=request.POST['member']
        oneuser_data.save()
        user_data=Club.objects.all()
        return club(request)
    else:
        oneuser_data=Club.objects.get(id=pk)
        user_data=Club.objects.all()
        session_userdata=mainadmin.objects.get(username=request.session['email'])
        return render(request,"update_club.html",{"oneuser_data":oneuser_data,"user_data":user_data,"session_userdata":session_userdata})

def delete_club(request,pk):
        user_data =Club.objects.get(id=pk)
        user_data.delete()
        return club(request)

def book(request):
    user_data=Book.objects.all()
    session_userdata=mainadmin.objects.get(username=request.session['email'])
    return render(request,"book.html",{"user_data":user_data,"session_userdata":session_userdata})

def update_book(request,pk):
    if request.method=="POST":
        oneuser_data=Book.objects.get(id=pk)
        oneuser_data.name=request.POST['name']
        oneuser_data.book_title=request.POST['title']
        oneuser_data.book_author=request.POST['author']
        oneuser_data.book_publisher=request.POST['publisher']
        oneuser_data.book_price=request.POST['price']
        oneuser_data.book_description=request.POST['desc']
        oneuser_data.save()
        user_data=Book.objects.all()
        return book(request)
    else:
        oneuser_data=Book.objects.get(id=pk)
        user_data=Book.objects.all()
        session_userdata=mainadmin.objects.get(username=request.session['email'])
        return render(request,"update_book.html",{"oneuser_data":oneuser_data,"user_data":user_data,"session_userdata":session_userdata})

def delete_book(request,pk):
        user_data =Book.objects.get(id=pk)
        user_data.delete()
        return Book(request)

class booklist(APIView):
    def get(self,request):
        books=Book.objects.all()
        book_data=bookserializer(books,many=True)
        return Response(book_data.data)

class singlebooklist(APIView):
    def get(self,request,pk):
        books=Book.objects.get(id=pk)
        book_data=bookserializer(books)
        return Response(book_data.data)