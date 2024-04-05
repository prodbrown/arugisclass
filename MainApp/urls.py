"""
URL configuration for ClassProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import*

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', FirstView.as_view(), name='first-view'),
    path('dashboard', DashboardView.as_view(), name='dashboard'),



    path('post/', PostView.as_view(), name='post-view'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail-view'),
    path('add-post/', AddPostView.as_view(), name='add-post'),
    path('post/edit/<int:pk>/', UpdatePostView.as_view(), name='update-post'),
    path('post/<int:pk>/delete/', DeletePostView.as_view(), name='delete-post'),

    path('add-course/', AddCourseView.as_view(), name='add-course'),
    path('course/list/', CourseListView.as_view(), name='course-list'),
    path('course/<str:cats>/', course_view, name='course-view'),


    path('notes/', NotesView.as_view(), name='notes-view'),
    path('notes/<int:pk>/', NotesDetailView.as_view(), name='notes_detail-view'),
    path('add-notes/', AddNotesView.as_view(), name='add-notes'),
    path('notes/edit/<int:pk>/', UpdateNotesView.as_view(), name='update-notes'),
    path('notes/<int:pk>/delete/', DeleteNotesView.as_view(), name='delete-notes'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
