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
    path('<slug:branch_url>/<slug:semester_url>/courses/<slug:url>/', views.course, name='course_view'),
    
    path('<slug:branch_url>/<slug:semester_url>/courses/<slug:course_url>/instructor/<slug:url>/<int:course_taken_in_year>', views.instructor, name='instructor_view'),
    path('<slug:branch_url>/<slug:semester_url>/courses/<slug:course_url>/instructor/<slug:instructor_url>/<int:course_taken_in_year>/pdf/<slug:pdf_url>/', views.instructor_post_pdf, name='pdf_view'),
    path('<slug:branch_url>/<slug:semester_url>/courses/<slug:course_url>/instructor/<slug:instructor_url>/<int:course_taken_in_year>/post/<slug:post_url>/', views.instructor_post_text, name='post_view'),
    # path('post/<int:post_id>/', post_view, name='post_view'),
]
