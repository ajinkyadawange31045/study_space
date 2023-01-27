from django.contrib import admin
from .models import  Branch, Semester, Course,Instructor, PostForImage

# class CollegeAdmin(admin.ModelAdmin):
#     list_display = ('name', 'desc')
# admin.site.register(College,CollegeAdmin)

class BranchAdmin(admin.ModelAdmin):
    list_display = ('name','content')
admin.site.register(Branch,BranchAdmin)

class SemesterAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'branch')
admin.site.register(Semester,SemesterAdmin)


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'semester')
admin.site.register(Course,CourseAdmin)


class InstructorAdmin(admin.ModelAdmin):
    list_display = ('name', 'course_taken_in_year','about','reviews')
admin.site.register(Instructor)



class PostForImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor')
admin.site.register(PostForImage)

