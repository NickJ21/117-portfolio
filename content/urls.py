from django.urls import path
from django.conf.urls.static import static
from .views import get_all_projects_list, get_all_experience_list
from django.conf import settings

urlpatterns = [
    path('', get_all_projects_list, name="projects_list"),
    path('experiences', get_all_experience_list, name="experience_list")
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)