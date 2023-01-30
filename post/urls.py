# from django.urls import path,include
# from .views import home
# urlpatterns = [
    
#     path('',home)
# ]

from . import views
# urls.py
from django.urls import path
# from .views import college_view, branch_view, semester_view, instructor_view, post_view,home
from .views import home,semester

urlpatterns = [
    path('',home,name='home'),
    # path('college/<int:college_id>/', college_view, name='college_view'),
    path('branch/<slug:url>/', semester, name='semester'),
    path('branch/courses/<slug:url>/', views.course, name='course_view'),
    
    path('branch/courses/instructor/<slug:url>/', views.instructor, name='instructor_view'),
    path('branch/courses/instructor/pdfs/<slug:url>/', views.instructor_post_pdf, name='pdf_view'),
    path('branch/courses/instructor/post/<slug:url>/', views.instructor_post_text, name='post_view'),
    # path('post/<int:post_id>/', post_view, name='post_view'),
]
