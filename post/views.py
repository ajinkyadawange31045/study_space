# views.py
from django.shortcuts import render, get_object_or_404
from .models import Branch, Semester, Course, Instructor,PostForImage

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

def branch_view(request, branch_id):
    branch = get_object_or_404(Branch, id=branch_id)
    semesters = Semester.objects.filter(branch=branch)
    context = {'branch': branch, 'semesters': semesters}
    return render(request, 'branch.html', context)

# def semester_view(request, semester_id):
#     semester = get_object_or_404(Semester, id=semester_id)
#     courses = Course.objects.filter(semester=semester)
#     instructors = Instructor.objects.filter(course__semester=semester)
#     context = {'semester': semester, 'courses': courses, 'instructors':instructors}
#     return render(request, 'semester.html', context)

# def course_view(request, course_id):
#     course = Course.objects.get(id=course_id)
#     context = {'course': course}
#     return render(request, 'course.html', context)

# def instructor_view(request, instructor_id):
#     instructor = get_object_or_404(Instructor, id=instructor_id)
#     context = {'instructor': instructor}
#     return render(request, 'instructor.html', context)

# def post_view(request, post_id):
#     post = get_object_or_404(PostForImage, id=post_id)
#     context = {'post': post}
#     return render(request, 'post.html', context)

