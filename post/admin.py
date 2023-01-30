from django.contrib import admin
from .models import  Branch, Semester, Course,Instructor, Instructor_post_pdf,Instructor_post_text,Course_post

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
admin.site.register(Instructor,InstructorAdmin)



class Instructor_post_pdfAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
admin.site.register(Instructor_post_pdf,Instructor_post_pdfAdmin)


class Instructor_post_textAdmin(admin.ModelAdmin):
    list_display = ('title','image', 'content')
admin.site.register(Instructor_post_text,Instructor_post_textAdmin)


from  embed_video.admin  import  AdminVideoMixin
from .models  import  Course_post
#Register your models here.

class  Course_postAdmin(AdminVideoMixin, admin.ModelAdmin):
    list_display = ('books_link_drive','youtube_Title', 'youtube_Resources','youtube_Body')
	# pass

admin.site.register(Course_post, Course_postAdmin)