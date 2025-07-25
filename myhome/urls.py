from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.home),
        path('upload-audio/', views.upload_audio, name='upload_audio'),  # <-- This is the one you need
    path('transcription_result/', TemplateView.as_view(template_name='transcription_result.html')),

]