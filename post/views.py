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


def course(request, url,branch_url,semester_url):
    branch = Branch.objects.get(url = branch_url)
    semester = Semester.objects.get(url = semester_url)
    course = get_object_or_404(Course, url=url)
    post_thing =Instructor.objects.filter(course=course)
    course_post = Course_post.objects.filter(course=course)
    context = {'branch':branch, 'course': course,'inc':post_thing,'course_post':course_post,'semester':semester}
    return render(request, 'post/course.html',context)

def instructor(request, url, branch_url,semester_url,course_url,course_taken_in_year):
    branch = Branch.objects.get(url = branch_url)
    semester = Semester.objects.get(url = semester_url)
    course = Course.objects.get(url = course_url)
    instructor = get_object_or_404(Instructor, url=url,id=course_taken_in_year)
    instructor_post_pdf1 = Instructor_post_pdf.objects.all().filter(instructor=instructor)
    instructor_post_text1 = Instructor_post_text.objects.all().filter(instructor=instructor)
    context = {'instructor': instructor,'instructor_post_pdf1':instructor_post_pdf1,'instructor_post_text1':instructor_post_text1,'course':course,'branch':branch,'semester':semester}
    return render(request, 'post/instructor.html', context)

def instructor_post_pdf(request, pdf_url, branch_url,semester_url,course_url,instructor_url,course_taken_in_year):
    branch = Branch.objects.get(url = branch_url)
    semester = Semester.objects.get(url = semester_url)
    course = Course.objects.get(url = course_url)
    instructor = Instructor.objects.get(url=instructor_url,id=course_taken_in_year)
    instructor_post_pdf1 = get_object_or_404(Instructor_post_pdf, url=pdf_url)
    context = {'instructor_post_pdf1': instructor_post_pdf1,'course':course,'branch':branch,'semester':semester,'instructor':instructor}
    return render(request, 'post/instructor_post_pdf.html', context)

def instructor_post_text(request, post_url, branch_url,semester_url,course_url,instructor_url,course_taken_in_year):
    branch = Branch.objects.get(url = branch_url)
    semester = Semester.objects.get(url = semester_url)
    course = Course.objects.get(url = course_url)
    instructor = Instructor.objects.get(url=instructor_url,id=course_taken_in_year)
    instructor_post_text1 = get_object_or_404(Instructor_post_text, url=post_url)
    context = {'instructor_post_text1': instructor_post_text1,'course':course,'branch':branch,'semester':semester,'instructor':instructor}
    return render(request, 'post/instructor_post_text.html', context)

