from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import TaskModel
from .serializers import TaskSerializer



# @api_view(['GET', 'POST'])
# def task_list(request):
#     if request.method == 'GET':
#         tasks = TaskModel.objects.all()
#         serializer = TaskSerializer(tasks, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = TaskSerializer(data=request.data, many=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PATCH', 'PUT', 'DELETE'])
# def task_details(request, pk):
#      task = get_object_or_404(TaskModel, id=pk)
#      if task.DoesNotExist:
#          return Response(status=status.HTTP_404_NOT_FOUND)
    
#      if request.method == 'GET':
#        serializer = TaskSerializer(task).data
#        return Response(serializer, status=status.HTTP_200_OK )
     
#      elif request.method == 'PUT':
#         serializer = TaskModel(task, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#      elif request.method == 'DELETE':
#          ids = request.query_params.get('id')
#          if len(ids) > 1:
#              task = TaskModel.objects.filter(id__in=ids)
#              task.delete()
#          else: task.delete()
#          return Response(status=status.HTTP_204_NO_CONTENT)

class CreateListTasksApiView(generics.ListCreateAPIView):
    queryset = TaskModel.objects.all()
    serializer_class = TaskSerializer

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data, many=True)
    #     if serializer.is_valid(raise_exception=True):
    #         self.perform_create(serializer)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class TaskDetailApiView(generics.RetrieveAPIView):
    queryset = TaskModel.objects.all()
    serializer_class = TaskSerializer



class TaskUpdateApiView(generics.UpdateAPIView):
    queryset = TaskModel.objects.all()
    serializer_class = TaskSerializer
    lookup_field = "pk"




class TaskDestroyApiView(generics.DestroyAPIView):
    queryset = TaskModel.objects.all()
    serializer_class = TaskSerializer
    lookup_field = "pk"

    # def perform_destroy(self, instance):
    #     super().perform_destroy(instance)

    
