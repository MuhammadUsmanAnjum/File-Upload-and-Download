from django.urls import path
from . import views
urlpatterns = [
    path('file_upload/',views.upload_file),
    path('dashboard/', views.get_dashboard),
    path('download/<int:pk>/', views.download_file, name='download_file'),
]
