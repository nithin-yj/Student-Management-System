from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm


def home(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'home.html', context=context)


def create_student(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            profile_pic = form.cleaned_data.get('profile_pic')
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
        'form': form,
        'operation': 'Create'
    }

    return render(request, 'create-student.html', context=context)


def update_student(request, id):
    context = {}
    try:
        student = Student.objects.get(id=id)

    except Student.DoesNotExist:
        context['error'] = 'Student Does not exist'

    else:
        form = StudentForm(
            initial={
                'profile_pic': student.profile_pic,
                'name': student.name,
                'roll_no': student.roll_no,
                'email': student.email,
                'phone': student.phone,
                'address': student.address,
                'course': student.course,

            })
        context['form'] = form
        context['operation'] = 'Update'

        if request.method == 'POST':
            form = StudentForm(request.POST, request.FILES)
            if form.is_valid():
                if form.cleaned_data.get('profile_pic'):  # Image Bug resolved
                    student.profile_pic = form.cleaned_data.get('profile_pic')
                else:

                    student.profile_pic = student.profile_pic
                student.name = form.cleaned_data.get('name')
                student.roll_no = form.cleaned_data.get('roll_no')
                student.email = form.cleaned_data.get('email')
                student.phone = form.cleaned_data.get('phone')
                student.address = form.cleaned_data.get('address')
                student.course = form.cleaned_data.get('course')
                student.save()
                return redirect('home')

            context['form'] = form

    return render(request, 'update-student.html', context=context)
