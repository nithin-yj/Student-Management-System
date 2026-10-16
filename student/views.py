from django.shortcuts import render,redirect
from .models import Student
from .forms import StudentForm

def home(request):
    students = Student.objects.all()
    context = {
        'students':students
    }
    return render(request,'home.html',context=context)


def create_student(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST,request.FILES)
        if form.is_valid():
                profile_pic = form.cleaned_data('profile_pic')
                name = form.cleaned_data.get('name')
                roll_no = form.cleaned_data.get('roll_no')
                email = form.cleaned_data.get('email')
                phone = form.cleaned_data.get('phone')
                course = form.cleaned_data.get('course')
                address = form.cleaned_data.get('address')
                Student.objects.create(
                     profile_pic=profile_pic,
                     name=name,
                     roll_no=roll_no,
                     course=course,
                     phone=phone,
                     address=address,
                     email=email
                    
                )
                return redirect('home')



            
            
        
    context = {
        'form':form
    }

    return render(request,'create-student.html',context=context)


def update_student(request,id):
    if request.method == 'POST':
          pass

    return render(request,'update-student.html')

    
     

