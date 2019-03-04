from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tutorial, Post
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm, PostForm
from django.contrib.auth.models import User


def homepage(request):
	return render(request=request,
				  template_name="main/home.html",
				  context={"tutorials": Tutorial.objects.all().order_by('-tutorial_published')})

def snippets(request):
	return render(request=request,
				  template_name="main/snippets.html",
				  context={"posts": Post.objects.all().order_by('-published')})

def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f"New Account Created: {username}")
			login(request, user)
			messages.info(request, f"You are now logged in as {username}")
			return redirect("main:homepage")
		else:
			for msg in form.error_messages:
				messages.error(request, f"{msg}: {form.error_messages[msg]}")

def post(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.username = request.user
			messages.success(request, f"Snippet Posted!")
			post.save()
			return redirect("main:homepage")
		else:
			for msg in form.error_messages:
				messages.error(request, f"{msg}: {form.error_messages[msg]}")
	form = PostForm()
	return render(request,
				  "main/post.html",
				  context={"form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "Logged out successfully!")
	return redirect("main:homepage")

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}")
				return redirect("main:homepage")
			else:
				messages.error(request, "Invalid username or password")

		else:
			messages.error(request, "Invalid username or password")

	form = AuthenticationForm()
	return render(request,
				  "main/login.html",
				  {"form":form})