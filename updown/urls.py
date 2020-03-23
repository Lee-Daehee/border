from django.urls import path, re_path
from updown import views

app_name = "UD"

urlpatterns = [
    path('', views.index, name="I"),
    path('upload/', views.upload, name="U"),
    re_path(r'^download/([0-9]+)/([0-9a-zA-Z-.]+)$', views.download, name="D"),
    re_path(r'^delete/([0-9]+)/([0-9a-zA-Z-.]+)$', views.delete, name="L"),
]