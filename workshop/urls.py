from django.urls import path
from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('', views.loginPage, name="login"), 
	path('home/', views.home, name="home"),
	path('register/', views.registerPage, name="register"),
	 
	path('logout/', views.logoutUser, name="logout"),
	path('profile/',views.profile,name='profile'),
	path('workshop/',views.workshop,name='workshopsi'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
