# views.py
from django.shortcuts import render, get_object_or_404
from .models import Branch, Semester, Course, Instructor,Instructor_post_pdf,Instructor_post_text
from django.urls import reverse

def home(request):
    # branch = get_object_or_404(Branch, id=branch_id)
    branch = Branch.objects.all()
    # print(branch)
    context = {'branch':branch}
    return render(request,'post/home.html',context)

# def college_view(request, college_id):
#     college = get_object_or_404(College, id=college_id)
#     branches = Branch.objects.filter(college=college)
#     context = {'college': college, 'branches': branches}
#     return render(request, 'home/college.html', context)

# def branch_view(request, branch_id):
#     branch = get_object_or_404(Branch, id=branch_id)
#     semesters = Semester.objects.filter(branch=branch)
    
#     # semester = get_object_or_404(Semester, id=semester_id)
#     # courses = Course.objects.filter(semester=semester)
#     # courses1 = Course.objects.filter(semester=semester).first()
#     context = {'branch': branch, 'semesters': semesters,}
#     return render(request, 'post/branch.html', context)

# def branch_view(request, branch_id):
#     branch = get_object_or_404(Branch, id=branch_id)
#     semesters = Semester.objects.filter(branch=branch)
#     courses = Course.objects.filter(semester__branch=branch)
#     context = {'branch': branch, 'semesters': semesters, 'courses': courses}
#     return render(request, 'post/branch.html', context)

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
    context = {'course': course,'inc':post_thing}
    return render(request, 'post/course_post.html',context)

# def semester_view(request, semester_id):
#     semester = get_object_or_404(Semester, id=semester_id)
#     courses = Course.objects.filter(semester=semester)
#     courses1 = Course.objects.filter(semester=semester).first()
#     instructors = Instructor.objects.filter(course__semester=semester)
#     context = {'semester': semester, 'courses': courses,'courses1': courses1, 'instructors':instructors}
#     return render(request, 'post/semester.html', context)

# def course_view(request, course_id):
#     course = Course.objects.get(id=course_id)
#     context = {'course': course}
#     return render(request, 'post/course.html', context)

# def instructor_view(request, instructor_id):
#     instructor = get_object_or_404(Instructor, id=instructor_id)
#     context = {'instructor': instructor}
#     return render(request, 'post/instructor.html', context)

# def post_view(request, post_id):
#     post = get_object_or_404(Instructor_post_pdf,Instructor_post_text, id=post_id)
#     context = {'post': post}
#     return render(request, 'post/post.html', context)

