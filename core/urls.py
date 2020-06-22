from django.urls import path

from . import views

app_name = "core"
urlpatterns = [
    path("", views.home, name="home"),
    path("upload/", views.UploadView.as_view(), name="upload"),
]
