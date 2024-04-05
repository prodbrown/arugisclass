from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Notes, Course
from .forms import PostForm, NotesForm, CourseForm 
from django.urls import reverse_lazy


class FirstView(TemplateView):
    template_name = 'index.html'

class DashboardView(TemplateView):
    template_name = 'home.html'

class PostView(ListView):
    model = Post
    template_name = 'post.html'
    ordering = ['-post_date','-id']

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm 
    template_name = 'add_post.html'

class UpdatePostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'update_post.html'
#    fields = ['title', 'body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('post-view')





#Notes

class NotesView(ListView):
    model = Notes
    template_name = 'notes.html'
    ordering = ['-notes_date','-id']

class NotesDetailView(DetailView):
    model = Notes
    template_name = 'notes_detail.html'

class AddNotesView(CreateView):
    model = Notes
    form_class = NotesForm 
    template_name = 'add_notes.html'

class UpdateNotesView(UpdateView):
    model = Notes
    form_class = NotesForm
    template_name = 'update_notes.html'
#    fields = ['title', 'body']

class DeleteNotesView(DeleteView):
    model = Notes
    template_name = 'delete_notes.html'
    success_url = reverse_lazy('notes-view')





#COURSE
class AddCourseView(CreateView):
    model = Course
    form_class = CourseForm  # Use your custom form here
    template_name = 'add_course.html'

def course_view(request, cats):
    course_posts = Notes.objects.filter(course=cats)
    course_posts = course_posts.order_by('id')  # Order alphabetically by title
    return render(request, 'course.html', {'cats': cats, 'course_posts': course_posts})

class CourseListView(ListView):
    model = Course
    template_name = 'course_list.html'
    ordering = ['course_name']