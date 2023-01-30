# views.py
from django.shortcuts import render, get_object_or_404
from .models import Branch, Semester, Course, Instructor,Instructor_post_pdf,Instructor_post_text,Course_post
from django.urls import reverse

def home(request):
    # branch = get_object_or_404(Branch, id=branch_id)
    branch = Branch.objects.all()
    # print(branch)
    context = {'branch':branch}
    return render(request,'post/home.html',context) 

def semester(request, url):
    branch = Branch.objects.get(url=url)
    semesters = Semester.objects.filter(branch=branch)
    context = {
        'branch': branch,
        'semesters': semesters
    }
    return render(request, 'post/semester.html', context)


def course(request, url):
    course = get_object_or_404(Course, url=url)
    post_thing =Instructor.objects.filter(course=course)
    course_post = Course_post.objects.filter(course=course)
    context = {'course': course,'inc':post_thing,'course_post':course_post}
    return render(request, 'post/course.html',context)

def instructor(request, url):
    instructor = get_object_or_404(Instructor, url=url)
    instructor_post_pdf = Instructor_post_pdf.objects.all().filter(instructor=instructor)
    instructor_post_text = Instructor_post_text.objects.all().filter(instructor=instructor)
    context = {'instructor': instructor,'instructor_post_pdf':instructor_post_pdf,'instructor_post_text':instructor_post_text}
    return render(request, 'post/instructor.html', context)

def instructor_post_pdf(request, url):
    instructor_post_pdf = get_object_or_404(Instructor_post_pdf, url=url)
    context = {'instructor_post_pdf': instructor_post_pdf}
    return render(request, 'post/instructor_post_pdf.html', context)

def instructor_post_text(request, url):
    instructor_post_text = get_object_or_404(Instructor_post_text, url=url)
    context = {'instructor_post_text': instructor_post_text}
    return render(request, 'post/instructor_post_text.html', context)

