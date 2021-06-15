from django.urls import path

from . import views


urlpatterns = [
    path('tasks/', views.TaskViewList.as_view()),
    # path('users/', views.TaskViewList.as_view()),
    path('<int:id>/', views.TaskViewDetail.as_view()),
]