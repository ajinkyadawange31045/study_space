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

def branch_view(request, branch_id):
    branch = Branch.objects.get(id=branch_id)
    semesters = Semester.objects.filter(branch=branch)
    context = {
        'branch': branch,
        'semesters': semesters
    }
    return render(request, 'post/branch.html', context)


def course_view(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    post_thing =Instructor.objects.filter(course=course)
    course_post = Course_post.objects.filter(course=course)
    context = {'course': course,'inc':post_thing,'course_post':course_post}
    return render(request, 'post/course_post.html',context)

def instructor_view(request, instructor_id):
    instructor = get_object_or_404(Instructor, id=instructor_id)
    context = {'instructor': instructor}
    return render(request, 'post/instructor.html', context)

# def post_view(request, post_id):
#     post = get_object_or_404(Instructor_post_pdf,Instructor_post_text, id=post_id)
#     context = {'post': post}
#     return render(request, 'post/post.html', context)

