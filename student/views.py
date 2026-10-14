from django.shortcuts import render
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
            print(form.cleaned_data)
            
        
    context = {
        'form':form
    }

    return render(request,'create-student.html',context=context)

