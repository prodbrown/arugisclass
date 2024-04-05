from django.urls import path, include
from django.contrib.auth import views as auth_views  # Import auth_views for the built-in authentication views
from . import views
from .views import logout_view, user_list, UserEditView, PasswordChangeView, forgot_password, about, contact, services


urlpatterns = [

    path('account/login/', views.login_view, name='login'),
    path('account/register/', views.register, name='register'),
    path('adminpage/', views.admin, name='adminpage'),
    path('crpage/', views.cr, name='crpage'),
    path('studentpage/', views.student, name='studentpage'),
    path('logout/', logout_view, name='logout'),

    path('edit_profile/', UserEditView.as_view(), name='edit-profile'),
    path('change_password/', PasswordChangeView.as_view(), name='change-password'),

    path('custom_password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='custom_password_reset'),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),



    path('admin/ClassAccountApp/user/', views.UserListView.as_view(), name='user_list'),
    path('users/<int:pk>/', views.UserUpdateView.as_view(), name='user_update'),



    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),


] 
