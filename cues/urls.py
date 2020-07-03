from django.urls import path
from . import views

app_name = "cues"

urlpatterns = [
    path("", views.CuesView.as_view()),
    path("<int:pk>/", views.CueView.as_view()),
]