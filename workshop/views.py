from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, RegisterWorkshopUserForm
from django.http import HttpResponseForbidden
from .models import User, Workshop
from django.contrib.admin.views.decorators import staff_member_required, user_passes_test

def home(request):
	context={
		'workshops':Workshop.objects.all()
	}
	return render(request,'workshop/home.html', context)

@login_required
def registerWorkshop(request):
	if request.method == 'POST':
		form = RegisterWorkshopUserForm(request.POST)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.user = request.user
			obj.save()
			workshop = form.cleaned_data.get('workshop')
			messages.success(request, 'Successfully registered for ' + workshop)
			return redirect('home')
		else:
			messages.error(request, 'Unable to register')
			return redirect('home')
	else:
		form = RegisterWorkshopUserForm()	
	context = {'form':form}
	return render(request, 'workshop/workshop.html', context)


def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request, 'Account was created for ' + user)
			return redirect('login')
	else:
		form = UserRegisterForm()	
	context = {'form':form}
	return render(request, 'workshop/register.html', context)


def profile(request, username):
	context = {
		'title': 'Profile',
		'user_data': User.objects.get(username=username)
	}
	return render(request, 'workshop/profile.html', context)

@login_required
def update_profile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST,
								   request.FILES,
								   instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Your account has been updated!')
			return redirect('profile', username=request.user.username)

	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)

	context = {
		'u_form': u_form,
		'p_form': p_form
	}

	return render(request, 'workshop/update_profile.html', context)

		 
