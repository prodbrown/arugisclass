from django.shortcuts import render, redirect
from .forms import*
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import User  # Import your custom User model
from django.views import generic
from django.contrib.auth.forms import UserChangeForm
from django.urls import reverse_lazy


from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import UpdateView
from .forms import UserEditForm



from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.views.generic.edit import FormView


from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .forms import ForgotPasswordForm


from django.views.generic import ListView, UpdateView
# Create your views here.



def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'registration/register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('dashboard')
            elif user is not None and user.is_cr:
                login(request, user)
                return redirect('dashboard')
            elif user is not None and user.is_student:
                login(request, user)
                return redirect('dashboard')
            else:
                msg= 'Incorrect username or password'
        else:
            msg = 'error validating form'
    return render(request, 'registration/login.html', {'form': form, 'msg': msg})


def admin(request):
    return render(request,'admin.html')


def cr(request):
    return render(request,'cr.html')


def student(request):
    return render(request,'student.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login') 


def user_list(request):
    users = User.objects.all()  # Retrieve all users from the database
    return render(request, 'user_list.html', {'users': users})



class UserEditView(LoginRequiredMixin, UpdateView):
    model = User  # Assuming you are using the built-in User model
    form_class = UserEditForm  # Assuming you have created a form for user profile editing
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('login')  # Redirect to login page after successful update

    def get_object(self, queryset=None):
        return self.request.user  # Get the current logged-in user as the object to be updated

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # Pass the current user to the form
        return kwargs




class PasswordChangeView(LoginRequiredMixin, FormView):
    template_name = 'registration/change_password.html'
    form_class = CustomPasswordChangeForm
    success_url = reverse_lazy('login')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        user = self.request.user
        form.save()
        # Important: to keep the user logged in after password change,
        # update the session auth hash
        update_session_auth_hash(self.request, user)
        return super().form_valid(form)





from django.contrib.auth import get_user_model

User = get_user_model()


from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            # Authenticate the user using the default password
            user = authenticate(username=user.username, password='aru_gis1234')
            if user is not None:
                login(request, user)
                messages.success(request, 'You have successfully logged in. Please change your password.')
                return redirect('change-password')  # Redirect to change password page
            else:
                messages.error(request, 'Failed to log in with the default password.')
        except User.DoesNotExist:
            messages.error(request, 'User with this email does not exist.')
    return render(request, 'registration/forgot_password.html')

# Add views for changing password and other necessary views here



class UserListView(ListView):
    model = User
    template_name = 'user_list.html'

class UserUpdateView(UpdateView):
    model = User
    fields = ['username', 'email', 'is_admin', 'is_cr', 'is_student', 'middle_name', 'registration_number', 'gender', 'groups', 'user_permissions']
    template_name = 'user_update.html'
    success_url = reverse_lazy('login')



def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')