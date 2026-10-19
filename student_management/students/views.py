from django.shortcuts import render, redirect,get_object_or_404
from .models import Student

def home(request):
    return render(request, 'home.html')

def add_Student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        age = request.POST.get('age')
        course = request.POST.get('course')

        Student.objects.create(
            name=name,
            email=email,
            phone=phone,
            age=age,
            course=course
        )
        return redirect('home')
    
    return render(request, 'add_Student.html')




def view_students(request):
    students=Student.objects.all()
    return render(request,'Student_list.html',{'students':students})

def update_student(request, id):

    student = get_object_or_404(Student, id=id)

    if request.method == "POST":

        student.name = request.POST['name']
        student.email = request.POST['email']
        student.phone = request.POST['phone']
        student.age = request.POST['age']
        student.course = request.POST['course']

        student.save()

        return redirect('/view/')

    return render(request,'update_student.html', {
        'student': student
    })