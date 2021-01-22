from django.contrib import admin
from . import views
from django.urls import include, path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static




# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', views.index, name='index'),
    path('scrap/', views.scrap, name='scrap'),
    path('emailsearcher/', views.emailsearcher, name='emailsearcher'),
    path('login/', views.userlogin, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logoutUser, name="logout"),
    path('api/', views.apiOverview.as_view(), name='api'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="leadfinderapp/forgot-password.html"), name="lostpassword"),
    path('reset_password_sent/',
        auth_views.PasswordResetDoneView.as_view(template_name="leadfinderapp/password_reset_sent.html"),
        name="password_reset_done"),
    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="leadfinderapp/password_reset_form.html"),
     name="password_reset_confirm"),
    path('reset_password_complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name="leadfinderapp/password_reset_done.html"),
        name="password_reset_complete"),
        
]
