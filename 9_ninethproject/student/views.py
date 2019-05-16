from django.shortcuts import render, redirect, get_object_or_404
from .models import Student

# Create your views here.

def index(request):
    students = Student.objects.all

    return render(request, "index.html", {
        "students": students,
    })


def create_page(request):
    return render(request, "create_page.html", {

    })


def create(request):
    student = Student()

    student.name = request.GET["name"]
    student.department = request.GET["department"]
    student.admission_year = request.GET["admission_year"]
    student.student_number = request.GET["student_number"]
    student.level = request.GET["level"]
    student.grade_avg = request.GET["grade_avg"]

    student.save()

    return redirect("index")


def read(request, id):
    student = get_object_or_404(Student, pk=id)

    return render(request, "read.html", {
        "student": student,
    })


def update(request, id):
    student = get_object_or_404(Student, pk=id)

    student.name = request.GET["name"]
    student.department = request.GET["department"]
    student.admission_year = request.GET["admission_year"]
    student.student_number = request.GET["student_number"]
    student.level = request.GET["level"]
    student.grade_avg = request.GET["grade_avg"]

    student.save()

    return redirect("index")


def update_page(request, id):
    student = get_object_or_404(Student, pk=id)

    return render(request, "update.html", {
        "student": student,
    })

def delete(request, id):
    student = get_object_or_404(Student, pk=id)

    student.delete()

    return redirect("index")
