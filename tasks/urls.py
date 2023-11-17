from django.urls import path
from . import views


urlpatterns = [
    path('v1/tasks/', views.CreateListTasksApiView.as_view() ),
    path('v1/tasks/<int:pk>/', views.TaskDetailApiView.as_view() ),
    path('v1/tasks/<int:pk>/update/', views.TaskUpdateApiView.as_view() ),
    path('v1/tasks/<int:pk>/delete/', views.TaskDestroyApiView.as_view() ),
]