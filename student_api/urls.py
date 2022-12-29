from django.urls import path, include
from rest_framework import routers
from .views import (
    home,
    # student_api,
    # student_api_get_update_delete,
    # students_list,
    # student_create,
    # student_detail,
    # student_update,
    # student_delete,
    #! class wievs
    # StudentListCreate,
    # StudentDetail,
    #!GEnericapiwies
    # StudentGAV,
    # StudentDetailGAV,
    #! ConcreteView
    # StudentCV,
    # StudentDetailCV
    #!ModelView
    StudentMVS,
    PathMVS
    
) 
router =routers.DefaultRouter()
router.register("student", StudentMVS)
router.register("path", PathMVS)

urlpatterns = [
   path("", home),
#    path('student/', student_api),
#    path('student/<int:pk>', student_api_get_update_delete)
#    path("student-list/", students_list, name='list'),
#    path("student-create/", student_create, name='create'),
#    path("student-detail/<int:id>", student_detail, name='detail'),
#    path("student-update/<int:id>", student_update, name='update'),
#    path("student-delete/<int:id>", student_delete, name='delete'),
#! class wievs
    # path("student/", StudentListCreate.as_view()),
    # path("student/<int:pk>", StudentDetail.as_view()),
#!GEnericapiwies
    # path("student/", StudentGAV.as_view()),
    # path("student/<int:pk>", StudentDetailGAV.as_view()),
#! Concretewiev
    # path("student/", StudentCV.as_view()),
    # path("student/<int:pk>", StudentDetailCV.as_view()),
#!ModelView
    path("",include(router.urls)),
    

]