from django.urls import path
from .views import (
    home,
    student_api,
    student_api_get_update_delete,
    # students_list,
    # student_create,
    # student_detail,
    # student_update,
    # student_delete,
) 

urlpatterns = [
   path("", home),
   path('student/', student_api),
   path('student/<int:pk>', student_api_get_update_delete)
#    path("student-list/", students_list, name='list'),
#    path("student-create/", student_create, name='create'),
#    path("student-detail/<int:id>", student_detail, name='detail'),
#    path("student-update/<int:id>", student_update, name='update'),
#    path("student-delete/<int:id>", student_delete, name='delete'),
]