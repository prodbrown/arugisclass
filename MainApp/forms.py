from django import forms
from .models import Post, Notes, Course

choices = Course.objects.all().values_list('course_name', 'course_name')
choice_list = []

for item in choices:
    choice_list.append(item)



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'post_image', 'post_file')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'post_image': forms.FileInput(attrs={'class': 'form-control'}),
            'post_file': forms.FileInput(attrs={'class': 'form-control'}),

        }

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('course', 'title', 'header_image', 'header_file', 'body')

        widgets = {
            'course': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'header_image': forms.FileInput(attrs={'class': 'form-control'}),
            'header_file': forms.FileInput(attrs={'class': 'form-control'}),
        }


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_name', 'course_code', 'lecture_teacher', 'practical_teacher']
        widgets = {
            'course_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Course Name'}),
            'course_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Course Code'}),
            'lecture_teacher': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Lecture Teacher'}),
            'practical_teacher': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Practical Teacher'}),
        }