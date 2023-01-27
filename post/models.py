from django.db import models
from taggit.managers import TaggableManager 

# Create your models here.
from django.db import models
# class College(models.Model):
#     name = models.CharField( blank=True, max_length=60)
#     desc = models.CharField( blank=True, max_length=330)
    
#     def __str__(self):
#         return self.name

class Branch(models.Model):
    # college = models.ForeignKey(College, on_delete=models.CASCADE)
    name = models.CharField( blank=True, max_length=255)
    content = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class Semester(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    name = models.CharField( blank=True, max_length=255)
    number = models.IntegerField()
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class Course(models.Model):
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    title = models.CharField( blank=True, max_length=255)
    views = models.IntegerField()
    def __str__(self):
        return self.title


    

class Instructor(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField( blank=True, max_length=255)
    course_taken_in_year = models.IntegerField()
    about = models.TextField(blank=True)
    content = models.TextField(blank=True)
    reviews = models.TextField(blank=True)
    books_drive_link = models.CharField( blank=True, max_length=1000)
    resources = models.TextField(blank=True)
    youtube_embed_videos = TaggableManager()
    def __str__(self):
        return self.name


class PostForImage(models.Model):
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    title = models.CharField( blank=True, max_length=255)
    image = models.ImageField(blank=True)
    content = models.TextField(blank=True)
    tags = TaggableManager()
    pdf_link = models.CharField(max_length=1000,blank=True)
    def __str__(self):
        return self.title
