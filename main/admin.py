from django.contrib import admin
from .models import Tutorial, Post
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.
class TutorialAdmin(admin.ModelAdmin):
	fieldsets = [
		("Title/date", {"fields": ["tutorial_title", "tutorial_published"]}),
		("Content", {"fields":["tutorial_content"]})
	]

	formfield_overrides = {
		models.TextField: {'widget': TinyMCE()}
	}

class PostAdmin(admin.ModelAdmin):
	fieldsets = [
		("Title/date", {"fields": ["username", "published"]}),
		("Body", {"fields":["body"]})
	]
	formfield_overrides = {
		models.TextField: {'widget': TinyMCE()}
	}

admin.site.register(Tutorial, TutorialAdmin)
admin.site.register(Post, PostAdmin)