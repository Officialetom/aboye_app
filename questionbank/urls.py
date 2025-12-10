from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="questionbank_home"),
    path("add/", views.add_question, name="add_question"),
    path("view/<int:pk>/", views.view_question, name="view_question"),
    path("download/txt/", views.download_txt, name="download_txt"),
]
