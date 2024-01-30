from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
        path('register/',UserRegistration,name='register_user'),
        path('login/',Login,name='login'),
        path('logout/',Logout,name='logout'),
        path('reset_password_user_email/',auth_views.PasswordResetView.as_view(success_url="/reset_password_email_sent/",template_name='users/reset_password_user_email.html'),name='reset_password_user_email'),
        path('reset_password_email_sent/',auth_views.PasswordResetDoneView.as_view(template_name = 'users/reset_password_email_sent.html'),name='reset_password_email_sent'),
        path('reset_password_confirm/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(success_url="/reset_password_complete",template_name = "users/reset_password_new_password.html"),name='password_reset_confirm'),
        path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="users/reset_password_complete.html"),name='reset_password_complete'),
]
