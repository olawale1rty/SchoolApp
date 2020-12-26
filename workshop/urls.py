from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('', views.home, name="home"),
	path('register/', views.registerPage, name="register"),
	path('profile/<username>/',views.profile,name='profile'),
	path('workshop/',views.registerWorkshop,name='workshop'),
	path('edit_profile/', views.update_profile, name='update-profile'),
	path('login/', auth_views.LoginView.as_view(template_name='workshop/login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='workshop/logout.html'), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
