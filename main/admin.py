from django.contrib import admin
from .models import Tutorial, Post, TutorialCategory, TutorialSeries, Organization
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.
class TutorialAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Title/date", {'fields': ["tutorial_title", "tutorial_published"]}),
        ("URL", {'fields': ["tutorial_slug"]}),
        ("Series", {'fields': ["tutorial_series"]}),
        ("Content", {"fields": ["tutorial_content"]})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
        }




class PostAdmin(admin.ModelAdmin):
	fieldsets = [
		("Title/date", {"fields": ["username", "published"]}),
		("Body", {"fields":["body"]})
	]
	formfield_overrides = {
		models.TextField: {'widget': TinyMCE()}
	}




admin.site.register(TutorialSeries)
admin.site.register(TutorialCategory)
admin.site.register(Tutorial,TutorialAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Organization)