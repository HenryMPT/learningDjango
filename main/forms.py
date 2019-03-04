from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from tinymce.widgets import TinyMCE
from django.db import models
from .models import Post
from django.forms import ModelForm

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user





class PostForm(ModelForm):
	username = User.username
	title = forms.CharField()
	body = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    
	class Meta:
		model = Post
		exclude = ('username', 'published')


#	def save(self, commit=True):
#		self.title = self.cleaned_data['title']
#		self.title = self.cleaned_data['body']
#		models.Model.save(self)
		
