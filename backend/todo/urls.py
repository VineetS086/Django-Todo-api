from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views


urlpatterns = [
    path('tasks/', views.TaskViewList.as_view()),
    # path('users/', views.TaskViewList.as_view()),
    path('tasks/<int:id>/', views.TaskViewDetail.as_view()),

    path('auth-token/', obtain_auth_token),
    path('user-register/', views.ReqisterView.as_view()),
]