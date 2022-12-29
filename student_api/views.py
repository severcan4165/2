from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Student, Path
from .serializers import StudentSerializer, PathSerializer
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, mixins, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet


@api_view()
def home(request):
    return Response({'home':'This is home Page..'})

# @api_view(['GET'])
# def students_list(request):
#     students = Student.objects.all()
#     print(students)
#     serializer = StudentSerializer(students, many=True)
#     print(serializer)
#     print(serializer.data)

#     return Response(serializer.data)

# @api_view(['POST'])
# def student_create(request):
#     serializer = StudentSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response("succesful", status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET'])
# def student_detail(request, id):
#     student = get_object_or_404(Student, id=id)
#     serializer = StudentSerializer(student)
#     return Response(serializer.data)

# @api_view(['PUT'])
# def student_update(request, id):
#     student = get_object_or_404(Student, id=id)
#     serializer = StudentSerializer(instance = student, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response("succesful", status=status.HTTP_200_OK)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['DELETE'])
# def student_delete(request, id):
#     student = get_object_or_404(Student, id=id)
#     student.delete()
#     return Response("Deleted succesfully", status=status.HTTP_200_OK)

###################################################################################

# @api_view(['GET', 'POST'])
# def student_api(request):
#     if request.method == 'GET':
#         students = Student.objects.all()
#         serializer = StudentSerializer(students, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             data = {
#                 "message": f"Student {serializer.validated_data.get('first_name')} saved successfully!"}
#             return Response(data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
# def student_api_get_update_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Student {student.last_name} updated successfully"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = StudentSerializer(student, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Student {student.last_name} updated successfully"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        student.delete()
        data = {
            "message": f"Student {student.last_name} deleted successfully"
        }
        return Response(data)


# class StudentListCreate(APIView):
#     def get(self, request):
#         students = Student.objects.all()
#         serializer = StudentSerializer(students, many=True)
#         return Response(serializer.data)
#     def post(self, request):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             data = {
#                 "message": f"Student {serializer.validated_data.get('first_name')} saved successfully!"}
#             return Response(data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class StudentDetail(APIView):
#     def get_obj(self, pk):
#         return get_object_or_404(Student, pk = pk)
    
#     def get(self, request, pk):
#         student = self.get_obj(pk)
#         serializer = StudentSerializer(student)
#         return Response(serializer.data)
#     def put(self, request, pk):
#         student = self.get_obj(pk)
#         serializer = StudentSerializer(student, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response("succesful", status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     def delete(self, request, pk):
#         student = self.get_obj(pk)
#         student.delete()
#         return Response("Deleted succesfully", status=status.HTTP_200_OK)


###### ! GENERICAPIwiev

# class StudentGAV(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# class StudentDetailGAV(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
    
#!Concrete View
# class StudentCV(ListCreateAPIView):

#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class StudentDetailCV(RetrieveUpdateDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#!Model View
from .pagination import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
class StudentMVS(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = CustomPageNumberPagination
    # pagination_class = CustomLimitOffsetPagination
    # pagination_class = CustomCursorPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields =['first_name', 'id']
    search_fields =['first_name', 'id']
    
    @action(detail=False, methods=["GET"])
    def student_count(self, request):
        count = {
            "student-count": self.queryset.count()
        }
        return Response(count)
        
class PathMVS(ModelViewSet):

    queryset = Path.objects.all()
    serializer_class = PathSerializer
    
    @action(detail=True)
    def student_names(self, request, pk=None):
        path = self.get_object()
        students = path.students.all()
        return Response([i.first_name for i in students])