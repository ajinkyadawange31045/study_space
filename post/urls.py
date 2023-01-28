# from django.urls import path,include
# from .views import home
# urlpatterns = [
    
#     path('',home)
# ]

from . import views
# urls.py
from django.urls import path
# from .views import college_view, branch_view, semester_view, instructor_view, post_view,home
from .views import home,branch_view,semester_view

urlpatterns = [
    path('',home,name='home'),
    # path('college/<int:college_id>/', college_view, name='college_view'),
    path('branch/<int:branch_id>/', branch_view, name='branch_view'),
    path('semester/<int:semester_id>/', semester_view, name='semester_view'),
    # # path('course/<int:course_id>/', views.course_view, name='course_view'),
    # path('course/int:college_id/int:branch_id/int:semester_id/int:course_id/', views.course_view, name='course_view'),
    # path('instructor/<int:instructor_id>/', instructor_view, name='instructor_view'),
    # path('post/<int:post_id>/', post_view, name='post_view'),
]
