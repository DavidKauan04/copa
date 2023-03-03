from django.urls import path
from . import views

urlpatterns = [
    path('teams/', views.TeamViews.as_view()),
    path('teams/<int:team_id>/', views.TeamViewId.as_view())
]