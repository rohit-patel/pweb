from django.contrib import admin

from .models import Skill, AIProject, Contact, Research

admin.site.register(Skill)

@admin.register(Research)
class ResearchAdmin(admin.ModelAdmin):
	list_display = ('title','author',)
	prepopulated_fields = {"slug": ("title",)}

@admin.register(AIProject)
class AIProjectAdmin(admin.ModelAdmin):
	list_display = ('title',)
	prepopulated_fields = {"slug": ("title",)}

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'number')