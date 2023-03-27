from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from .models import Student
from app.serializers import StudentSerializer
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status


from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
# Create your views here.



@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def StudentList(request,format=None):
    if request.method == 'GET':
        data = Student.objects.all()
        serializer = StudentSerializer(data,many=True)
        return Response(serializer.data)
 
 
@swagger_auto_schema(method='post', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'fname': openapi.Schema(type=openapi.TYPE_STRING),
        'lname': openapi.Schema(type=openapi.TYPE_STRING),
        'email': openapi.Schema(type=openapi.TYPE_STRING),
        'contact': openapi.Schema(type=openapi.TYPE_STRING),
        # add more fields as necessary
    }
))   
@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def StudentPost(request,format=None):
    if request.method == 'POST':
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


      
# @api_view(['PUT', 'PATCH'])
# @permission_classes((permissions.AllowAny,))
# def my_model_update(request, pk):
#     try:
#         my_model = Student.objects.get(pk=pk)
#     except Student.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     serializer = StudentSerializer(my_model, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
@api_view(['DELETE'])
@permission_classes((permissions.AllowAny,))
def StudentDelete(request,pk):
    if request.method == 'DELETE':
        data = Student.objects.get(id=pk)
        data.delete()
        return Response("Record Deleted Successfully")\
            

# @swagger_auto_schema(method='put', request_body=openapi.Schema(
#     type=openapi.TYPE_OBJECT,
#     properties={
#         'fname': openapi.Schema(type=openapi.TYPE_STRING),
#         'lname': openapi.Schema(type=openapi.TYPE_STRING),
#         'email': openapi.Schema(type=openapi.TYPE_STRING),
#         'contact': openapi.Schema(type=openapi.TYPE_STRING),
#         # add more fields as necessary
#     }
# ))             
# @api_view(['PUT'])
# @permission_classes((permissions.AllowAny,))
# def StudentUpdate(request,pk):
#     if request.method == 'PUT':
#         student = Student.objects.get(id=pk)
#         serializer = StudentSerializer(instance=student, data = request.data)
#         serializer.save()
#         return Response("Record Updated Successfully")
    
@swagger_auto_schema(method='put', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'fname': openapi.Schema(type=openapi.TYPE_STRING),
        'lname': openapi.Schema(type=openapi.TYPE_STRING),
        'email': openapi.Schema(type=openapi.TYPE_STRING),
        'contact': openapi.Schema(type=openapi.TYPE_STRING),
        # add more fields as necessary
    }
))
@api_view(['PUT'])
@permission_classes((permissions.AllowAny,))
def update_data(request, pk):
    # retrieve data from request
    data = request.data
    
    # perform actions with the data to update the specified data_id
    # ...
    
    # return a response
    return Response({'message': f'Data with id {pk} updated successfully!'})